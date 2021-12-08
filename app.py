from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/home')
def check_red():
    return redirect('/')

@app.route('/help')
def check_url():
    return redirect(url_for('hello_world'))

@app.route('/about') #code from lecture 2 of backend, not relevant to this weeks homework
def about():
    return render_template('about.html',
                           uni = 'BGU',
                           profile = {'name': 'Ido', 'lastname': 'Polak'},
                           degrees = ['BSc', 'MSc']
                           )

if __name__ == '__main__':
    app.run(debug=True)