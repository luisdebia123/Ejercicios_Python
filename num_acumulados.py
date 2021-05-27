import decimal
from datetime import datetime, time, date
import locale
from random import randrange
import random
from random import randint
import calendar
# print('Mínimo   :',heapq.nsmallest(1,lista))
import heapq
# print('Máximo   :',heapq.nlargest(1,lista))

import math


from os import system
system("cls")


print()
print(" Números acumulados")
print()

# Generar 10 números aleatorios entre 10 y 29 no repetidos y ordenarlos.

a = []
b = []
numeros=0
while numeros<=9:
    x=random.randint(10,29)
    x=str(x)
    a.append(x)
    n = a.count(x)
    if n == 1:
        b.append(x)
        numeros =numeros + 1

print(a, "lista 'a' desordenada")
a.sort()
print(a, "lista 'a' ordenada")
b.sort()
print(b, "lista final ordenada")