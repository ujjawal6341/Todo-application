# Todo Application

A simple and lightweight Todo Application built using Flask. It allows users to create, manage, and delete daily tasks through a clean and user-friendly interface.

## Features

* Add new tasks
* View all tasks
* Mark tasks as completed
* Delete tasks
* Simple and responsive interface
* Lightweight Flask-based backend

## Tech Stack

* **Frontend:** HTML, CSS, Bootstrap
* **Backend:** Flask (Python)
* **Database:** SQLite

## Project Structure

```
Todo-Application/
│
├── static/            # CSS, JS and other static files
├── templates/         # HTML templates
├── app.py             # Main Flask application
├── requirements.txt  # Project dependencies
├── database.db       # SQLite database
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/Todo-Application.git
```

2. Move to the project directory:

```bash
cd Todo-Application
```

3. Create and activate a virtual environment (optional):

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Run the Flask application:

```bash
python app.py
```

6. Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## Requirements

```text
Flask
SQLite3
```

Or install Flask directly:

```bash
pip install flask
```

## Future Improvements

* User authentication
* Task categories and priorities
* Due dates and reminders
* Dark mode support
* Search and filter functionality

## License

This project is open-source and available for educational and personal use.

---

**Built with Flask and Python for learning and productivity.**
