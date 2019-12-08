import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))
#class 'requests.models.Response'>
print(res.status_code == requests.codes.ok)
 
print(len(res.text))
 
print(res.text[:250])