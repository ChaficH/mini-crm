# Mini CRM

A small Django app for managing contacts and companies.

## Setup

Create and activate a virtual environment:

    python -m venv venv
    source venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

Run migrations:

    python manage.py migrate

Start the server:

    python manage.py runserver

Open http://127.0.0.1:8000/contacts/

## Admin

Create an admin account:

    python manage.py createsuperuser

The admin panel is available at http://127.0.0.1:8000/admin/
