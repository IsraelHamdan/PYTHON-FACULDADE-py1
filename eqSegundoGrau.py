import cmath

def vars():
    a = int(input('insira o coeficiente a: '))
    b = int(input('insira o coeficiente b: '))
    c = int(input('insira o coeficiente c: '))
    return a,b,c

a, b, c = vars()

def delta(a, b, c):
    delta = (b**2)-4*a*c
    return delta

d = delta(a, b, c)


def raw(a, b, c, d):
    if d > 0:
        x1 = -b + cmath.sqrt(d) / (2*a)
        x2 = -b - cmath.sqrt(d) / (2*a)
        raw = f'a equação {a}x² + {b}x + {c} possui raizes x1 = {x1} e x2 = {x2}'
        print(raw)
    elif d == 0:
        x = -b / (2*a)
        raw = f'a equação {a}x² + {b}x + {c} possui raiz x = + ou - {x}' 
        print(raw)
    else:
        raw = f'a equação {a}x² + {b}x + {c} NÃO possui raiz no conjunto dos reais pois o determinante da equação é: {d}, essa equação possui raizes no conjunto dos complexos'
        print(raw)
    # return x1, x2
raw(a, b, c, d)







