# exercicio 1199
def conversor_de_numero():
    # enquanto for verdade faça
    while True:
        # recebe do usuário a entrada
        numero_para_ser_convertido = input()
        # se o elemento for negativo o programa é interrompido
        if '-' in numero_para_ser_convertido:
            print('Não pode haver elementos negativos')
            break
        # ===========================================================
        # converte de hexadecimal para decimal
            # o elemento '0x' está dentro da nossa entrada? se sim execute esse código
        elif '0x' in numero_para_ser_convertido:
            numero_convertido = int(numero_para_ser_convertido, 16)
            print(numero_convertido)
        # converte de decimal para hexadecimal
        # ==================================================================
        # se nenhuma das alternativas anteriores foi atendida, converta de decimal para hexadecimal
        else:
            numero_convertido = hex(int(numero_para_ser_convertido))
            # mostra o resultado convertido em hexadecimal, sendo que tudo que vem antes do segundo elemento é maiusculo
            # e tudo que vem ANTES do segundo elemento é minusculo
            print(numero_convertido[:2] + numero_convertido[2:].upper())


conversor_de_numero()
