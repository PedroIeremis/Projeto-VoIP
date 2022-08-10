from gtts import gTTS 
from asterisk.agi import *
import os, requests, time

agi = AGI()
agi.answer()

init = agi.get_data('apresentacao',10000,1)
time.sleep(0.1)

if init == '1':
    init2 = agi.get_data('opdocker',10000,1)

    if init2 == '1':
        agi.stream_file('gerandomale')
        os.system('./up-service.sh')
        agi.stream_file('processofinishmale')
        agi.stream_file('beep')
        agi.hangup()

    elif init2 == '2':
        agi.stream_file('gerandomale')
        os.system('./down-docker.sh')
        agi.stream_file('processofinishmale')
        agi.stream_file('beep')
        agi.hangup()

    else:
        agi.stream_file('invalidamale')
        agi.stream_file('beep')
        agi.hangup()

elif init == '2':
    init3 = agi.get_data('opcep',20000,8)

    subs = "http://viacep.com.br/ws/SUBSTITUIR/json"
    res = subs.replace('SUBSTITUIR', f'{init3}')
    reqs = requests.get(res).content
    agi.stream_file('gerandofemale')

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
        time.sleep(0.1)
        agi.stream_file('audiocep')
        time.sleep(0.2)
        agi.stream_file('processofinishfemale')
        agi.stream_file('beep')
        agi.hangup()
        os.system('rm /usr/share/asterisk/sounds/audio.gsm')

else:
    agi.stream_file('invalidamale')
    agi.stream_file('beep')
    agi.hangup()
