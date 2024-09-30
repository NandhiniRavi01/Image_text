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
        <h1>Upload an Image that you want to convert it to text</h1>
        <form method="POST" enctype="multipart/form-data" action="/upload">
            <input type="file" name="file">
            <input type="upload the image" value="Extract to text">
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
        text_path = os.path.join(app.con
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Clean Up Old Containers)
[Pipeline] script
[Pipeline] {
[Pipeline] sh
+ docker stop flask-ocr-app
flask-ocr-app
+ docker rm flask-ocr-app
flask-ocr-app
[Pipeline] }
[Pipeline] // script
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Run Docker Container)
[Pipeline] script
[Pipeline] {
[Pipeline] sh
+ docker run -d -p 5006:5006 --name flask-ocr-app flask-ocr-app:latest
cad20de286354cd4cc18eecb3fa4c7cb395bb11bbd882c798eb9f987ea466484
[Pipeline] }
[Pipeline] // script
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Post-deployment)fig['UPLOAD_FOLDER'], text_filename)
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
