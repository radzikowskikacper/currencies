# Currency RSS

## Architecture

Everything is executed using Docker Containers.

There are separate containers (docker-compose.yml) for:
- backend
- PostgreSQL
- Redis
- Celery
- Celery-beat

The RSS feeds with currencies are read as [scheduled tasks](prices/tasks.py).

For the sake of demonstration, the interval is 10 seconds.

### Database
The database consists of [one table](prices/models.py) for the prices.

## Execute tests
~~~~
$ docker-compose -f docker-compose-test.yml -f docker-compose.yml up tests
~~~~

## Start the service
~~~~
$ docker-compose up
~~~~
Access to the prices endpoint at e.g:
~~~~
http://localhost:8000/prices/
~~~~
~~~~
http://localhost:8000/prices/USD/
~~~~
~~~~
http://localhost:8000/prices/PLN/2020-02-06T13:15:00Z/
~~~~
