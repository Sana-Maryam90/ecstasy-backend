#docker file - development version
FROM python:3.11-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /ecstasy-backend

# Install dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Expose the Django port
EXPOSE 8000

# Run Django’s development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 
# Start the development server on port 8000, and listen on all available network interfaces (not just localhost)
#The CMD manage.py is only meant for development purposes and should be changed for a WSGI server.

#----NOTES----
# FROM: Selects the image with the Python version you need.
# WORKDIR: Sets the working directory of the application within the container.
# ENV: Sets the environment variables needed to build the application
# RUN and COPY commands: Install dependencies and copy project files.
# EXPOSE and CMD: Expose the Django server port and define the startup command.