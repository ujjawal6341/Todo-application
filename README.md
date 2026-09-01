# 📝 Todo Application

A simple, lightweight, and responsive **Todo Application** built with **Flask, Python, SQLite, HTML, CSS, and Bootstrap**.

The application helps users manage their daily tasks by allowing them to create, complete, and delete todos through a clean and intuitive interface.

---

## ✨ Features

* ➕ **Add Tasks** — Create new tasks quickly.
* 📋 **View Tasks** — See all your tasks in one place.
* ✅ **Complete Tasks** — Mark tasks as completed.
* 🗑️ **Delete Tasks** — Remove tasks you no longer need.
* 📱 **Responsive UI** — Works across desktop, tablet, and mobile devices.
* ⚡ **Lightweight Backend** — Powered by Flask with minimal dependencies.
* 💾 **SQLite Database** — Simple and reliable local data storage.

---

## 🛠️ Tech Stack

| Technology    | Purpose                  |
| ------------- | ------------------------ |
| **Python**    | Application logic        |
| **Flask**     | Backend web framework    |
| **SQLite**    | Database                 |
| **HTML5**     | Page structure           |
| **CSS3**      | Styling                  |
| **Bootstrap** | Responsive UI components |
| **Jinja2**    | Dynamic HTML templating  |

---

## 📂 Project Structure

```text
Todo-Application/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   └── ...
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── database.db            # SQLite database
├── .gitignore             # Git ignored files
└── README.md              # Project documentation
```

> The exact files inside `static/` and `templates/` may vary depending on your implementation.

---

## 🚀 Getting Started

Follow the steps below to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Todo-Application.git
```

### 2. Navigate to the Project

```bash
cd Todo-Application
```

### 3. Create a Virtual Environment

Using a virtual environment is recommended to keep project dependencies isolated.

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the Application

```bash
python app.py
```

You should see Flask start the development server.

### 6. Open the Application

Visit:

```text
http://127.0.0.1:5000/
```

---

## 📦 Requirements

The project primarily requires Flask.

### `requirements.txt`

```text
Flask
```

SQLite is included with Python through the built-in `sqlite3` module, so **you normally do not need to install SQLite3 separately with pip**.

You can also install Flask manually:

```bash
pip install Flask
```

---

## 🖥️ Application Workflow

The basic workflow is:

```text
User
  │
  ▼
Flask Web Application
  │
  ├── Add Task
  ├── View Tasks
  ├── Complete Task
  └── Delete Task
  │
  ▼
SQLite Database
```

Tasks are stored in the SQLite database and retrieved by the Flask backend when the application is accessed.

---

## 📸 Screenshots

Add screenshots of your application here to make the repository easier to understand.

For example:

```markdown
![Todo Application Dashboard](screenshots/dashboard.png)
```

You could include screenshots showing:

* 📋 Main task dashboard
* ➕ Adding a task
* ✅ Completed tasks
* 📱 Mobile/responsive layout

---

## 🔮 Future Improvements

The application can be extended with several useful features:

### 👤 User Management

* User registration and login
* Secure authentication
* User-specific task lists
* Password management

### 🗂️ Task Organization

* Categories and tags
* Task priorities
* Due dates
* Recurring tasks
* Task sorting

### 🔔 Productivity Features

* Reminders and notifications
* Search functionality
* Filters for completed/pending tasks
* Progress tracking
* Task statistics

### 🎨 UI Improvements

* Dark mode
* Custom themes
* Improved animations
* Drag-and-drop task ordering
* Enhanced mobile experience

### ☁️ Deployment

* Production WSGI server
* Cloud deployment
* PostgreSQL/MySQL support
* Environment-based configuration

---

## 🔐 Security Considerations

If this project is extended beyond local/educational use, consider adding:

* CSRF protection
* Input validation
* Secure authentication
* Password hashing
* Environment variables for secrets
* Proper database migrations
* Production-grade database configuration

---

## 🧪 Development

To run the application during development:

```bash
python app.py
```

For production deployments, avoid using Flask's built-in development server. Use an appropriate WSGI server and configure the application for production.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature/new-feature
```

3. Make your changes.
4. Commit your changes:

```bash
git commit -m "Add new feature"
```

5. Push the branch:

```bash
git push origin feature/new-feature
```

6. Open a Pull Request.

---

## 📄 License

This project is open-source and available for **educational and personal use**.

---

## 👨‍💻 Author

**Your Name**

* GitHub: `https://github.com/your-username`
* LinkedIn: `https://linkedin.com/in/your-profile`

---

## ⭐ Support

If you found this project useful, consider giving the repository a **star ⭐** on GitHub.

---

### Built with ❤️ using Python, Flask, and SQLite.

> A simple project for learning Flask, database integration, CRUD operations, and web application development.
