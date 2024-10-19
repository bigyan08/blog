# Blog WebApp
This is a simple blog web application that allows users to create, read, update, and delete blog posts. The application is built using Python Django and SQLite.

## Application Features
The project is divided into two main apps:
1. Blog App: Handles blog-related functionality like creating, viewing, updating, and deleting blog posts.
2. User App: Manages user authentication (registration, login, logout), profiles, and user permissions.

## Technologies Used
1. Backend: Python Django
2. Frontend: css, bootstrap
3. Database: db.sqlite3 (SQLite)
4. Authentication: Django's built-in authentication system

## Installation
1. Clone the repository:

```bash
git clone https://github.com/bigyan08/blog.git
cd blog
```
2. Set up the virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Set up the database.Configure the database settings in the settings.py file (for Django) or the relevant configuration file in your project.

```bash
# Django example (run migrations)
python manage.py migrate

# Run the development server:
python manage.py runserver

```
4. Access the website:
Open your browser and go to http://127.0.0.1:8000

