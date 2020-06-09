from flask import Flask, flash, request, redirect, url_for, jsonify
from flask import send_from_directory
import time, json, requests, os
from werkzeug.utils import secure_filename

from utils.pdfconverter import PdfToCsv

app = Flask(__name__)

UPLOAD_FOLDER = r'C:\Users\vaibhawkumar13\Desktop\balanceApp\uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file  = request.files['file']
        query = request.form['query']
        year  = request.form['year']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
        # Converting the PDF file to CSV and serving the same through /uploads/<filename> API
            PdfToCsv().toCSV(filepath)
            return redirect(url_for('uploaded_file',
                                    filename=filename.replace('pdf','csv')))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <div>
    <p>Please Upload new Balance Sheet and give Query Params</p>
    <form method=post enctype=multipart/form-data style="display: grid; width: 200px">
      <label> Variable Name </label>
      <input type=text name=query>
      <label> Year </label>
      <input typer=number name=year>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </div>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)