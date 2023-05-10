def entrada():
    a = [int(i) for i in input().split()]
    b = [int(j) for j in input().split()]

    return a, b

def no_repeat(alice, bea):
   alice = set(alice)
   bea = set(bea)

   diff_A_B = alice.difference(bea)
   diff_B_A = bea.difference(alice)
   
   troca = min(len(diff_A_B), len(diff_B_A))

   print(troca)

while True:
    inputA, inputB = map(int, input().split())

    if inputA and inputB == 0:
        break
    
    alice, bea = entrada()
    no_repeat(alice, bea)
