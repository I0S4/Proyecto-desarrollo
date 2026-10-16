from flask import Flask, render_template, abort, redirect, url_for, request, session, flash
import json
import os
from functools import wraps

app = Flask(__name__)
# Secret key for sessions (for demo purposes). In production use a secure random value from env.
app.secret_key = 'change-this-to-a-secure-random-key'

DATA_PATH = os.path.join(app.root_path, 'data', 'restaurants.json')

# Simple, hard-coded credential for the demo as requested
DEMO_USERNAME = 'xyz'
DEMO_PASSWORD = '123'


def load_data():
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if not session.get('user'):
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return wrapped_view


@app.route('/')
def root():
    # redirect to login page
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        if username == DEMO_USERNAME and password == DEMO_PASSWORD:
            session['user'] = username
            flash('Inicio de sesión correcto', 'success')
            return redirect(url_for('index'))
        else:
            flash('Usuario o contraseña incorrectos', 'error')
            return render_template('login.html')

    # GET
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Sesión cerrada', 'info')
    return redirect(url_for('login'))


@app.route('/home')
@login_required
def index():
    data = load_data()
    return render_template('index.html', restaurants=data['restaurants'])


@app.route('/restaurant/<int:r_id>')
@login_required
def restaurant(r_id):
    data = load_data()
    for r in data['restaurants']:
        if r['id'] == r_id:
            return render_template('restaurant.html', restaurant=r)
    abort(404)


# Convenience: allow /index to work
@app.route('/index')
def index_alias():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
