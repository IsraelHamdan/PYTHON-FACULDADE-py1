numero = int(input("quantos elementos verificar? "))


def eh_primo(n):
    if n < 2:
        return False
    i = n // 2
    while i > 1:
        if n % i == 0: 
            return False
        i = i - 1
    return True

def imprimir_resultado(numero, resultado):
    mensagem = f'{numero} nao eh primo'
    print(f'o numero é {numero}')
    if resultado:
        mensagem = f'{numero} eh primo'
    return mensagem

lista_input = []

for _ in range(numero): 
    n = int(input())
    lista_input.append(n)

for  n in lista_input:
    resultado =  eh_primo(n)
    msg =  imprimir_resultado(n, resultado)
    print(msg)



