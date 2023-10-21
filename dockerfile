# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the Django project directory into the container
COPY ./api /app

# Expose the port your Django app will run on
EXPOSE 8090


# Install dependencies from requirements.txt
RUN pip install -r /app/requirements.txt

# Define the command to start your Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8090"]

