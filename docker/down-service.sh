#!/bin/bash

docker-compose down

docker rm -f web
dokcer rm -f ns1

docker rmi -f docker_web
docker rmi -f docker_dns