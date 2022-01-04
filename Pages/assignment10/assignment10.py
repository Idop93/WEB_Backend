from flask import redirect, render_template, request, Blueprint
from  interact_with_db import interact_db

# assignment 10
change_message = ""

assignment10 = Blueprint('assignment10', __name__, static_folder='static', static_url_path='/assignment10', template_folder='templates')

@assignment10.route("/assignment10", methods=['GET', 'POST'])
def assignment10_page():
    global change_message
    change_message = ""
    return render_template('assignment10.html')

@assignment10.route('/insert_user', methods=['POST'])
def insert_user_func():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    query = "INSERT INTO users(name, email, phone) VALUES ('%s', '%s', '%s')" % (name, email, phone)
    interact_db(query=query, query_type='commit')
    global change_message
    change_message = "The user "+name+" is inserted"
    return redirect('/user_list')

@assignment10.route('/update_user', methods=['POST'])
def update_user_func():
    name = request.form['name']
    new_email = request.form['new_email']
    new_phone = request.form['new_phone']
    query = "update users set email = '%s',phone = '%s' where name = '%s'" % (new_email, new_phone, name)
    interact_db(query=query, query_type='commit')
    global change_message
    change_message = "The email and phone of the user "+name+" is updated"
    return redirect('/user_list')

@assignment10.route('/delete_user', methods=['POST'])
def delete_user_func():
    name = request.form['name']
    query = "DELETE FROM users WHERE name='%s'" % name
    interact_db(query, query_type='commit')
    global change_message
    change_message = "The user "+name+" was deleted"
    return redirect('/user_list')

@assignment10.route('/user_list')
def user_list_func():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', user_list=query_result, change_message=change_message)