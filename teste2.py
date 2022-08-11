#!/usr/bin/python3
import time, subprocess, requests
from gtts import gTTS 
from playsound import playsound

init3 = input('CEP> ')

subs = "http://viacep.com.br/ws/SUBSTITUIR/json"
res = subs.replace("SUBSTITUIR', f'{init3}")
reqs = requests.get(res).content
subprocess.run(['./filtragem.sh'])

with open('x.txt', 'wb') as arq:
    arq.write(reqs)

with open('process.txt', 'r') as arq:
    conteudo = arq.read()
    formatacao = 'audiocep.mp3'
    lingua = 'pt-br'

    var = gTTS(text=conteudo, lang=lingua)
    var.save(formatacao)

    time.sleep(1)
    playsound(formatacao)