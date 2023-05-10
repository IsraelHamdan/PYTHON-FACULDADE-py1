# chat gpt
while True:
    # leitura dos dados de entrada
    a, b = map(int, input().split())
    if a == b == 0:  # fim da entrada
        break
    alice = set(map(int, input().split()))
    beatriz = set(map(int, input().split()))

    # cálculo do número máximo de cartas que podem ser trocadas
    intersecao = alice.intersection(beatriz)
    troca_maxima = min(len(alice) - len(intersecao), len(beatriz) - len(intersecao))

    # impressão do resultado
    print(troca_maxima)
