# Flask MongoDB CRUD API

This is a simple Flask application that demonstrates how to perform CRUD (Create, Read, Update, Delete) operations on a MongoDB database through a REST API. The application manages a `User` resource with basic user details such as `name`, `email`, and `password`. The password is securely hashed before storing in the database.

## Features

- **Create User**: Add a new user to the database.
- **Read User**: Get details of a user by their ID.
- **Update User**: Update user details by their ID.
- **Delete User**: Delete a user by their ID.
- **Password Hashing**: User passwords are securely hashed using `werkzeug.security`.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework.
- **MongoDB**: A NoSQL database to store user data.
- **Flask-PyMongo**: Flask extension to simplify working with MongoDB.
- **Werkzeug**: Provides utilities for secure password hashing.

## Setup Instructions

### Prerequisites

- Python 3.6 or higher
- Docker (for running MongoDB)
- MongoDB running in Docker container (configured via Docker Compose)

### Install Dependencies

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    Docker Setup
    Ensure Docker is installed on your system.

4. Build and run the Docker containers:

    ```bash
    docker-compose up --build
    This will start both your Flask application and a MongoDB container.

5. Running the Application
    Once the application and MongoDB container are up and running, navigate to http://localhost:5000.
    You can interact with the API using Postman or any HTTP client.
    API Endpoints
    POST /users: Create a new user.

- **POST** `/users`: Create a new user.
  - **Request Body (JSON)**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com",
      "password": "password123"
    }
    ```

- **GET** `/users`: Retrieve a list of all users.

- **GET** `/users/{id}`: Retrieve a user by their ID.

- **PUT** `/users/{id}`: Update a user by their ID.
  - **Request Body (JSON)**:
    ```json
    {
      "name": "John Updated",
      "email": "john.updated@example.com",
      "password": "newpassword123"
    }
    ```

- **DELETE** `/users/{id}`: Delete a user by their ID.

<!-- ## Docker Commands

- **Build Docker image**:
  ```bash
  docker-compose build


### Explanation:

- **Project Title**: `# Flask MongoDB CRUD API` – A brief title of your project.
- **Description**: A concise overview of what your project does.
- **Technologies**: Lists the main technologies used in your project.
- **Setup Instructions**: Steps to get your application running locally.
- **API Endpoints**: Details of the available REST API endpoints, including methods and sample JSON payloads.
- **Docker Setup**: Instructions to build and run Docker containers for both Flask and MongoDB.
- **License**: Information on the project license (if applicable). -->









