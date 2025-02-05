# Pitateka
# app.py
from flask import Flask, render_template
import json

app = Flask(__name__)

def load_texts():
    with open('texts.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def home():
    texts = load_texts()
    return render_template('index.html', texts=texts['index'])

@app.route('/services')
def services():
    texts = load_texts()
    return render_template('services.html', texts=texts['services'])

@app.route('/contacts')
def contacts():
    texts = load_texts()
    return render_template('contacts.html', texts=texts['contacts'])

if __name__ == '__main__':
    app.run(debug=True)
