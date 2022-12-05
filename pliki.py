# plik = open("pliki/dane1.txt", 'r')
# # test = open(r'C:\Użytkownicy\Janek\temp\test.txt')
# # print(plik)
# name = "Tomek"
# customers = ['Nela', 'Roman', 'Adam', 2022]
# slownik = {1: "tomek", 2: 'romek', 3: 'antek'}

# plik.write(name)
# plik.write("\n")
# plik.write(str(customers))

# for i in customers:
#     plik.write("\n")
#     plik.write(str(i))
#     # print(i)

# for i in slownik.items():
#     plik.write("\n")
#     plik.write(str(i))


# lista = []
# content = plik.readline()
# content1 = plik.readline()
# content2 = plik.readline()
# # print(content)
# lista.append(content)
# lista.append(content1)
# lista.append(content2)
# print(lista)


# for c in plik.read():
#     lista.append(c)
#
# print(lista)
# plik.close()


# with open('pliki/dane1.txt', 'a') as f:
#     f.write("\nkolejny wpis")

with open('pliki/dane1.txt', 'r') as f:
    plik = f.read().rsplit('\n')
    print(plik)


