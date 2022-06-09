# Flasgger

specs_dict = {
    "parameters": [
        {
            "in": "path",
            "type": "integer",
            "name": "post_id",
            "required": "true",
            "default": "1"
        }
    ],
    "responses": {
        "200": {
            "description": "Single user",
            "schema": {
                'id': 'Posts',

            }
        }
    }
}
