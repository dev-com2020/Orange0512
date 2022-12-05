# x = 1
# z = 12
# y = 2
# a = range(x, z, y)
# b = list(a)
# print(a)
# print(b)


def infinite_seq():
    num = 0
    while True:
        yield num
        num += 1

#
# for i in infinite_seq():
#     print(i, end=" ")


# infinite_seq()
lista = []

gen = infinite_seq()
# print(next(gen))
for i in range(5):
    lista.append(next(gen))

lista.append('Tomek')
lista.append(next(gen))
lista.append(next(gen))
lista.append(next(gen))
print(lista)
lista.append(next(gen))
print(lista)





# print(next(gen))
# print(next(gen))
# for i in range(2):
#     print("Inne rzeczy w programie")
# print(next(gen))