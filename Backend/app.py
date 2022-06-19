from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger, swag_from

import my_swagger
from function import validation_post_input, validation_title_body, validation_user, search_post

app = Flask(__name__)
api = Api()
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
swag = Swagger(app)


# Data base models
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=True)
    title = db.Column(db.String(50), nullable=True)
    body = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f'Post(user_id = {self.user_id}, title = {self.title}, body = {self.body})'


# Posts - post request parsing
posts_post_args = reqparse.RequestParser()
posts_post_args.add_argument("id", type=int, help='Id of post', required=True)
posts_post_args.add_argument("user_id", type=int, help='User id of post', required=True)
posts_post_args.add_argument("title", type=str, help='Post title', required=True)
posts_post_args.add_argument("body", type=str, help='Post body', required=True)

# Posts - put request parsing
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


class Main(Resource):
    @marshal_with(resource_fields)
    @swag_from(my_swagger.specs_dict_get)
    def get(self, post_id):
        result = Posts.query.filter_by(id=post_id).first()
        if result:
            return result, 200
        elif search_post(post_id):
            post_from_api = Posts(
                id=post_id,
                user_id=search_post(post_id)['userId'],
                title=search_post(post_id)['title'],
                body=search_post(post_id)['body']
            )
            db.session.add(post_from_api)
            db.session.commit()
            return search_post(post_id), 200
        return abort(408, message='Post not exist')

    @swag_from(my_swagger.specs_dict_post)
    def post(self, post_id):
        args = posts_post_args.parse_args()
        if validation_post_input(post_id, args['user_id'], args['title'], args['body']):
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

    @swag_from(my_swagger.specs_dict_put)
    def put(self, post_id):
        result = Posts.query.filter_by(id=post_id).first()
        if result:
            args = posts_put_args.parse_args()
            if validation_title_body(args['title'], args['body']):
                if args['title']:
                    result.title = args['title']
                if args['body']:
                    result.body = args['body']
                db.session.commit()
                return 'Post was changed', 202
            abort(403, message='Incorrect data')
        abort(408, message='Post not exist')

    @swag_from(my_swagger.specs_dict_get)
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
