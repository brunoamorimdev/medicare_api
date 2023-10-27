#!/bin/sh

# Apply database migrations (if needed)
poetry run python manage.py migrate

# Start the Django development server
poetry run python manage.py runserver 0.0.0.0:8000