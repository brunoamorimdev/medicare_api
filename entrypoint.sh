#!/bin/sh
cd medicare_api

poetry run python manage.py makemigrations

# Apply database migrations (if needed)
poetry run python manage.py migrate

# Start the Django development server
poetry run python manage.py runserver