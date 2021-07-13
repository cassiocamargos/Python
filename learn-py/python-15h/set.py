'''list1 = [10, 20, 30, 40, 50]
list2  = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) #union
print(num1 - num2) #difference
print(num1 ^ num2) #symmetric difference
print(num1 & num2) #and

print(len(num1))'''


'''list1 = set([1, 2, 3, 4, 5, 6])
s1 = {1, 2, 3, 4, 5, 6}

s1.add(7)
s1.update([7, 8, 9, 10])
s1.remove(10) #gera erro se o numero nao existir
s1.discard(10) #nao gera erro se o numero nao existir

print(s1)'''


s1 = {'a', 'b', 'c'}
s2 = {'a', 'd', 'e'}
s3 = {'c', 'd', 'f'}

s4 = s1.union(s2)
s4 = s1.difference(s3)
s4 = s1.intersection(s2)
s4 = s1.symmetric_difference(s3)

print(s4)
