# idade em dias (exericicio 1020)
# Dado o tempo em dias converta ele para o formato: anos, meses, dias 

dias = int(input())

def conv(dias): 
     
    anos =  dias // 365 
    dias = dias % 365
 
    meses = dias // 30
    dia =  dias % 30

    r = f'{anos} ano(s) \n{meses} mes(es) \n{dia} dia(s)'
    print(r)
conv(dias)

