import platform
import os
from core.base_module import BaseModule

class SystemMonitorModule(BaseModule):
    """
    Analyses the host environment and prints system specs.
    """
    
    def execute(self):
        print(f"   [SystemMonitor] 🔍 Scanning Host Infrastructure...")
        
        try:
            os_name = platform.system()
            os_release = platform.release()
            machine = platform.machine()
            
            print(f"   [SystemMonitor] ✅ OS: {os_name} {os_release} ({machine})")
            print(f"   [SystemMonitor] 💾 Python Version: {platform.python_version()}")
            return True
        except Exception as e:
            print(f"   [SystemMonitor] ⚠️ Error: {e}")
            return False
