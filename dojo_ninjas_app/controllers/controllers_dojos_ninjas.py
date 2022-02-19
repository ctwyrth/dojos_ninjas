from dojo_ninjas_app import app
from dojo_ninjas_app.models.dojos_ninjas import Dojo
from flask import render_template, redirect, request, session

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    new_dojo = {
        "name": request.form['name'],
        "location": request.form['location']
    }
    id = Dojo.save(new_dojo)
    return redirect('/show/' + str(id))

@app.route('/show')
def show_all():
    dojos = Dojo.all()
    return render_template('/results.html', dojos = dojos)

@app.route('/show/<int:id>')
def show_record(id):
    dojo_id = {
        'id': id
    }
    dojo = Dojo.show(dojo_id)
    print(dojo)
    return render_template("/details.html", dojo = dojo)

# @app.route('/edit/<int:id>')
# def edit(id):
#     dojo_id = {
#         'id': id
#     }
#     return render_template("edit.html", dojo = Dojo.show(dojo_id))

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    dojo = {
        "id": id,
        "name":request.form['name'],
        "location": request.form['location'],
    }
    Dojo.update(dojo)
    return redirect(f"/show/{id}")

@app.route('/delete/<int:id>') 
def delete(id):
    dojo_id = {
        'id': id
    }
    Dojo.delete(dojo_id)
    return redirect('/show')

@app.route('/dojo/students/<int:id>')
def ninjas(id):
    dojo_id = {
        "id": id
    }
    students = Dojo.get_students(dojo_id)
    dojo = Dojo.show(dojo_id)
    return render_template('/students.html', students = students, dojo = dojo)

@app.route('/new_ninja/<int:id>')
def add_ninja(id):
    dojo_id = {
        "id": id
    }
    return render_template("/add.html", dojo_id = dojo_id)

@app.route('/new_ninja', methods=["POST"])
def create_ninja():
    new_ninja = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "age": request.form['age'],
        "dojo_id": request.form['dojo_id']
    }
    print(new_ninja)
    test = Dojo.create_ninja(new_ninja)
    print(test)
    return redirect('/show')