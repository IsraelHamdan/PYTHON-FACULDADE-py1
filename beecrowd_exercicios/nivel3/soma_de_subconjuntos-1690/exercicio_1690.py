cases = int(input())

def menor_valor(a):
    if 1 in a:
        s = 1
        a.sort()

        for i in a:
            if i > s:
                break
            s += i
        print(s)
    else:
        print('1')

def entrada(cases, menor_valor):
    for _ in range(cases):
        n = int(input())
        a = list(map(int, input().split()))

        menor_valor(a)

entrada(cases, menor_valor)

# SOLUÇÃO ACEITA 
