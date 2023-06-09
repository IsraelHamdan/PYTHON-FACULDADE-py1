N = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]


def convert(N, notas, moedas):
    r_notas = []
    r_moedas = []

    for nota in notas:
        q = int(N/nota)
        r_notas.append(q)
        N -= q * nota
    for moeda in moedas:
        q = int(round(N, 2) / moeda)
        r_moedas.append(q)
        N -= q * moeda

    return r_notas, r_moedas


r_notas, r_moedas = convert(N, notas, moedas)


def resultado(r_notas, r_moedas):
    print('NOTAS:')
    for i in range(len(notas)):
        print(f'{r_notas[i]} nota(s) de R$ {notas[i]:.2f}')
    print('MOEDAS:')
    for i in range(len(moedas)):
        print(f'{r_moedas[i]} moeda(s) de R$ {moedas[i]:.2f}')


resultado(r_notas, r_moedas)
