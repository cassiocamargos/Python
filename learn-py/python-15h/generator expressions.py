from sys import getsizeof

valores = [x * 10 for x in range(1000)]
print(type(valores))
#print(valores)
print(getsizeof(valores))

print()

valores = (x * 10 for x in range(1000))
print(type(valores))
#print(list(valores))
print(getsizeof(valores))