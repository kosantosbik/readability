#!/usr/bin/env python3

from flask import Flask, flash, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
import textract
from words import word_count

UPLOAD_FOLDER = '/home/kosantosbik/projects/readability/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'doc', 'docx'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    file_full_name = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    text = textract.process(file_full_name).decode('utf-8')

    wc = word_count(text)
    word2,word3,word4,word5,word6,wordt = wc.get_numbers()

    os.remove(file_full_name)

    return '''
    <!doctype html>
    <title> Result </title>
    <h1>Result</h1>
    <h3>2 heceli kelime sayisi: {}</h3>
    <h3>3 heceli kelime sayisi: {}</h3>
    <h3>4 heceli kelime sayisi: {}</h3>
    <h3>5 heceli kelime sayisi: {}</h3>
    <h3>6 heceli kelime sayisi: {}</h3>
    <h3>Toplam hece sayisi: {}</h3>

    <h1><a href="/">Process another file</a></h1>
'''.format(word2,word3,word4,word5,word6,wordt)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
