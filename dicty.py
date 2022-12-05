import csv

# with open('customer.csv', 'w', newline="") as file:
#     fieldnames = ['name', 'rating']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'name': "TK", 'rating': 123})
#     writer.writerow({'name': "TE", 'rating': 133})
#     writer.writerow({'name': "TR", 'rating': 323})


def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result

def csv_reader2(file_name):
    for row in open(file_name,'r'):
        print(row)
        yield row



plik = csv_reader2('sample.csv')
lista = []


for i in range(10):
    lista.append(next(plik))

print(lista)


