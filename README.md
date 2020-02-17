# API Books and Authors

It was created in a Docker container with the necessary requirements to manage books and authors.

## Installation

Download the project to the environment:

```
git clone https://github.com/rodrigets/api_books_authors.git
```

Compile the Docker image by running the command below in the same location where the files are found ```Dockerfile``` and ```docker-composer.yml```

```
docker-compose build
```

To start the container, and activate the service run:

```
docker-compose up
```

To import the authors from the csv file, with the container running, execute:

```
docker exec -it apibooksauthors_web_1 python manage.py author_import_csv
```

Api Documentation

```
http://64.225.1.38:8000/swagger

```

