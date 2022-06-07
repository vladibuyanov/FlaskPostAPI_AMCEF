import requests

BASE = 'https://jsonplaceholder.typicode.com/'

res = requests.get(BASE + 'users').json()
user_id = 1

id_list = [i['id'] for i in res]
print(id_list)


