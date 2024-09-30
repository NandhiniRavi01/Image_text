from flask import Flask, request, render_template, redirect, url_for
import pytesseract
from PIL import Image
import os

app = Flask(__name__)

# Route for home page to upload an image
@app.route('/')
def home():
    return render_template('upload.html')

# Route to handle image upload and text extraction
@app.route('/extract-text', methods=['POST'])
def extract_text():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file:
        # Save the image file
        image_path = os.path.join('uploads', file.filename)
        file.save(image_path)

        # Perform OCR
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)

        return f"<h2>Extracted Text:</h2><p>{text}</p>"

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
