#!/bin/bash

cd docker
docker build -t nx .
docker run -d --name web -p 8080:80 nx
