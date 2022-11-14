import requests


def get_api_key(email: str, password: str):
    headers = {
        'email': email,
        'password': password,
    }
    res = requests.get(f'https://petstore.swagger.io/v2/swagger.json/api/key', headers=headers)

print(get_api_key('atyuhtina111@gmail.com','Qwerty123'))

def add_new_pet(email: str, password: str):
    headers = {
        'email': email,
        'password': password,
    }
    data ={
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    res = requests.post(f'https://petstore.swagger.io/v2/swagger.json/pet', headers=headers, data=data)

print(add_new_pet('atyuhtina111@gmail.com','Qwerty123'))

def updates_user(data: str):
    data = {
        "id": 0,
        "username": "string",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }

    res = requests.put(f'https://petstore.swagger.io/v2/swagger.json', data=data)

print(updates_user)
