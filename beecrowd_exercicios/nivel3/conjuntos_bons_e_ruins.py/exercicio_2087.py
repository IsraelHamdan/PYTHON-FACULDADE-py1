while True:
    N = int(input())
    if N == 0:
        break
    
    conjunto_de_palavras = []
    for _ in range(N):
        conjunto_de_palavras.append(input())
        
    conjunto_de_palavras.sort()
    conjunto_ruim = False
    
    for i in range(N-1):
        if conjunto_de_palavras[i+1].startswith(conjunto_de_palavras[i]):
            conjunto_ruim = True
            break
        
    if conjunto_ruim:
        print('Conjunto Ruim')
    else:
        print('Conjunto Bom')