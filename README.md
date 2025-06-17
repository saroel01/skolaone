# SkolaOne

SkolaOne is a modular school management system that aims to simplify administrative and academic tasks for educational institutions. The project is designed with an **AI-first** philosophy, gradually introducing automation and data-driven decisions as modules mature.

## Modules

- **Akademik** – Manage student registration, grades, schedules, and academic reporting.
- **Asrama** – Handle dormitory assignments, resident monitoring, and facility management.
- **Keuangan** – Track tuition payments, budgeting, and overall school financials.
- **Perpustakaan** – Library catalog management and book lending.
- **HRD** – Staff management including recruitment, attendance, and payroll.
- **Inventori** – Control of supplies, assets, and maintenance records.

## Technology Stack

- **Python 3.10+** for core development
- **Django** web framework
- **PostgreSQL** as the primary database
- **Bootstrap** for responsive UI components
- **Docker** for consistent development and deployment environments

## Setup Instructions

1. Install Python 3.10 or newer.
2. Clone the repository and create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies (once a `requirements.txt` is available):
   ```bash
   pip install -r requirements.txt
   ```
4. Apply database migrations and start the development server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
5. Access the application at `http://localhost:8000`.

## AI First Development Guide

SkolaOne follows an **AI-first** roadmap that evolves through several phases:

1. **Initial Automation** – Implement basic data capture and reporting to replace manual processes.
2. **Insight Phase** – Introduce analytics and dashboards that provide actionable insights for educators and administrators.
3. **Intelligent Assistance** – Gradually add features such as scheduling recommendations, financial predictions, and automated alerts.

The roadmap focuses on building robust, well-tested modules first, then layering AI-driven features as data quality improves. Community feedback shapes priorities along the way.

For a more detailed overview of upcoming milestones, see [docs/roadmap.yaml](docs/roadmap.yaml).
You can also view the roadmap in your browser at `http://localhost:8000/roadmap/` after running the development server.
You can reach the team using the contact form at `http://localhost:8000/contact/`.

---

Contributions, issue reports, and feature requests are welcome. Together we can create a comprehensive, open platform for school management.

## License

This project is licensed under the [MIT License](LICENSE).

