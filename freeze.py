# freeze.py
from app import freezer
import os
import shutil
import warnings
from flask_frozen import MimetypeMismatchWarning

# Игнорировать предупреждения о MIME-типах
warnings.filterwarnings("ignore", category=MimetypeMismatchWarning)

if __name__ == '__main__':
    # Удаляем старую папку docs
    if os.path.exists('docs'):
        shutil.rmtree('docs')

    # Генерируем статические страницы
    freezer.freeze()

    # Копируем статические файлы
    if os.path.exists('static'):
        shutil.copytree('static', 'docs/static', dirs_exist_ok=True)

    print("Статический сайт успешно сгенерирован в папке docs!")
