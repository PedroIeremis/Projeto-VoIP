#!/bin/bash

/usr/bin/docker build -t nx /usr/share/asterisk/agi-bin/docker
/usr/bin/docker run -d --name web -p 8080:80 nx
