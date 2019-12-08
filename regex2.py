import re
phoneNum = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
num = phoneNum.search('My number is 415-555-4242.')
print('Phone number found: ' + num.group())
print(num.group(1))
print(num.group(2))
areaCode, mainNumber = num.groups()
print(areaCode)
print(mainNumber)
