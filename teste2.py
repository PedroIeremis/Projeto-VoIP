import time
from gtts import gTTS 
from playsound import playsound

formatacao = 'audiocep.mp3'
lingua = 'pt-br'
#descr = 'Este é o conteudo do audio a ser gravado.'
with open('process.txt', 'r') as arq:
    conteudo = arq.read()

var = gTTS(text=conteudo, lang=lingua)

var.save(formatacao)

time.sleep(1)
playsound(formatacao)