import sqlite3
import os
from datetime import datetime
import locale

# Definindo o local para formatação monetária (Brasil)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Função para conectar ao banco de dados
def conectar_banco(banco):
    conn = sqlite3.connect(banco)
    return conn.cursor()

# Função para consultar o valor da coluna DistributionPoint do dia
def consultar_distribution_point(cursor, data):
    query = f"""
    SELECT DISTINCT DistributionPoint 
    FROM Orders 
    WHERE BusinessPeriod = '{data}';
    """
    cursor.execute(query)
    resultado = cursor.fetchone()
    return resultado[0] if resultado else None

# Funções para consultar os dados do banco com base na data
def consultar_dados(cursor, data, estado):
    query = f"""
    SELECT SUM(PriceListTotal) AS TotalPrice 
    FROM Orders 
    WHERE StateId = {estado} 
    AND BusinessPeriod = '{data}';
    """
    cursor.execute(query)
    resultado = cursor.fetchone()
    return resultado[0] if resultado[0] else 0

def consultar_credito(cursor, data):
    query = f"""
    SELECT SUM(ot.TenderAmount) AS TotalTenderAmount
    FROM Orders o
    JOIN OrderTender ot ON o.OrderId = ot.OrderId
    WHERE o.BusinessPeriod = '{data}'
    AND ot.TenderId = 1;  -- TenderId 1 corresponde ao Cartão Crédito
    """
    cursor.execute(query)
    resultado = cursor.fetchone()
    return resultado[0] if resultado[0] else 0

def consultar_pix(cursor, data):
    query = f"""
    SELECT SUM(ot.TenderAmount) AS TotalTenderAmount
    FROM Orders o
    JOIN OrderTender ot ON o.OrderId = ot.OrderId
    WHERE o.BusinessPeriod = '{data}'
    AND ot.TenderId = 51;  -- TenderId 51 corresponde ao PIX
    """
    cursor.execute(query)
    resultado = cursor.fetchone()
    return resultado[0] if resultado[0] else 0

def consultar_dinheiro(cursor, data):
    query = f"""
    SELECT SUM(ot.TenderAmount) AS TotalTenderAmount
    FROM Orders o
    JOIN OrderTender ot ON o.OrderId = ot.OrderId
    WHERE o.BusinessPeriod = '{data}'
    AND ot.TenderId = 0;  -- TenderId 0 corresponde ao Dinheiro
    """
    cursor.execute(query)
    resultado = cursor.fetchone()
    return resultado[0] if resultado[0] else 0

def consultar_debito(cursor, data):
    query = f"""
    SELECT SUM(ot.TenderAmount) AS TotalTenderAmount
    FROM Orders o
    JOIN OrderTender ot ON o.OrderId = ot.OrderId
    WHERE o.BusinessPeriod = '{data}'
    AND ot.TenderId = 2;  -- TenderId 2 corresponde ao Cartão Débito
    """
    cursor.execute(query)
    resultado = cursor.fetchone()
    return resultado[0] if resultado[0] else 0

def consultar_ifood(cursor, data):
    query = f"""
    SELECT SUM(ot.TenderAmount) AS TotalTenderAmount
    FROM Orders o
    JOIN OrderTender ot ON o.OrderId = ot.OrderId
    WHERE o.BusinessPeriod = '{data}'
    AND ot.TenderId = 28;  -- TenderId 28 corresponde ao IFOOD
    """
    cursor.execute(query)
    resultado = cursor.fetchone()
    return resultado[0] if resultado[0] else 0

def consultar_rappi(cursor, data):
    query = f"""
    SELECT SUM(ot.TenderAmount) AS TotalTenderAmount
    FROM Orders o
    JOIN OrderTender ot ON o.OrderId = ot.OrderId
    WHERE o.BusinessPeriod = '{data}'
    AND ot.TenderId = 33;  -- TenderId 33 corresponde ao RAPPI
    """
    cursor.execute(query)
    resultado = cursor.fetchone()
    return resultado[0] if resultado[0] else 0

# Função para formatar o valor com duas casas decimais e como valor monetário
def formatar_valor(valor):
    return locale.currency(valor, grouping=True)

# Função para buscar todos os bancos de dados chamados 'order'
def buscar_bancos(pasta):
    bancos = []
    for arquivo in os.listdir(pasta):
        if arquivo.startswith("order.db") and ".filepart" not in arquivo:
            bancos.append(os.path.join(pasta, arquivo))
    return bancos

# Função para converter a data no formato dd/mm/yyyy para yyyymmdd
def converter_data(data_str):
    try:
        data_obj = datetime.strptime(data_str, "%d/%m/%Y")
        return data_obj.strftime("%Y%m%d")
    except ValueError:
        return None

