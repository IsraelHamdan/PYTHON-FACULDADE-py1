def verifica () :
    try:
        matricula = int(input('Insira o seu numero de matricula: '))
    except ValueError:
        if type(matricula) == str: 
            print("Você digitou uma letra, insira o número de matricula sem letras, se houver uma letra, troque a letra pela posição dela no alfabeto, por exemplo d é a quarta letra do afabeto")
            matricula = int(input("Digte seu número de matricula"))
        elif type(matricula) == int :
            print("verificando numero de matricula")

    return matricula
verifica()