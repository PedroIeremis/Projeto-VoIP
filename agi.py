#!/usr/bin/python3
from operator import sub
from gtts import gTTS
from asterisk.agi import *
import requests, time, subprocess

agi = AGI()
agi.answer()

init = agi.get_data('apresentacao',10000,1)
time.sleep(0.1)

if init == '1':
    init2 = agi.get_data('opdocker',10000,1)

    if init2 == '1':
        agi.stream_file('gerandomale')
        subprocess.run(['/usr/share/asterisk/agi-bin/up-service.sh'])
        agi.verbose()
        agi.wait_for_digit(10000)
        #time.sleep(1)
        agi.stream_file('processofinishmale')
        agi.stream_file('beep')
        agi.hangup()

    elif init2 == '2':
        agi.stream_file('gerandomale')
        subprocess.run(['/usr/share/asterisk/agi-bin/down-service.sh'])
        #time.sleep(1)
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

    with open('/usr/share/asterisk/agi-bin/x.txt', 'wb') as arq:
        arq.write(reqs)
    subprocess.run(['/usr/share/asterisk/agi-bin/filtragem.sh'])

    with open('/usr/share/asterisk/agi-bin/process.txt', 'r') as arq:
        conteudo = arq.read()
        saida = 'audiocep.mp3'
        lingua = 'pt-br'

        var = gTTS(text=conteudo, lang=lingua)
        var.save(saida)
        #time.sleep(0.3)
        subprocess.run(['/usr/share/asterisk/agi-bin/move.sh'])
        #time.sleep(0.3)
        agi.stream_file('audiocep')
        #time.sleep(0.2)
        agi.stream_file('processofinishfemale')
        agi.stream_file('beep')
        agi.hangup()
        subprocess.run(['rm', '/usr/share/asterisk/sounds/audiocep.gsm'])

else:
    agi.stream_file('invalidamale')
    agi.stream_file('beep')
    agi.hangup()
