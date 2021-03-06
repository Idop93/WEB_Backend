from flask import Flask, redirect, url_for, render_template, request, session, Blueprint
from interact_with_db import interact_db, query_json
from Pages.assignment10.assignment10 import assignment10
import requests
import json

app = Flask(__name__)
app.register_blueprint(assignment10)
app.secret_key = '123'

# Home page
@app.route('/ido')
@app.route('/')
def main_func():  # put application's code here
    # TODO
    return redirect(url_for('home_func'))


@app.route('/Home')
def home_func():
    return render_template('welcome.html')


# About me page
@app.route('/About_me')
def about_func():
    return render_template('CV.html')


# Hobbies page
@app.route('/hobbies')
def hobbies_func():
    return render_template('assignment8.html',
                           hobbies=['Soccer', 'Football', 'Running', 'Playing drums', 'hiking', '', 'diving'])


# Contact page
@app.route('/contact')
def contact_func():
    if 'y_name' in request.args:
        name = request.args['y_name']
        email = request.args['y_email']
        password = request.args['y_password']
        return render_template('contact.html', user_name=name, user_email=email, user_password=password)
    return render_template('contact.html')


users = {'user1': {'name': 'Yossi', 'email': 'yo@gmail.com', 'phone': '0526783234'},
         'user2': {'name': 'Ido', 'email': 'Ido@gmail.com', 'phone': '0542436586'},
         'user3': {'name': 'Lior', 'email': 'lior@hotmail.com', 'phone': '0507384522'},
         'user4': {'name': 'Noam', 'email': 'noam@yahoo.com', 'phone': '0521435647'},
         'user5': {'name': 'ofir', 'email': 'ofir@mail.com', 'phone': '0548793482'},
         'user6': {'name': 'ofer', 'email': 'ofer@gmail.com', 'phone': '0507683213'}
         }


@app.route("/assignment9", methods=['GET', 'POST'])
def assignment9_page():
    # search form
    if 'email' in request.args:
        email = request.args['email']
        if email == '':
            return render_template('assignment9.html', user_list=users)
        # search it in users dict
        for key, value in users.items():
            if value.get('email') == email:
                return render_template('assignment9.html', u_name=value.get('name'), u_email=value.get('email'))
    # registration form
    if request.method == "POST":
        session['username'] = request.form['username']
    return render_template('assignment9.html')


@app.route("/logout", methods=['GET', 'POST'])
def logout_func():
    session['username'] = ''
    return render_template('assignment9.html')


@app.route('/req_frontend')
def req_frontend_func():
    return render_template('req_frontend.html')


from Pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

@app.route('/assignment11/users', methods=['GET'])
def get_users():
    if request.method == 'GET':
        query = "select * from users"
        query_result = query_json(query=query)
        return json.dumps(query_result)

@app.route("/assignment11/outer_source", methods=['GET'])
def os_page():
    if 'number' in request.args:
        number = request.args['number']
        res = requests.get(url=f"https://reqres.in/api/users/{number}")
        res = res.json()
        return render_template('assignment11-outer_source.html', user=res['data'])
    return render_template('assignment11-outer_source.html')

@app.route('/assignment12/restapi_users', defaults={'user_id': 1})
@app.route("/assignment12/restapi_users/<int:user_id>")
def assignment12(user_id):
    query = 'select * from users where id=%s' % user_id
    query_result = query_json(query=query)
    if len(query_result) == 0:
        query_result = [{'status': 'unsuccessful', 'message': 'user not found, please try a different user'}]
    return json.dumps(query_result)

if __name__ == '__main__':
    app.run(debug=True)
