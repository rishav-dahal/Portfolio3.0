# Portfolio Project

This is a personal portfolio project built using **Django** (backend) and **React** (frontend).

## Features

- Showcases personal projects and achievements
- Modern, responsive UI
- RESTful API with Django
- Interactive frontend with React
- **Blog section** managed exclusively via Django admin

## Tech Stack

- **Backend:** Django, Django REST Framework
- **Frontend:** React, JavaScript, HTML, CSS
- **Database:** SQLite (default), easily switchable to PostgreSQL

## Getting Started

1. **Clone the repository:**
    ```bash
    git clone <repo-url>
    cd portfolio
    ```

2. **Backend setup:**
    ```bash
    cd backend
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
    ```

3. **Frontend setup:**
    ```bash
    cd frontend
    npm install
    npm start
    ```

## Blog Management

The blog section is accessible and manageable only through the Django admin interface. Only authorized admin users can create, edit, or delete blog posts.

## License

This project is licensed under the MIT License.

---
Feel free to customize this README for your specific needs!