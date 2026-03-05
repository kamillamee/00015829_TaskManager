#!/bin/bash
set -e
echo "Running database migrations..."
python manage.py migrate --noinput
echo "Collecting static files..."
python manage.py collectstatic --noinput
chown -R appuser:appuser /app/staticfiles /app/media 2>/dev/null || true
exec runuser -u appuser -- "$@"
