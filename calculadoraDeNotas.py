nome = str(input('insira um nome: '))
notas = int(input('insira uma nota: '))
students = {1: [nome], 2: [nome], 3: [nome]}
nota = {1: [notas], 2: [notas], 3: [notas]}
media = int(input('insira a media para  aprovação: '))

def calculo(nota, media, students):
    if nota == media or nota > media :
        situacao = 'aprovado'
    elif nota == 5 or nota < media :
        situacao = "recuperação"
    else:
        situacao = "reprovado"
    print(f'o {students} está: {situacao}')


calculo(nota, media, students)

