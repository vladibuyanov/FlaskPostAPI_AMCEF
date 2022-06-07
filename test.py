import requests

BASE = 'https://jsonplaceholder.typicode.com/'

res = requests.get(BASE + 'users').json()
user_id = 1

id_list = [i['id'] for i in res]
print(id_list)

# for i in res:
#     id_list.append(i['id'])
#
#
# if user_id in id_list:
#     print(True)
#     for i in res:
#         print(i)
# else:
#     print(False)


# print(res.json())

