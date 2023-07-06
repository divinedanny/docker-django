#Use the python version to run the image
FROM python:3.9.16-alphine3.17

#setting the python environment variables
ENV PYTHONUNBUFFER 1

# copying the requirements(dependencies) to your container
COPY ./requirements.txt ./requirements.txt

#install the requiremets(dependencies) with no cache in your registry
RUN pip install --update --no-cache -r /requirements.txt

# install gcc to be
RUN apk add --update --no-cache --virtual .tmp-build-deps \ 
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

# make an app directory in your container
RUN mkdir /app

#copy from the root directory to yoru app directory
COPY . ./app

#make your working dirctory to now be the app directory
WORKDIR /app

RUN chmod +x /app/server-entrypoint.sh
RUN chmod +x /app/worker-entrypoint.sh

#running the gunicorn to run your wsgi server application to bind it to any ip address
CMD gunicorn docker_django.wsgi:application --bind 0.0.0.0:8008 --worker 4 --threads 4

#expose your port number
EXPOSE 8008



