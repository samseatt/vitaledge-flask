# Use the official Python image as the base
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Define the environment variables
ENV FLASK_APP=app/main.py
ENV FLASK_ENV=production

# Start the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
