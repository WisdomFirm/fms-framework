# FMS Framework 🏗️

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**The Core Automation Backbone for [WisdomFirm](https://github.com/WisdomFirm).**

**FMS (Flow Management System)** is a modular, config-driven Python framework designed to orchestrate internal workflows, automate administrative tasks, and manage AI agent pipelines. It serves as the foundational "Operating System" for WisdomFirm's automated business logic.

---

## 🚀 Key Features

* **🔌 Modular Architecture:** Plug-and-play design. New capabilities (like AI agents or SEO bots) can be added as isolated modules without touching the core engine.
* **⚙️ Config-Driven:** Fully controlled via `config/settings.yaml`. No hard-coding required to switch tasks on or off.
* **⏱️ Automated TimeSheet:** Built-in module to log runtime sessions and user activity into CSV format automatically.
* **🛡️ Scalable Core:** Lightweight `FMSEngine` designed to handle sequential task execution efficiently.

---

## 📂 Project Structure

```text
fms-framework/
├── config/
│   └── settings.yaml      # Central Configuration
├── core/
│   ├── engine.py          # The Brain (Task Runner)
│   └── base_module.py     # Interface Definition
├── modules/
│   ├── system_monitor.py  # Host Analysis Module
│   └── timesheet.py       # Time Logging Module
├── main.py                # Entry Point
└── requirements.txt       # Dependencies
🛠️ Installation & Usage
1. Prerequisites
Python 3.8 or higher

2. Installation
Clone the repository and install dependencies:

Bash

git clone [https://github.com/WisdomFirm/fms-framework.git](https://github.com/WisdomFirm/fms-framework.git)
cd fms-framework
pip install -r requirements.txt
3. Configuration
Edit config/settings.yaml to define which modules to run:

YAML

app_name: "WisdomFirm FMS Core"
tasks:
  - "system_monitor"
  - "timesheet"
4. Run the Engine
Execute the main script to start the automation pipeline:

Bash

python main.py
📦 Built-in Modules
1. System Monitor (system_monitor)
Analyzes the host infrastructure to ensure the environment is ready for automation tasks.

Checks: OS Version, Processor Architecture, Python Runtime.

2. TimeSheet Logger (timesheet)
Automatically logs the session start time and user identity.

Output: Generates/Updates timesheet_data.csv.

Fields: Timestamp, User, Action, Status.

🔮 Roadmap
[ ] AI Connector Module: Integration with Google Gemini Pro API.

[ ] SEO Auto-Generator: Automated content structure generation.

[ ] Notification Service: Line Notify integration for task completion alerts.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

<p align="center"> Built with ❤️ by <strong>WisdomFirm Team</strong>


<em>Innovating Education & Business through AI Automation.</em> </p>
