# Gateway Service

## Description
The Gateway Service acts as an API gateway, forwarding requests to the appropriate microservices. It provides endpoints for user registration, login, messaging, and user management.

## Endpoints
- `POST /api/register`: Forward registration request to Auth Service.
- `POST /api/login`: Forward login request to Auth Service.
- `POST /api/send`: Forward send message request to Chat Service.
- `GET /api/messages/<receiver>`: Forward get messages request to Chat Service.
- `POST /api/create`: Forward create user request to User Service.
- `GET /api/profile`: Forward get profile request to User Service.
- `GET /api/users`: Forward get users request to Auth Service.
- `POST /api/send-request/<r_username>`: Forward send friend request to User Service.
- `POST /api/accept-request/<r_username>`: Forward accept friend request to User Service.
- `POST /api/withdraw-request/<r_username>`: Forward withdraw friend request to User Service.
- `GET /api/friends`: Forward get friends request to User Service.

### Register
- **URL:** `/api/register`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
      "username": "string",
      "password": "string",
      "email": "string",
      "mobile": "string",
      "name": "string",
  }
- **Response:**
    - 201 `Created` if the user is registered successfully.
    - 400 `Bad Request` if the user already exists.

### Login
- **URL:** `/api/login`
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
- **URL:** `/api/send`
- **Method:** `POST`
- **Headers:**
  - `X-Logged-In-UserName: <username>`
- **Request Body:**
  ```json
    {
        "sender": "string",
        "receiver": "string",
        "message": "string"
    }
- **Response:**
    - 201 `Created` if the message is sent successfully.

### Get Message
- **URL:** `/api/message`
- **Method:** `GET`
- 
- **Response:**
    - 200 OK with a list of messages.

### Get User Profile
- **URL:** `/api/profile/<username>`
- **Method:** `GET`
- **Response:**
    - 200 OK with the user profile.
    - 404 Not Found if the user does not exist.


## Running the service
To run the service, use Docker Compose:
```bash docker-compose up --build gateway-service```
