# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install Tesseract OCR and necessary libraries
RUN apt-get update && apt-get install -y tesseract-ocr libtesseract-dev

# Create upload folder
RUN mkdir -p /app/upload

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed Python packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5006 for Flask
EXPOSE 5006

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=0

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5006"]
