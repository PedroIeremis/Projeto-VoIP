#!/bin/bash

/usr/bin/docker build -t nx .
/usr/bin/docker run -d --name web -p 8080:80 nx
