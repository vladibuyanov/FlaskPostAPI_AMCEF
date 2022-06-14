# Test work for AMCEF
Python microservice containing a RESTful API for managing user messages.

## Content
- [Tech](#tech)
- [Usage](#Usage)

## Technology
- [Python](https://www.python.org/)
- [flask](https://flask.palletsprojects.com/en/2.1.x/)

## Usage
Install the used libraries into your virtualenv with the command:
```sh
pip install requiremenst.txt
```

### Starting the Development server
To start the development server, run the command:
```sh
python app.py runserver
```

### API requests
API requests are made to the address:
```sh
127.0.0.1:5000/app/main/{post_id}
```

### Examples
```sh
curl -X GET --header 'Accept: application/json' 'http://127.0.0.1:5000/api/main/1'
```

### Swagger
To use swagger: 
- start the server
- go to http://127.0.0.1:5000/apidocs/