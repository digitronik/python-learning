catname = []
while True:
    print('Enter the name of the cat'+ str(len(catname)+ 1))
    name = input()
    if name == '':
        break
    catname = catname + [name]
print('the cat names are:')
for name in catname:
    print(name)