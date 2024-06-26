# CodeLeap Network API

This project provides a RESTful API backend, built with Django and Django REST Framework, designed for managing posts on the CodeLeap Network. 

## Features

- CRUD operations.
- Automated tests for API endpoints.
- Swagger and Redoc documentation for API endpoints.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- pip

### Installation

1. Clone the repository: `https://github.com/CCerrer/django-CRUD.git`
2. Navigate to the project directory: `cd django-CRUD`
3. Install the required packages: `pip install -r requirements.txt`
4. Apply the migrations: `python mange.py migrate`
5. Run the development server: `python manage.py runserver`
6. The API will be available at `http://127.0.0.1:8000/api/` and Swagger on `http://127.0.0.1:8000/swagger/`.

## Testing

To run the automated tests for this system, use: `python manage.py test`

## Documentation

To view the API documentation, navigate to:

- Swagger UI: `http://127.0.0.1:8000/swagger/`
- Redoc: `http://127.0.0.1:8000/redoc/`