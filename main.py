from core.engine import FMSEngine

def main():
    # 1. Initialize the FMS Engine
    app = FMSEngine()
    
    # 2. Load configured modules
    app.load_modules()
    
    # 3. Execute the pipeline
    app.run()

if __name__ == "__main__":
    main()
