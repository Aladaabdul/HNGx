# HNGx
This README provides an overview and documentation of this project that allows you to manage information about people, particularly their names. 
This project includes a model, serializers, views, and URLs for handling person-related data.

# PROJECT STRUCTURE
The project structure includes the following key components:

1. people (Django app)
2. models.py: Defines the Person model
3. serializers.py: Defines the DRF serializer for the Person model
4. views.py: Contains the viewsets and view functions for handling person data
5. urls.py: Defines the API endpoints for the Person model
6. manage.py: The Django management script
7. settings.py: Django project settings
8. urls.py: The project's main URL configuration

# GETTING STARTED

1. clone the repository to your local machine
2. Navigate to the project directory
3. Create a virtual environment and activate it
4. Install the project dependencies and Apply database migrations

# PERSON MODEL

The Person model represents a person with a name. It includes the following fields:

1. id: An integer field that serves as the primary key.
2. name: A character field with a maximum length of 255 characters. 
   It uses a regex validator to ensure that names contain only letters and spaces.

# SERIALIZERS

The PersonSerializer class in serializers.py defines how Person model instances are serialized/deserialized for use in the API. 
It uses the DRF ModelSerializer class and includes all fields from the Person model.
The serializer also includes a create method, which allows you to create new Person instances by providing valid data.

# VIEWS
The PersonViewSet class in views.py extends DRF's ModelViewSet and is responsible for handling 
CRUD (Create, Retrieve, Update, Delete)operations for Person objects. 
It specifies the queryset and serializer class to us

# API Endpoints
This project exposes the following API endpoints for managing people:

1. List People: GET /api/api/
2. Create Person: POST /api/api/
3. Retrieve Person: GET /api/api/{id}/
4. Update Person: PUT /api/api/{id}/
5. Delete Person: DELETE /api/api/{id}/

# RUNNING THE PROJECT
To run the Django development server and access the API, execute the following command:

1. Python manage.py runserver
