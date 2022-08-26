### About

Project to integrate a simple GraphQL API with a Postgres database.

Using Python's library Graphene, FastAPI, Postgres and the JSONPlaceholder API


### Installation

```
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip && python -m pip install -r requirements.txt
```

### Running API Server locally

```
uvicorn source.main:app --reload
```

### Open [PlayGround](http://127.0.0.1:8000/graphql)


### Running Tests

Run test_main.http to test the API

### Run Docker Compose

```
docker-compose up -d
```

### Run Migrations

*This step must be run after Docker Compose is up and running,
also locally after installing the dependencies.*

```
orator migrate -c db.py
```

### Usage

Get All Users
```
query GetUsers{
  users{
    name
    username
    email
    address { city street zipcode }
  }
}
```


Get One User:
```
query GetUser{
  user(id: "2"){
    id
    name
    email
    address { city geo { lat lng } }
    company{ name }
  }
}
```

Create User:
```
mutation CreateUser{
  createUser(user: {
    name: "John Doe",
    username: "johndoe123",
    email: "johndoe@example.com",
    company: {name: "Crehana", catchPhrase:"My Courses"},
    address:{city: "Mexico", street: "Mount Av.12 b.12", geo: {lat: 12.18283, lng: -17.22}}
  }){
    id
    name
    username
    email
    address { city geo { lat lng } }
    company { name }
  }
}
```

Update User:
```
mutation UpdateUser{
  updateUser(id: "7", user:{
    email: "updateduser@example.com",
    address:{ city: "Mexico" street: "H. Avenue Av. 57.1"}
    company: {name: "Crehana", catchPhrase:"My Courses"}
  }){
    email
    address { city }
    company { name }
    
  }
}
```

Delete User:
```
mutation DeleteUser{
  deleteUser(id: "1"){
    ok
  }
}
```

### License

MIT License

Copyright (c) 2022 Adrian Romo