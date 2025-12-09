import yaml
import importlib
import sys
import time

class FMSEngine:
    def __init__(self, config_path="config/settings.yaml"):
        self.config = self._load_config(config_path)
        self.modules = []
        print(f"\n⚡ {self.config.get('app_name', 'FMS Framework')} v{self.config.get('version', '1.0')} Initialized.")

    def _load_config(self, path):
        try:
            with open(path, "r") as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"❌ Critical Error: Could not load config file ({path}): {e}")
            sys.exit(1)

    def load_modules(self):
        """Dynamically loads modules defined in settings.yaml"""
        task_list = self.config.get("tasks", [])
        
        print("⚙️  Loading Modules...")
        for task_name in task_list:
            try:
                # 1. Determine file path and class name dynamically
                # Example: 'timesheet' -> modules.timesheet -> TimesheetModule
                module_path = f"modules.{task_name}"
                class_name = "".join(x.title() for x in task_name.split('_')) + "Module"
                
                # 2. Import the module
                mod = importlib.import_module(module_path)
                cls = getattr(mod, class_name)
                
                # 3. Instantiate and store
                instance = cls(self.config)
                self.modules.append(instance)
                print(f"   └── [OK] {task_name} -> {class_name}")
                
            except Exception as e:
                print(f"   └── [FAILED] Could not load '{task_name}': {e}")

    def run(self):
        """Executes the workflow pipeline."""
        print("\n🚀 Starting Workflow Execution...")
        print("="*40)
        
        for module in self.modules:
            try:
                # Execute the module
                module.execute()
                time.sleep(0.5) # Slight delay for visual flow
            except Exception as e:
                print(f"❌ Error during module execution: {e}")
        
        print("="*40)
        print("✨ Workflow completed.\n")
