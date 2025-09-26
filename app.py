from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define model
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(2000), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

# Home Route (Add + Show Todos)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('home'))  # Redirect to avoid resubmission on refresh

    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)

# Update Route
@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    if request.method == 'POST':
        todo.title = request.form['title']
        todo.desc = request.form['desc']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('update.html', todo=todo)

# Delete Route
@app.route('/delete/<int:sno>')
def delete(sno):
    todo_to_delete = Todo.query.filter_by(sno=sno).first()
    if todo_to_delete:
        db.session.delete(todo_to_delete)
        db.session.commit()
    return redirect(url_for('home'))

# Run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if not exist
    app.run(debug=True, port=8000)
