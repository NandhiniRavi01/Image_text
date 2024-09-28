# Use the official Python image
FROM python:3.10-slim

# Set environment variable
ENV PYTHONUNBUFFERED=1
ENV FLASK_ENV=production

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install curl for healthcheck
RUN apt-get update && apt-get install -y curl && apt-get clean

# Copy the rest of the application code
COPY . .

# Create uploads directory
RUN mkdir -p /app/upload && chmod -R 777 /app/upload


# Expose the application port
EXPOSE 5000

# Health check to ensure the application is running
HEALTHCHECK --interval=30s --timeout=5s CMD curl -f http://localhost:5000/ || exit 1

# Add a non-root user and switch to it
RUN useradd -m flaskuser
USER flaskuser

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
