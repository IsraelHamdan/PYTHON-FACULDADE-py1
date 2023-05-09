def entrada():
   listaa = [int(k) for k in input().split()]
   listab = [int(k) for k in input().split()]
   return listaa, listab

def remove_repetidos(lista1, lista2):
   conjuntoa = set(lista1)
   conjuntob = set(lista2)
   a_b = conjuntoa.difference(conjuntob)
   b_a = conjuntob.difference(conjuntoa)
   print(min(len(a_b),len(b_a)))

while True:
   a, b = input().split()
   if a == b == "0":
      break
   alice, beatriz = entrada()
   remove_repetidos(alice,beatriz)