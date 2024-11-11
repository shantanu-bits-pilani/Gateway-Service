# Gateway Service

## Description
The Gateway Service acts as an API gateway to route requests to the appropriate microservices.

## Endpoints

### Register
- **URL:** `/register`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "username": "string",
    "password": "string"
  }
- **Response:**
    - 201 Created if the user is registered successfully.
    - 400 Bad Request if the user already exists.

### Login
- **URL:** `/login`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "username": "string",
    "password": "string"
  }
- **Response:**
    - 200 OK if the login is successful.
    - 401 Unauthorized if the credentials are invalid.

### Send Message
- **URL:** `/send`
- **Method:** `POST`
- **Request Body:**
  ```json
    {
        "sender": "string",
        "receiver": "string",
        "message": "string"
    }
- **Response:**
    - 201 Created if the message is sent successfully.

### Get Message
- **URL:** `/message`
- **Method:** `GET`
- **Response:**
    - 200 OK with a list of messages.

### Create User Profile
- **URL:** `/create`
- **Method:** `POST`
- **Request Body:**
  ```json
    {
        "username": "string",
        "profile": {
            "name": "string",
            "email": "string"
        }
    }
- **Response:**
    - 201 Created if the user profile is created successfully.
    - 400 Bad Request if the user already exists.

### Get User Profile
- **URL:** `/profile/<username>`
- **Method:** `GET`
- **Response:**
    - 200 OK with the user profile.
    - 404 Not Found if the user does not exist.


## Running the service
To run the service, use Docker Compose:
```bash docker-compose up --build gateway-service```
