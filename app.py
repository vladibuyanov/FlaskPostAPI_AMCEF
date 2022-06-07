from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

import requests

app = Flask(__name__)
api = Api()
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)


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

resource_fields = {
    'id': fields.Integer,
    'user_id': fields.Integer,
    'title': fields.String,
    'body': fields.String,
}


# Validation of input data
def validation_input(post_id, user_id, title, body):
    if type(post_id) == int and type(user_id):
        if int and type(title) == str and type(body) == str:
            return True


# Validation with a third party API
def validation_user(user):
    json_api = requests.get('https://jsonplaceholder.typicode.com/users').json()
    user_id_list = [i['id'] for i in json_api]
    if user in user_id_list:
        return True


class Main(Resource):
    @marshal_with(resource_fields)
    def get(self, post_id):
        result = Posts.query.filter_by(id=post_id).first()
        if result:
            return result
        else:
            abort(404, message='Could not find post with that id')

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
                    return 'Add done!', 201
                abort(409, message='Post with this id is already exist')
            abort(401, message='Authorization failed')
        abort(408, message='Incorrect data')

    @marshal_with(resource_fields)
    def put(self, post_id):
        result = Posts.query.filter_by(id=post_id).first()
        if result:
            args = posts_put_args.parse_args()
            if validation_input(post_id, args['user_id'], args['title'], args['body']):
                if args['title']:
                    result.title = args['title']
                if args['body']:
                    result.body = args['body']
                db.session.commit()
                return 'Change done!', 202
            abort(408, message='Incorrect data')
        abort(409, message='Post not exist')

    def delete(self, post_id):
        result = Posts.query.filter_by(id=post_id).first()
        db.session.delete(result)
        db.session.commit()
        return 'Delete done!', 203


api.add_resource(Main, '/api/main/<int:post_id>')

api.init_app(app)

if __name__ == '__main__':
    app.run()
