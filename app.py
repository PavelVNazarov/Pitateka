# Pitateka
# app.py
from flask import Flask, render_template, redirect, url_for, send_from_directory
import json
import os
from flask_frozen import Freezer

app = Flask(__name__)

app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True

freezer = Freezer(app)

def load_texts():
    with open('texts.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# Редирект с корня на index.html
@app.route('/')
def root_redirect():
    return redirect(url_for('home'))

# Главная страница
@app.route('/index.html')
def home():
    texts = load_texts()
    return render_template('index.html', texts=texts['index'])

# Услуги
@app.route('/services.html')
def services():
    texts = load_texts()
    return render_template('services.html', texts=texts['services'])

# Контакты
@app.route('/contacts.html')
def contacts():
    texts = load_texts()
    return render_template('contacts.html', texts=texts['contacts'])

# Обработчик статических файлов
@app.route('/static/<path:filename>')
def static_files(filename):
    # Нормализуем путь для Windows/Linux
    filename = filename.replace('\\', '/')
    return send_from_directory(app.static_folder, filename)


# Генератор URL для статических файлов (для Frozen-Flask)
@freezer.register_generator
def static_files_generator():
    # Получаем список всех файлов в директории static
    static_dir = app.static_folder
    for root, dirs, files in os.walk(static_dir):
        for file in files:
            # Вычисляем относительный путь
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, static_dir)
            # Нормализуем путь для URL
            rel_path = rel_path.replace('\\', '/')
            yield 'static_files', {'filename': rel_path}

if __name__ == '__main__':
    freezer.freeze()

