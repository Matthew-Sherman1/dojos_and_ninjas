from flask import render_template, request, redirect, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask_app import app


@app.route('/')
def index():
    dojos = Dojo.get_all_dojos()
    return render_template("/index.html",  dojos=dojos)


@app.route('/add/ninja')
def display():
    dojos = Dojo.get_all_dojos()
    return render_template("/ninjas.html", dojos=dojos)
    

@app.route('/dojos')
def get_all_dojos():
    dojos = Dojo.get_all_dojos()
    return redirect('/index.html')


@app.route('/dojo/<int:id>')
def one_dojo(id):
    data = {
        "id": id
    }
    dojo = Dojo.get_one(data)
    return render_template('/dojo.html', dojo=dojo)


# route works, don't chnge
@app.post('/add/dojo')
def create_new_dojo():

    data = {
        'name': request.form['name']
    }
    Dojo.create_new_dojo(request.form)
    print(request.form)
    return redirect('/')


@app.post('/create/ninja')
def create_new_ninja():

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }

    Ninja.create_new_ninja(data)
    return redirect(f'/dojo/{data["dojo_id"]}')


@app.post('/delete')
def delete(id):
    data = {
        'id': id
    }
    Dojo.delete(data)
    return redirect('/index.html')