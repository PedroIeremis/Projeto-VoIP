#!/bin/bash

cd docker/web
docker build -t nx .
docker run -d --name web -p 8080:80 nx
