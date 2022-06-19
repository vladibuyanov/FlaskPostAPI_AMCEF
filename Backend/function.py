import requests

# External API variable
BASE = 'https://jsonplaceholder.typicode.com/'


# Validation of input data for method post
def validation_post_id_user_id(post_id, user_id, title, body):
    if type(post_id) == int and type(user_id) == int:
        if validation_title_body(title, body):
            return True


# Validation of input data for method put
def validation_title_body(title, body):
    if type(title) == str and type(body) == str:
        return True


# Validation user with external AP
def validation_user(user):
    json_api = requests.get(f'{BASE}users').json()
    user_id_list = [i['id'] for i in json_api]
    if user in user_id_list:
        return True


# Search for a post using an external AP
def search_post(post_id):
    posts_res = requests.get(f'{BASE}posts/{post_id}').json()
    if posts_res:
        return posts_res
    return False
