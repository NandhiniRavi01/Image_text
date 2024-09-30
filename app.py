from flask import Flask, request, redirect, url_for, render_template, send_from_directory
import os
from werkzeug.utils import secure_filename
import pytesseract
from PIL import Image

app = Flask(__name__)
UPLOAD_FOLDER = '/app/upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Route to display upload form
@app.route('/')
def upload_form():
    return '''
    <html>
    <body>
        <h1>Upload an Image</h1>
        <form method="POST" enctype="multipart/form-data" action="/upload">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
    </body>
    </html>
    '''

# Route to handle image upload and text extraction
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = secure_filename(file.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Save the image to the uploads folder
        file.save(image_path)

        # Extract text from the image using pytesseract
        extracted_text = pytesseract.image_to_string(Image.open(image_path))

        # Save the extracted text into a .txt file in the uploads folder
        text_filename = os.path.splitext(filename)[0] + '.txt'
        text_path = os.path.join(app.config['UPLOAD_FOLDER'], text_filename)
        with open(text_path, 'w') as text_file:
            text_file.write(extracted_text)

        # Return the contents of the text file to the user
        return f"<h2>Extracted Text:</h2><pre>{extracted_text}</pre>"

# Route to download the extracted text file
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(host='0.0.0.0', port=5006)
