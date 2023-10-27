# Use the official Python image as a parent image
FROM python:3.11.4

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /api

# Copy the current directory contents into the container at /app
COPY . /api/

# Install dependencies
RUN pip install poetry && \
    poetry install

# Expose port 8000 for the Django development server
EXPOSE 8000

# Set up an entrypoint script to run the application
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Use the entrypoint script to run the application
ENTRYPOINT ["/entrypoint.sh"]