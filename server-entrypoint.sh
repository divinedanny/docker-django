until cd /app
do
    echo "Connection to Volume....."
done


until python manage.py migrate
do
    echo "Conntecting to database....."
    sleep 2
done


python manage.py collectstatic --noinput

# python manage.py createsuperuser --noinput

gunicorn django_docker.wsgi:application --bind 0.0.0.0:8000 --workers 4 --threads 4

# for debug
#python manage.py runserver 0.0.0.0:8000