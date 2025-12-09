import datetime
import os
import csv
from core.base_module import BaseModule

class TimesheetModule(BaseModule):
    """
    Logs the current runtime session into a CSV file.
    Simulates an automated clock-in system.
    """
    
    def execute(self):
        print(f"   [TimeSheet] 🕒 Processing Time Log...")
        
        # Data Preparation
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user = os.getenv('USERNAME') or os.getenv('USER') or "WisdomFirm_Admin"
        action = "AUTO_RUN_CHECK_IN"
        filename = "timesheet_data.csv"
        
        # Check if file needs a header
        file_exists = os.path.isfile(filename)
        
        try:
            with open(filename, mode='a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                
                if not file_exists:
                    writer.writerow(["Timestamp", "User", "Action", "Status"])
                
                writer.writerow([timestamp, user, action, "OK"])
                
            print(f"   [TimeSheet] ✅ Logged Entry: {user} @ {timestamp}")
            print(f"   [TimeSheet] 📄 File updated: {filename}")
            return True
            
        except Exception as e:
            print(f"   [TimeSheet] ❌ IO Error: {e}")
            return False
