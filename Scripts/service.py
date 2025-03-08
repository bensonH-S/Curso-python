import os
import shutil
import time
import win32serviceutil
import win32service
import win32event

class CopyFileService(win32serviceutil.ServiceFramework):
    _svc_name_ = "CopyFileService"
    _svc_display_name_ = "Copy File Service"
    _svc_description_ = "Service that copies a file every hour."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.running = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.running = False

    def SvcDoRun(self):
        while self.running:
            self.copy_file()
            time.sleep(3600)  # Espera 1 hora

    def copy_file(self):
        src = r"C:\Users\u811737\OneDrive - BRB - Banco de Brasilia SA\Arquivos de Chat do Microsoft Teams\PAGAMENTOS DE AGÊNCIAS 2025-corrigido.xlsm"
        dst = r"W:\_GERAL\gecafpag\PAGAMENTOS DE AGÊNCIAS 2025-corrigido.xlsm"
        shutil.copy2(src, dst)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(CopyFileService)