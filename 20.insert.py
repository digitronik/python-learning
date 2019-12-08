def eggs(example):
    example.insert(-1,'and')
    
spam = ['apple','banana','tofu','cats']

eggs(spam)
print(spam)
string = ','.join(map(str,spam))
print (string)