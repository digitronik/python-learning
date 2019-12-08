spam = {'color':'red','type':'fine','model': '2020'}
for i in spam.values():
    print(i)
for j in spam.keys():
    print(j)
for k in spam.items():
    print(k)
spam.setdefault('range','45')
    print(spam)