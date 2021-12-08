# AWeber-API
Python API for AWeber assessment

## Setup Instructions

1. Clone repo: `$ git clone https://github.com/mrbnsn/AWeber-API.git`
2. Enter repo directory: `$ cd AWeber-API`
3. Create virtual environment: `$ python3 -m venv venv`
4. Start virtual environment: `$ source venv/bin/activate`
5. Install dependencies: `$ pip3 install -r requirements.txt`
6. Run app: `$ python app.py`

Submit API requests using your preferred method, e.g. Postman. 

A database is included (`db.sqlite`) with a couple of example widgets. To create a fresh database:

* Delete the existing database
* Open the Python shell within the virtual environment
* Run the commands `from app import db` and `db.create_all()`
* This will create a fresh `db.sqlite` file in the root directory.

## API Documentation

### Base URL
All request endpoints will are relative to `http://127.0.0.1:5000`.

### Create
- Header `Content-Type: application/json`
- Submit `POST` request to `/api/widget`, passing a JSON object with the following two required parameters:
- - `name`: `string` (64 characters max, must be unique)
- - `num_parts`: `int`

### Read
- Submit `GET` request to `/api/widget/<widget_id>`, providing the target widget ID.

### List
- Submit `GET` request to `/api/widgets`.

### Update
- Header `Content-Type: application/json`
- Submit `PUT` request to `/api/widget/<widget_id>`, passing a JSON object with any of the following parameters:
- - `name`: `string` (64 characters max, must be unique)
- - `num_parts`: `int`

### Delete
- Submit `DELETE` request to `http://127.0.0.1:5000/api/widget/<widget_id>`, providing the target widget ID.

## Tech Stack
- Python 3.9.9
- Flask (to server the API)
- SQLAlchemy (to model the data)
- Marshmallow (to serialize the data)
- SQLite