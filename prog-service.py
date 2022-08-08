import requests
cep = input('Digite CEP para busca> ')

subs = "http://viacep.com.br/ws/SUBSTITUIR/json"
res = subs.replace('SUBSTITUIR', f'{cep}')
#res = "http://viacep.com.br/ws/59052800/json"
#print(res)
reqs = requests.get(res).content

with open('x.txt', 'wb') as arq:
    arq.write(reqs)