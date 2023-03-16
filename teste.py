nota = eval(input('Digte a nota do aluno:'))
media = eval(input('Digite a média para ser aprovado:'))

def aprovacao ():
   if nota > media or nota == media:
      print('o aluno está aprovado')
   if nota < media or nota == 5 :
      print('o aluno está de recuperação')
   if nota < 5 :
      print('o aluno está reprovado')
aprovacao()

