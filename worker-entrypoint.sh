until cd /app/backend
do
    echo "Waiting for server volume..."
done

# run a worker :)
celery -A django_docker worker --loglevel=info --concurrency 1 -E