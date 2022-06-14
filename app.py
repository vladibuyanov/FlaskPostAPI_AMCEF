import requests
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger, swag_from

from swagger import *

app = Flask(__name__)
api = Api()
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
swag = Swagger(app)

# External API variable
BASE = 'https://jsonplaceholder.typicode.com/'


# Data base models
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=True)
    title = db.Column(db.String(50), nullable=True)
    body = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f'Post(user_id = {self.user_id}, title = {self.title}, body = {self.body})'


# Posts - post
posts_post_args = reqparse.RequestParser()
posts_post_args.add_argument("id", type=int, help='Id of post', required=True)
posts_post_args.add_argument("user_id", type=int, help='User id of post', required=True)
posts_post_args.add_argument("title", type=str, help='Post title', required=True)
posts_post_args.add_argument("body", type=str, help='Post body', required=True)

# Posts - put
posts_put_args = reqparse.RequestParser()
posts_put_args.add_argument("id", type=int, help='Id of post')
posts_put_args.add_argument("user_id", type=int, help='User id of post')
posts_put_args.add_argument("title", type=str, help='Post title')
posts_put_args.add_argument("body", type=str, help='Post body')

# Serialization to json
resource_fields = {
    'id': fields.Integer,
    'user_id': fields.Integer,
    'title': fields.String,
    'body': fields.String,
}


# Validation of input data
def validation_input(post_id, user_id, title, body):
    if type(post_id) == int and type(user_id) == int:
        if type(title) == str and type(body) == str:
            return True


def validation_put_input(title, body):
    if type(title) == str and type(body) == str:
        return True


# Validation with a third party API
def validation_user(user):
    json_api = requests.get(f'{BASE}users').json()
    user_id_list = [i['id'] for i in json_api]
    if user in user_id_list:
        return True


# Search for a post using an external AP
def search_post(post_id):
    posts_res = requests.get(f'{BASE}posts/{post_id}').json()
    return posts_res


class Main(Resource):
    @marshal_with(resource_fields)
    @swag_from(specs_dict_get)
    def get(self, post_id):
        result = Posts.query.filter_by(id=post_id).first()
        if result:
            return result
        post_from_api = Posts(
            id=post_id,
            user_id=search_post(post_id)['userId'],
            title=search_post(post_id)['title'],
            body=search_post(post_id)['body']
        )
        db.session.add(post_from_api)
        db.session.commit()
        return search_post(post_id), 200

    @swag_from(specs_dict_post)
    def post(self, post_id):
        args = posts_post_args.parse_args()
        if validation_input(post_id, args['user_id'], args['title'], args['body']):
            if validation_user(args['user_id']):
                result = Posts.query.filter_by(id=post_id).first()
                if not result:
                    user_post = Posts(
                        id=post_id,
                        user_id=args['user_id'],
                        title=args['title'],
                        body=args['body']
                    )
                    db.session.add(user_post)
                    db.session.commit()
                    return 'Post was created', 201
                abort(410, message='Post with this id is already exist')
            abort(401, message='Authorization failed')
        abort(403, message='Incorrect data')

    @swag_from(specs_dict_put)
    def put(self, post_id):
        result = Posts.query.filter_by(id=post_id).first()
        if result:
            args = posts_put_args.parse_args()
            if validation_put_input(args['title'], args['body']):
                if args['title']:
                    result.title = args['title']
                if args['body']:
                    result.body = args['body']
                db.session.commit()
                return 'Post was changed', 202
            abort(403, message='Incorrect data')
        abort(408, message='Post not exist')

    @swag_from(specs_dict_get)
    def delete(self, post_id):
        result = Posts.query.filter_by(id=post_id).first()
        if result:
            db.session.delete(result)
            db.session.commit()
            return 'Delete done!', 203
        abort(410, message='Post not exist')


api.add_resource(Main, '/api/main/<int:post_id>')
api.init_app(app)

if __name__ == '__main__':
    app.run()
