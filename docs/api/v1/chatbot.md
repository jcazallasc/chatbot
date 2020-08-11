# Chatbot V1
Supports:
- Listing users
- Create new user

## Listing users

**Request**:

`GET` `http://localhost:8000/api/v1/users/`

*Note:*

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
200 OK

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "username": "jcazallasc@gmail.com",
            "email": "jcazallasc@gmail.com",
            "phone": "123123123"
        }
    ]
}
```

## Create new user

**Request**:

`POST` `http://localhost:8000/api/v1/users/`

Parameters:

Name       | Type   | Required |
-----------|--------|----------|
username   | string | Yes      |
email      | string | Yes      |
phone      | string | Yes      |

*Note:*

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
201 Created

{
    "username": "test",
    "email": "test@test.com",
    "phone": "123123123"
}
```