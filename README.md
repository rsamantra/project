# Hello Everyone this the assignment with celery, rabbitmq and django.

1. Clone this repo locally.
2. Make an evironment for this repo.
3. Install third party libraries in requirements.txt - `pip install -r requirements.txt`
4. Then go to manage.py folder and run migrations. - `python manage.py makemigrations` --> `python manage.py migrate`
5. Run the server - `python manage.py runserver`.
6. In duplicate tabs, make the rabbit mq server up. - `rabbitmq-server` and celery worker log - `celery -A django_project worker -l info`.

Thank You.
