import requests

user_id = 1
post_id = 67

BASE = 'https://jsonplaceholder.typicode.com/'

users_res = requests.get(BASE + 'users').json()
post_res = requests.get(f'{BASE}posts/{post_id}').json()


# for users
# id_list = [i['id'] for i in users_res]
# if user_id in id_list:
#     print(True)

# for posts
print(post_res)


