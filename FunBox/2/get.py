import requests
import datetime

a = "Maria.ru"
b = "rose.ru"
c = "sina.ru"

d = datetime.datetime.today().replace(microsecond=0)
response = requests.get("http://Scotch.io")
print(str(d) + ' ' + str(a)+ ' ' + str(response.status_code))
