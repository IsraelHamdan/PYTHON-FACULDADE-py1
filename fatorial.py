# implementar uma solução em python que calcule o fatorial de um numero
# N! = N * (N -1 ) !
# 0! = 1 ; 1! = 1
# num = int(input('digite um número: '))

# minha solução 1
# def fatorial(n):
#     n = num
#     if n == 0 or n == 1:
#         print('o fatorial de 0 é 1 e o fatorial de 1 é 1')
#     while n < num * ( num - 1):
#        n * (num - 1)
#     print(n)
#     return n
# ----------------------------------------------------------------------------------------------------------------------------------------------------
# minha solução refatorada
numero = int(input('Insira um número: '))
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n-1)
print(f'o fatorial de {numero} é: {fatorial(numero)}')
