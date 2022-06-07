import requests

BASE = "http://127.0.0.1:5000/"

user_post = None
crud = None


while user_post != 'stop':
    crud = input("0 - del, 1 - get, 2- put, 3 - post : ")
    user_post = int(input('Post: '))

    if crud == "1":
        res = requests.get(BASE + f'/api/main/{user_post}')

    elif crud == "2":
        new_post = {
            'title': input('title: '),
            'body': input('body: ')
        }
        res = requests.put(BASE + f'/api/main/{user_post}', json=new_post)

    elif crud == "3":
        new_post = {
                'id': int(input('id: ')),
                'user_id': int(input('user_id: ')),
                'title': input('title: '),
                'body': input('body: ')
        }
        res = requests.post(BASE + f'/api/main/{user_post}', json=new_post)
    else:
        res = requests.delete(BASE + f'/api/main/{user_post}')

    print(res.json())

