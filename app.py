import os
import time
import threading
from conv_service import convert_file, delayed_delete
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

temp_dir = 'temp'
os.makedirs(temp_dir, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    uploaded_file = request.files['file']
    selected_format = request.form.get('format')
    
    if uploaded_file and uploaded_file.filename != '':
        temp_path = os.path.join(temp_dir, uploaded_file.filename)
        uploaded_file.save(temp_path)

        output_filename = os.path.splitext(uploaded_file.filename)[0] + '.' + selected_format
        output_path = os.path.join(temp_dir, output_filename)

        try:
            convert_file(selected_format, temp_path, output_path)
        except Exception as e:
            return "An error occurred during file processing.", 500

        response = send_file(output_path, as_attachment=True)
        delayed_delete(temp_path)
        delayed_delete(output_path)
        return response

    return 'No file uploaded', 400

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')