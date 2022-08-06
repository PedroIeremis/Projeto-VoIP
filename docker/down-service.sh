#!/bin/bash

docker rm -f ns1
docker rm -f web

docker rmi -f img-dns
docker rmi -f nx