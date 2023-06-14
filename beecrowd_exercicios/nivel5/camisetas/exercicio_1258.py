impresso = False


def ordena_camisas(N, cor, tamanho, nome):
    for i in range(N - 1):
        for j in range(i + 1, N):
            if (
                cor[i] > cor[j] or cor[i] == cor[j] and tamanho[i] < tamanho[j] or
                cor[i] == cor[j] and tamanho[i] == tamanho[j] and nome[i] > nome[j]
            ):
                cor[i], cor[j] = cor[j], cor[i]
                nome[i], nome[j] = nome[j], nome[i]
                tamanho[i], tamanho[j] = tamanho[j], tamanho[i]


while True:
    N = int(input())
    if N == 0:
        break

    cor = []
    tamanho = []
    nome = []

    for _ in range(N):
        nome.append(input())
        cor_deseordenada, tamanho_desordenado = input().split()
        cor.append(cor_deseordenada)
        tamanho.append(tamanho_desordenado)

    ordena_camisas(N, cor, tamanho, nome)
    if impresso:
        print()
    for i in range(N):
        print(f'{cor[i]} {tamanho[i]} {nome[i]}')

    impresso = True
