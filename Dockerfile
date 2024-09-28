# Use the official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Create uploads directory
RUN mkdir uploads

# Expose the application port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
