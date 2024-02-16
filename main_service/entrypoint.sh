python3 manage.py migrate --no-input

echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@myproject.com', 'admin')" | python manage.py shell

exec "$@"

pytest .
gunicorn main_service.wsgi:application --bind 0.0.0.0:8000 --workers 4
