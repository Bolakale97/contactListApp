release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input


web: gunicorn wsgi:CONTACTSAPI

gunicorn --debug CONTACTSAPI:app
