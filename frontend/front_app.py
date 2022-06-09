import requests
from flask import Flask, render_template, request

app = Flask(__name__)
BASE = "http://127.0.0.1:5000/"


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/get', methods=['GET', 'POST'])
def get_json():
    if request.method == 'POST':
        user_post = request.form['user_post']
        res = requests.get(BASE + f'/api/main/{user_post}')
        print(type(res))
        return render_template('get.html', res=res)
    return render_template('get.html')


@app.route('/post', methods=['GET', 'POST'])
def post_json():
    if request.method == 'POST':
        user_post = request.form['user_post']
        new_post = {
            'id': user_post,
            'user_id': request.form['user_id'],
            'title': request.form['title'],
            'body': request.form['body']
        }
        res = requests.post(BASE + f'/api/main/{user_post}', json=new_post).json()
        return render_template('post.html', res=res)
    return render_template('post.html')


@app.route('/put', methods=['GET', 'POST'])
def put_json():
    if request.method == 'POST':
        user_post = request.form['user_post']
        new_post = {
            'title': request.form['title'],
            'body': request.form['body']
        }
        res = requests.put(BASE + f'/api/main/{user_post}', json=new_post)
        return render_template('put.html', res=res)
    return render_template('put.html')


@app.route('/delete', methods=['GET', 'POST'])
def delete_json():
    if request.method == 'POST':
        user_post = request.form['user_post']
        res = requests.delete(BASE + f'/api/main/{user_post}')
        return render_template('delete.html', res=res)
    return render_template('delete.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
    