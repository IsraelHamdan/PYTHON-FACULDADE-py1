# Implementar uma solução em python que determine se um número é primo ou não
# numeros primos só são divisiveis por 1 e por eles mesmos, onde o resto da divisão tem que ser 0

# minha solução
# # primeiro passo: receber o numero que o usuário digitou
# numero = int(input('Digite um número: '))
#
#
# # segundo passo: criar a função para saber se é ou não primo
# def eh_par(n, numero):
#     if n % 1 == 0 or n % numero == 0:
#         n = numero
#     else :
#         print(f'o {numero} não é primo')
#     return n
# print(f'O {numero} é primo')

# solução do prof (adaptada)
numero = int(input('Insira um número: '))


def eh_primo(n):
    if n < 2:
        return False
    i = n // 2
    while i > 1:
        if n % i == 0:
            return False
        i = i - 1
    return True


resultado = eh_primo(numero)


def imprimir_resultado(numero, resultado):
    mensagem = f'O número {numero} NÃO é primo'
    if resultado:
        mensagem = f'O número {numero} é primo'
    return mensagem


msg = imprimir_resultado(numero, resultado)
print(msg)