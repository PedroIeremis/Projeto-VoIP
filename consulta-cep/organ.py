with open('x.txt', 'r') as arq:
    ler = arq.read()
    res = ler.strip('}').strip('{').split(':')
    for i in res:
        print(i,end='')
    print(res)