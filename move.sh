#!/bin/bash

sox /usr/share/asterisk/agi-bin/audiocep.mp3 -r8000 -c1 /usr/share/asterisk/agi-bin/audiocep.gsm
rm /usr/share/asterisk/agi-bin/audiocep.mp3
mv /usr/share/asterisk/agi-bin/audiocep.gsm /usr/share/asterisk/sounds/