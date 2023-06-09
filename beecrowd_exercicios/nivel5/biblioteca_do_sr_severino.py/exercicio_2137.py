while True:
    try:
        N = int(input())
    except EOFError:
        break
    livros = []

    for _ in range(N):
        codigo_livro = input()
        codigo_livro = codigo_livro.zfill(4)

        livros.append(codigo_livro)
        livros.sort()
    print('#################')

    for i in livros:
        print(i)
