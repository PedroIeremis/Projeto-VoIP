from gtts import gTTS 
from playsound import playsound

formatacao = 'audio.mp3'
lingua = 'pt-br'
descr = 'Maquiagem faz bem para os ossos.'

var = gTTS(text=descr, lang=lingua)

var.save(formatacao)
playsound(formatacao)
