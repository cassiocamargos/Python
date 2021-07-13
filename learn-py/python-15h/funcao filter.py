"""v = [ 10, 12, 34, 44, 57]

'''def remover20(x):
    return x > 20

print(list(map(remover20, v)))
print(list(filter(remover20, v)))'''

print(list(map(lambda x: x > 20, v)))
print(list(filter(lambda x: x > 20, v)))"""