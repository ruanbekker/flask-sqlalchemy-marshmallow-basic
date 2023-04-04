# flask-sqlalchemy-marshmallow-basic
Flask SQLAlchemy with Marshmallow (unstructured)

## Installation

```
python3 -m virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Or a public docker hub container image `ruanbekker/flask-rest-api`.

## Routes

- `/users` GET
- `/users` POST
- `/users/<id>` GET
- `/users/<id>` PUT
- `/users/<id>` DELETE


## Usage

Create Users:

```
$ curl -XPOST -H 'Content-Type: application/json' http://localhost:5000/users -d '{"username": "ruan.bekker", "email": "ruan.bekker@localhost"}'
{
  "id": 2,
  "username": "james.dean",
  "email": "james.dean@localhost"
}

$ curl -XPOST -H 'Content-Type: application/json' http://localhost:5000/users -d '{"username": "james.dean", "email": "james.dean@localhost"}'
{
  "id": 2,
  "username": "james.dean",
  "email": "james.dean@localhost"
}
```

List Users:

```
$ curl -H 'Content-Type: application/json' http://localhost:5000/users
[
  {
    "id": 1,
    "username": "ruan.bekker",
    "email": "ruan.bekker@localhost"
  },
  {
    "id": 2,
    "username": "james.dean",
    "email": "james.dean@localhost"
  }
]
```

View One User:

```
$ curl -H 'Content-Type: application/json' http://localhost:5000/users/1
{
  "id": 1,
  "username": "ruan.bekker",
  "email": "ruan.bekker@localhost"
}
```

Update User:

```
$ curl -XPUT -H 'Content-Type: application/json' http://localhost:5000/users/1 -d '{"username": "ruan.bekker", "email": "ruan@localhost"}'
{
  "id": 1,
  "username": "ruan.bekker",
  "email": "ruan@localhost"
}
```

Delete User:

```
$ curl -XDELETE -H 'Content-Type: application/json' http://localhost:5000/users/2
{
  "id": 2,
  "username": "james.dean",
  "email": "james.dean@localhost"
}
```

## Resources

- [1](https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application), [2](https://gist.github.com/Babatunde13/81866103136d20090a6f5c17f5de336b), [3](https://realpython.com/flask-connexion-rest-api-part-2/)
