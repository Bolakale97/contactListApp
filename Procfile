release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input


web: gunicorn CONTACTSAPI.wsgi: application

gunicorn --debug my_app:app
