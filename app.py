from flask import Flask, redirect, url_for,render_template
from flask import request
from flask import session
from  interact_with_db import interact_db
from datetime import date

app = Flask(__name__)
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
                           hobbies = ['Soccer','Football','Running','Playing drums','hiking','','diving'])

# Contact page
@app.route('/contact')
def contact_func():
    if 'y_name' in request.args:
          name = request.args['y_name']
          email = request.args['y_email']
          password = request.args['y_password']
          return render_template('contact.html', user_name = name,user_email = email,user_password = password)
    return render_template('contact.html')

users = {'user1': {'name': 'Yossi', 'email': 'yo@gmail.com'},
         'user2': {'name': 'Ido', 'email': 'Ido@gmail.com'},
         'user3': {'name': 'Lior', 'email': 'lior@hotmail.com'},
         'user4': {'name': 'Noam', 'email': 'noam@yahoo.com'},
         'user5': {'name': 'ofir', 'email': 'ofir@mail.com'},
         'user6': {'name': 'ofer', 'email': 'ofer@gmail.com'}
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

#
# @app.route('/users')
# def users_func():
#     query = "select * from users"
#     query_result = interact_db(query=query, query_type='fetch')
#     return render_template('users.html', users=query_result)
#
# @app.route('/insert_user', methods = ['post'])
# def insert_user_func():
#     name = request.form['name']
#     email = request.form['email']
#     password = request.form['password']
#
#     query = "insert into users(name, email, password) values ('%s', '%s', '%s')" % (name, email, password)
#     interact_db(query=query, query_type='commit')
#     return redirect('/users')
#
# @app.route('/delete_user')
# def delete_user_func():
#     user_id = request.form['id']
#     query = "delete from users where id='%s';" % user_id
#     interact_db(query, query_type='commit')
#     return redirect('/users')

# @app.route('/login', method = [ 'get', 'post' ])
# def login_func():
#     if request.method =='get':
#         return render_template('login.html')
#     if request.access_control_request_method == 'post':
#         #DB
#         username = request.form['username']
#         password = request.form['password']
#         session['username'] = username
#         return render_template('login.html', username= username)

if __name__ == '__main__':
    app.run(debug=True)