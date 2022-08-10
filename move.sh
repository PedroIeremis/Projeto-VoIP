#!/bin/bash

sox audiocep.mp3 -r8000 -c1 audiocep.gsm
rm audiocep.mp3
mv audiocep.gsm /usr/share/asterisk/sounds/