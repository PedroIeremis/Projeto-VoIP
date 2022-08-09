from asterisk.agi import *
import os, requests

agi = AGI()
agi.answer()

init = agi.get_data('apresentacao',10000,1)

if init == '1':
    init2 = agi.get_data('opdocker',10000,1)
    if init2 == '1':
        os.system('./up-service.sh')
    elif init2 == '2':
        os.system('./down-docker.sh')
    else:
        agi.stream_file('invalida')
        agi.stream_file('beep')
        agi.hangup()

elif init == '2':
    init3 = agi.get_data('opcep',20000,8)

    subs = "http://viacep.com.br/ws/SUBSTITUIR/json"
    res = subs.replace('SUBSTITUIR', f'{init3}')
    reqs = requests.get(res).content

    with open('x.txt', 'wb') as arq:
        arq.write(reqs)

    os.system('./filtragem.sh')

else:
    agi.stream_file('invalida')
    agi.stream_file('beep')
    agi.hangup()
