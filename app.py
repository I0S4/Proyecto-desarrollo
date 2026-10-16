from flask import Flask, render_template, abort
import json
import os

app = Flask(__name__)

DATA_PATH = os.path.join(app.root_path, 'data', 'restaurants.json')

def load_data():
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    data = load_data()
    return render_template('index.html', restaurants=data['restaurants'])

@app.route('/restaurant/<int:r_id>')
def restaurant(r_id):
    data = load_data()
    for r in data['restaurants']:
        if r['id'] == r_id:
            return render_template('restaurant.html', restaurant=r)
    abort(404)

if __name__ == '__main__':
    app.run(debug=True)
