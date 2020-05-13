import os
from flask import Flask, flash, redirect, render_template, request, send_file, url_for, send_from_directory
from encryptor import encrypt
from view import View
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = './uploads'
app = Flask(__name__)
view = View()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET'])
def get():
    """Запускается при первом заходе на сервер"""
    return view.render_view()


@app.route('/', methods=['POST'])
def load_information():
    """Обрабатывает информоцию из полей, вычисляет выходной текст. Рендерит страницу"""
    input_format = request.form.get('input_format')
    output_format = request.form.get('output_format')
    view.set_formats(input_format, output_format)
    cipher = request.form.get('cipher')
    mode = request.form.get('mode')
    if input_format == 'file':
        input_text = view.get_input_text()
    else:
        input_text = request.form.get('input_text')
    key = request.form.get('key')
    if input_text is None:
        input_text = ''
    view.set_fields(cipher, mode, input_text, key)
    return view.render_view()


@app.route('/upload_file', methods=['POST'])
def upload_file():
    """Загружает файл, извлекает из него входной текст."""
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    path_to_file = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(path_to_file) as input_file:
        input_text = input_file.read()
    view.set_input_text(input_text)
    return redirect('/')


@app.route('/output_file', methods=['POST'])
def get_output_file():
    """Отображает выходной файл. Переход на другую страницу."""
    with open('output_file.txt', 'w') as output_file:
        output_file.write(view.get_output_text())
    return send_file('output_file.txt')


if __name__ == '__main__':
    app.run(debug=True)
