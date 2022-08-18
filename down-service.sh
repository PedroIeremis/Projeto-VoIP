#!/bin/bash

docker rm -f web > /dev/null
docker rmi -f nx > /dev/null
docker rmi -f nginx > /dev/null