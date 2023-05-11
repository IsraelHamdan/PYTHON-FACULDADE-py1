while True:
    a, b =  input().split()

    if a and b == '0':
        break

    alice = set(list(map(int, input().split())))
    
    beatriz = set(list(map(int, input().split())))
 
    diffA_B = alice.difference(beatriz)
    diffB_A = beatriz.difference(alice)

    troca = min(len(diffA_B), len(diffB_A))

    print(troca)