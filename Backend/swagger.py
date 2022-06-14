# Flasgger

specs_dict_get = {
    "tags": [
        "Posts"
    ],
    "parameters": [
        {
            "in": "path",
            "type": "integer",
            "name": "post_id",
            "required": "true",
            "default": "5"
        }
    ],
    # "responses": {
    #     "200": {
    #         "description": "Get single user",
    #         "schema": {
    #             'id': 'Posts',
    #             'properties': {
    #                 'id': {
    #                     'type': 'integer'
    #                 },
    #                 'user_id': {
    #                     'type': 'integer'
    #                 },
    #                 'title': {
    #                     'type': 'string'
    #                 },
    #                 'body': {
    #                     'type': 'string'
    #                 }
    #             }
    #         }
    #     }
    # }
}
specs_dict_delete = {
    "tags": [
        "Posts"
    ],
    "parameters": [
        {
            "in": "path",
            "type": "integer",
            "name": "post_id",
            "required": "true",
            "default": "13"
        }
    ]
}
specs_dict_post = {
    "tags": [
        "Posts"
    ],
    'parameters': [
        {
            "in": "path",
            "type": "integer",
            "name": "post_id",
            "required": "true",
            "default": "13",
        },
        {
            "in": "body",
            'name': 'id',
            "required": "true",
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {
                        'type': 'integer',
                        'example': '13'
                    },
                    'user_id': {
                        'type': 'integer',
                        'example': '1'
                    },
                    'title': {
                        'type': 'string',
                        'example': "New post"
                    },
                    'body': {
                        'type': 'string',
                        'example': "It's new post"
                    }
                }
            }
        }
    ]
}
specs_dict_put = {
    "tags": [
        "Posts"
    ],
    'parameters': [
        {
            "in": "path",
            "type": "integer",
            "name": "post_id",
            "required": "true",
            "default": "13",
        },
        {
            "in": "body",
            'name': 'id',
            "required": "true",
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {
                        'type': 'integer',
                        'example': '13'
                    },
                    'user_id': {
                        'type': 'integer',
                        'example': '1'
                    },
                    'title': {
                        'type': 'string',
                        'example': "Changed post"
                    },
                    'body': {
                        'type': 'string',
                        'example': "It's changed post"
                    }
                }
            }
        }
    ]
}
