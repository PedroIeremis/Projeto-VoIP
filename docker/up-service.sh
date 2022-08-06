#!/bin/bash

cd web
docker build -t nx .
docker run -d --name web -p 8080:80 nx
