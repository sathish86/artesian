

Useful commands:

docker-compose run --service-ports web coverage run --source="." manage.py test

# to generate coverage report in html
docker-compose run --service-ports web coverage html