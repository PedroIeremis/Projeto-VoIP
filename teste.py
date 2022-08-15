#!/usr/bin/python3
from gtts import gTTS
from asterisk.agi import *
import requests, time, os

os.system('./up-service.sh')

init3 = input('CEP> ')

subs = "http://viacep.com.br/ws/SUBSTITUIR/json"
res = subs.replace('SUBSTITUIR', f'{init3}')
reqs = requests.get(res).content
#agi.stream_file('gerandofemale')

with open('x.txt', 'wb') as arq:
    arq.write(reqs)
os.system('./filtragem.sh')

with open('process.txt', 'r') as arq:
    conteudo = arq.read()
    saida = 'audiocep.mp3'
    lingua = 'pt-br'

    var = gTTS(text=conteudo, lang=lingua)
    var.save(saida)
    time.sleep(0.3)
    os.system('./move.sh')
    time.sleep(0.3)
    #agi.stream_file('audiocep')
    time.sleep(0.2)
    #agi.stream_file('processofinishfemale')
    #agi.stream_file('beep')
    #agi.hangup()
    os.system('rm /usr/share/asterisk/sounds/audio.gsm')