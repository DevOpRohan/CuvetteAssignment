from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'
mongo = PyMongo(app)


# Model
class Student:
    def __init__(self, name, university, course):
        self.name = name
        self.university = university
        self.course = course


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        university = request.form['university']
        course = request.form['course']
        student = Student(name=name, university=university, course=course)
        mongo.db.students.insert_one(student.__dict__)
        students = mongo.db.students.find()
        return render_template('index.html', students=students)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
