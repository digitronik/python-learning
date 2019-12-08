def eggs(spam):
    spam.append('hello')
    return spam

iamlist = [1,2,3,4]

eggs(iamlist)
print(iamlist)
eggs(iamlist)
eggs(iamlist)
eggs(iamlist)
eggs(iamlist)
eggs(iamlist)
eggs(iamlist)
print(iamlist)

a = [4,5,6]

eggs(a)
print(a)