from flask import Flask
from flask import render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, nullable=False)
    name = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Todo %r>' % self.name

@app.route("/")
def home():

    now = datetime.now()
    result = Todo.query.all()
    return "Success"

@app.route("/add/<name>")
def add(name):
    todo = Todo(time=datetime.now(), name=name)
    db.session.add(todo)
    db.session.commit()
    return "Success"
