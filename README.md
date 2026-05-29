# FinTracker – Personal Finance Tracker

A Django-based personal finance tracker web application that helps users manage transactions, track expenses and income, set financial goals, and monitor savings progress through a dashboard.

## Features

* Add Income and Expense transactions
* Track total income and expenses
* Dashboard with net savings calculation
* Create and manage financial goals
* Goal progress tracking
* Export transactions to Excel file
* User-specific transaction filtering
* Used LoginRequiredMixin to restrict access to authenticated users only
* Clean UI using Django templates
* GitHub version control integration
* Deployment-ready Django project

## Tech Stack

* Python
* Django
* SQLite
* HTML
* CSS
* Bootstrap
* Django Import Export

## Project Structure

finance/
│
├── migrations/
├── templates/
├── views.py
├── models.py
├── forms.py
├── urls.py

## Important Concepts Used

* Django Models
* Class-Based Views (CBV)
* Django Forms
* Model Relationships
* Database Migrations
* Aggregation using Sum()
* LoginRequiredMixin
* Export Functionality
* Static Templates Rendering

## Installation

Clone the repository:

```bash
git clone https://github.com/nikbopche125256/fintracker_project.git
```

Move into the project directory:

```bash
cd fintracker_project
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment (Windows):

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start development server:

```bash
python manage.py runserver
```

## Future Improvements

* PostgreSQL integration
* Docker support
* AWS deployment
* Redis caching
* REST API integration
* Monthly analytics charts

## Learning Outcomes

Through this project, I learned:

* Django project structure
* Database migrations
* Handling model relationships
* Git and GitHub workflow
* Deployment basics
* Debugging migration issues
* Exporting data in Excel format

## Author

Nitin Bopche
