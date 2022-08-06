#!/bin/bash

cd dns
docker build -t img-dns .
cd primary
dir=$(pwd)
docker run -d -p 192.168.0.12:53:53/udp -p 192.168.0.12:53:53/tcp --name ns1 --hostname dns-ns1 -v "$dir"/:/etc/bind --dns 192.168.0.12 img-dns

cd ../../web
docker build -t nx .
docker run -d --name web -p 8080:80 nx
