import csv

with open('pliki/dane2.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';', dialect='excel')
    for r in reader:
        print(r)


# with open('pliki/dane2.csv', 'r') as file:
#     reader = csv.DictReader(file,delimiter=';')
#     # for r in reader:
#         # print(dict(r))



# lista = [[3, 'java', 'MA'], [4, 'java', 'MA'], [5, 'java', 'MA']]

# with open('pliki/dane3.csv', 'w', newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["SN", 'Title', 'Author'])
#     writer.writerow([1, 'Python', 'TK'])
#     writer.writerow([2, 'java', 'MA'])
#     writer.writerows(lista)
