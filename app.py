from flask import Flask
from flask import render_template,request,redirect, url_for
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
        return self



@app.route("/")
@app.route('/index')
def home():

    now = datetime.now()
    result = Todo.query.all()
    return render_template(
        "test.html",
        entries = result,
        current_user = current_user,
    )

'''@app.route("/add/<name>")
def add_with_name(name):
    todo = Todo(time=datetime.now(), name=name)
    db.session.add(todo)
    db.session.commit()
    return "Success"'''

@app.route("/add/", methods=["POST"])
def add():
    name = request.form['todo']
    todo = Todo(time=datetime.now(), name=name)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/del/<id>")
def delete(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")
