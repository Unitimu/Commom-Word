handle = open(input('Choose a file by typing its name: '))
dictionary = dict()

for lines in handle:
    words = lines.split()
    for word in words:
        dictionary[word] = dictionary.get(word, 0) + 1

listaSuprema = list()
for k,v in dictionary.items():
    new = (v,k)
    listaSuprema.append(new)

listaSuprema = sorted(listaSuprema, reverse=True)

for x,y in listaSuprema[:10]:
    print(y,x)

# List Comprehension --- O (v,k) é o carimbo que se reperte até formar a lista, delimitada pelo FOR
print(sorted([(v,k) for k,v in dictionary.items()],reverse=True))    