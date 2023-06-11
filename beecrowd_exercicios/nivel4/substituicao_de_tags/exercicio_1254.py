while True:
    try:
        tag = input()
        numero = input()
        frase = input()

        frase_modificada = ''
        dentro = False

        i = 0
        while i < len(frase):
            if frase[i] == '<':
                dentro = True
                frase_modificada += frase[i]
                i += 1
                continue
            elif frase[i] == '>':
                dentro = False
                frase_modificada += frase[i]
                i += 1
                continue
            if dentro:
                if frase[i:].upper().startswith(tag.upper()):
                    frase_modificada += numero
                    i += len(tag)
                else:
                    frase_modificada += frase[i]
                    i += 1
            else:
                frase_modificada += frase[i]
                i += 1
        print(frase_modificada)
    except EOFError:
        break
