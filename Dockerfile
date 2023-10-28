# Use the official Python image as a parent image
FROM python:3.11.4

# Install dependencies
COPY pyproject.toml .
RUN pip install poetry && poetry install

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /opt/api

# Copy the current directory contents into the container at /app
COPY . .

# Expose port 8000 for the Django development server
EXPOSE 8000

CMD ["entrypoint.sh"]