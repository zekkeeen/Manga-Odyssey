# Manga Odyssey - CRUD Manga Library App

## About
Manga Odyssey is a web application designed for manga enthusiasts who want to create and manage their own digital manga library. Whether you're an avid reader or a collector, this app provides an intuitive platform to organize, track, and update your favorite manga titles. Built with Django for a robust backend and styled with CSS, Manga Odyssey offers seamless CRUD functionality to enhance the manga cataloging experience.

## Description
Manga Odyssey is a CRUD (Create, Read, Update, Delete) web application built using Django for the backend and CSS for the frontend. It serves as a digital manga library where users can manage a collection of manga, including adding new titles, viewing details, updating information, and deleting records.

## Features
- **Create**: Add new manga titles with details like title, author, genre, release date, and description.
- **Read**: View a list of all manga and detailed pages for each title.
- **Update**: Edit existing manga details.
- **Delete**: Remove manga from the collection.
- **Search Functionality**: Find manga by title or genre.
- **User Authentication** (Optional): Restrict access to certain features based on user roles.

## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: CSS (for styling)
- **Database**: Django Models (SQLite/PostgreSQL/MySQL)

## Installation
### Prerequisites
- Python (>=3.8 recommended)
- Django (>=4.0 recommended)
- Virtual Environment (optional but recommended)

### Setup Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/manga-odyssey.git
   cd manga-odyssey
   ```
2. **Create a Virtual Environment** (optional but recommended)
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```
5. **Create a Superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
7. Open your browser and visit `http://127.0.0.1:8000/` to access the app.

## Project Structure
```
manga-odyssey/
│── manga_app/         # Django app for manga management
│   ├── migrations/    # Database migrations
│   ├── templates/     # HTML templates
│   ├── static/        # CSS and static files
│   ├── views.py       # Handles CRUD logic
│   ├── models.py      # Database models
│   ├── urls.py        # URL routing
│── manga_odyssey/     # Project settings and configurations
│── db.sqlite3         # Default database (if using SQLite)
│── manage.py          # Django CLI tool
│── requirements.txt   # Dependencies
```

## Usage
- Navigate to `http://127.0.0.1:8000/` to view the manga library.
- Use the admin panel (`http://127.0.0.1:8000/admin/`) to manage manga records if needed.
- Perform CRUD operations through the UI.

## Future Enhancements
- Implement user authentication and authorization.
- Improve UI with better styling.
- Add API support for external integrations.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries, reach out to **ebenezernolimit@gmail.com**.