# Função para criar o arquivo de log para PDV
def criar_log_pdv(caminho_banco, data, tipo):
    cursor = conectar_banco(caminho_banco)

    venda = consultar_dados(cursor, data, 5)  # Estado 5: Pago
    cancelado = consultar_dados(cursor, data, 4)  # Estado 4: Cancelado
    credito = consultar_credito(cursor, data)  # Cartão Crédito (TenderId 1)
    pix = consultar_pix(cursor, data)  # PIX (TenderId 51)
    dinheiro = consultar_dinheiro(cursor, data)  # Dinheiro (TenderId 0)
    debito = consultar_debito(cursor, data)  # Cartão Débito (TenderId 2)

    vendas_total = venda + cancelado

    if venda > 0 or cancelado > 0 or credito > 0 or pix > 0 or dinheiro > 0 or debito > 0:
        with open(f"log_{os.path.basename(caminho_banco)}.txt", "w", encoding="utf-8") as log_file:
            log_file.write("=======================================\n")
            log_file.write("        Relatório de Vendas\n")
            log_file.write("=======================================\n\n")
            log_file.write(f"Banco de Dados:   {os.path.basename(caminho_banco)}\n")
            log_file.write(f"Data:             {data}\n")
            log_file.write(f"Tipo:             PDV\n\n")
            log_file.write("---------------------------------------\n")
            log_file.write(f"Vendas Totais:            {formatar_valor(vendas_total)}\n\n")
            log_file.write(f"Cancelado:                {formatar_valor(cancelado)}\n")
            log_file.write("---------------------------------------\n")
            log_file.write(f"Dinheiro:                 {formatar_valor(dinheiro)}\n")
            log_file.write(f"Cartão de Crédito:        {formatar_valor(credito)}\n")
            log_file.write(f"Cartão de Débito:         {formatar_valor(debito)}\n")
            log_file.write(f"PIX:                      {formatar_valor(pix)}\n\n")
            log_file.write("---------------------------------------\n")
            log_file.write(f"Vendas Líquidas:          {formatar_valor(venda)}\n")
            log_file.write("=======================================\n")

# Função para criar o arquivo de log para Totem
def criar_log_totem(caminho_banco, data, tipo):
    cursor = conectar_banco(caminho_banco)

    venda = consultar_dados(cursor, data, 5)  # Estado 5: Pago
    cancelado = consultar_dados(cursor, data, 4)  # Estado 4: Cancelado
    credito = consultar_credito(cursor, data)  # Cartão Crédito (TenderId 1)
    pix = consultar_pix(cursor, data)  # PIX (TenderId 51)
    dinheiro = consultar_dinheiro(cursor, data)  # Dinheiro (TenderId 0)
    debito = consultar_debito(cursor, data)  # Cartão Débito (TenderId 2)

    vendas_total = venda + cancelado

    if venda > 0 or cancelado > 0 or credito > 0 or pix > 0 or dinheiro > 0 or debito > 0:
        with open(f"log_{os.path.basename(caminho_banco)}.txt", "w", encoding="utf-8") as log_file:
            log_file.write("=======================================\n")
            log_file.write("        Relatório de Vendas\n")
            log_file.write("=======================================\n\n")
            log_file.write(f"Banco de Dados:   {os.path.basename(caminho_banco)}\n")
            log_file.write(f"Data:             {data}\n")
            log_file.write(f"Tipo:             TOTEM\n\n")
            log_file.write("---------------------------------------\n")
            log_file.write(f"Vendas Totais:            {formatar_valor(vendas_total)}\n\n")
            log_file.write(f"Cancelado:                {formatar_valor(cancelado)}\n")
            log_file.write("---------------------------------------\n")
            log_file.write(f"Cartão de Crédito:        {formatar_valor(credito)}\n")
            log_file.write(f"Cartão de Débito:         {formatar_valor(debito)}\n")
            log_file.write(f"PIX:                      {formatar_valor(pix)}\n\n")
            log_file.write("---------------------------------------\n")
            log_file.write(f"Vendas Líquidas:          {formatar_valor(venda)}\n")
            log_file.write("=======================================\n")

# Função para criar o arquivo de log para Delivery
def criar_log_delivery(caminho_banco, data, tipo):
    cursor = conectar_banco(caminho_banco)

    venda = consultar_dados(cursor, data, 5)  # Estado 5: Pago
    cancelado = consultar_dados(cursor, data, 4)  # Estado 4: Cancelado
    ifood = consultar_ifood(cursor, data)  # IFOOD (TenderId 28)
    rappi = consultar_rappi(cursor, data)  # RAPPI (TenderId 33)

    vendas_total = venda + cancelado

    if venda > 0 or cancelado > 0 or ifood > 0 or rappi > 0:
        with open(f"log_{os.path.basename(caminho_banco)}.txt", "w", encoding="utf-8") as log_file:
            log_file.write("=======================================\n")
            log_file.write("        Relatório de Vendas\n")
            log_file.write("=======================================\n\n")
            log_file.write(f"Banco de Dados:   {os.path.basename(caminho_banco)}\n")
            log_file.write(f"Data:             {data}\n")
            log_file.write(f"Tipo:             DELIVERY\n\n")
            log_file.write("---------------------------------------\n")
            log_file.write(f"Vendas Totais:            {formatar_valor(vendas_total)}\n\n")
            log_file.write(f"Cancelado:                {formatar_valor(cancelado)}\n")
            log_file.write("---------------------------------------\n")
            log_file.write(f"IFood:                    {formatar_valor(ifood)}\n")
            log_file.write(f"Rappi:                    {formatar_valor(rappi)}\n\n")
            log_file.write("---------------------------------------\n")
            log_file.write(f"Vendas Líquidas:          {formatar_valor(venda)}\n")
            log_file.write("=======================================\n")

# Exemplo de uso
pasta_bancos = r"F:\databases"

# Solicitar a data ao usuário
data_input = input("Digite a data (dd/mm/yyyy): ")

# Converter a data para o formato correto
data_formatada = converter_data(data_input)
if data_formatada is None:
    print("Formato de data inválido!")
else:
    bancos = buscar_bancos(pasta_bancos)

    for caminho_banco in bancos:
        cursor = conectar_banco(caminho_banco)
        tipo_relatorio = consultar_distribution_point(cursor, data_formatada)

        if tipo_relatorio:
            if "FC" in tipo_relatorio:
                criar_log_pdv(caminho_banco, data_formatada, tipo="PDV")
            elif "DL" in tipo_relatorio:
                criar_log_delivery(caminho_banco, data_formatada, tipo="DELIVERY")
            elif "TT" in tipo_relatorio:
                criar_log_totem(caminho_banco, data_formatada, tipo="TOTEM")

    print("Relatórios gerados com sucesso!")