# exercicio 1019
# a entrada contem um valor inteiro N que são os segundos
# a saida mostra o tempo em horas:minutos:segundos

def conversor():
    sec = int(input())
    seg = 60
    hr = sec // (seg**2)
    sec = sec % (seg**2)

    min = sec // seg
    sec = sec % seg

    print(f'{hr}:{min}:{sec}')


conversor()
