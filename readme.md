# Django Location API

A RESTful API built with Django and Django REST Framework for managing location data.

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Usage](#usage)
5. [API Endpoints](#api-endpoints)
6. [Contributing](#contributing)
7. [License](#license)

---

## Features

- **CRUD Operations**: Create, retrieve, update, and delete location records.
- **Soft Deletion**: Locations are soft-deleted by default (using a `deleted_at` field).
- **UUID for Communication**: Securely expose locations using UUIDs instead of internal identifiers.
- **Custom Management Command**: Import JSON data into the database using a custom command (`initial_setup`).
- **Environment Variables**: Secure handling of sensitive credentials using `.env` files.
- **Organized Settings**: Modular settings for development and production environments.

---

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (optional but recommended)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Rahul93/assignment.git
   cd assignment
2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate 
    
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

4. **Create a .env File**
   ```bash
   SECRET_KEY=your_secret_key_here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE_URL=sqlite:///db.sqlite3

5. **Run Migrations**
   ```bash
    python manage.py makemigrations
    python manage.py migrate

6. **Import initial data**
   ```bash
    python manage.py initial_setup

7. **Start dev server**
   ```bash
    python manage.py runserver

# The API will now be accessible at
`http://127.0.0.1:8000/api/locations/`

## Configuration

### Environment Variables
Sensitive information is stored in a `.env` file. Update the following variables as needed:

- **SECRET_KEY**: A secret key for Django's security mechanisms.
- **DEBUG**: Set to `True` for development, `False` for production.
- **ALLOWED_HOSTS**: Comma-separated list of allowed hostnames (e.g., `localhost,127.0.0.1`).
- **DATABASE_URL**: Database connection string (default is SQLite).

### Settings Structure
Settings are split into multiple files for better organization:

- `base.py`: Common settings shared across environments.
- `development.py`: Settings specific to the development environment.
- `production.py`: Settings specific to the production environment.

To switch between environments, set the `DJANGO_ENV` variable in your `.env` file:

```env
DJANGO_ENV=development
