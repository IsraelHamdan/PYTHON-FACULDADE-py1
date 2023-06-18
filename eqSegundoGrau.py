import cmath

a = int(input('Insira o coeficiente a: '))
b = int(input('Insira o coeficiente b: '))
c = int(input('Insira o coeficiente c: '))

delta = lambda a, b, c: (b**2) - 4*a*c
d = delta(a, b, c)


def raw(a,b, c, d):
    raiz = ""
    if d > 0:
        x1 = (-b + cmath.sqrt(d)/ (2*a))
        x2 = (-b - cmath.sqrt(d)/ (2*a))
        raiz = f'A equação {a}x² + {b}x + {c} possui raizes reais: x1 = {round(x1, 2)},x2 = {round(x2, 2)}'
    elif d == 0:
        x = -b / (2*a)
        raiz = f'A equação {a}x² + {b}x + {c} possui apenas uma raiz real: x = + ou - {round(x, 2)}'
    else:
        raiz = f'A equação {a}x² + {b}x + {c} NÃO possui raizes no conjunto dos reais, apenas nos complexos'
    print(raiz)
raw(a,b, c, d)
