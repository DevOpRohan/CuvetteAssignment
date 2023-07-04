# Flask MongoDB Registration Form

This is a simple Flask application that uses MongoDB as its database. It includes a registration form where users can enter their name, university, and course. After the form is submitted, the data is saved to the MongoDB database and displayed on the webpage.

## Requirements

- Python
- Flask
- Flask-MongoEngine
- MongoDB

## Installation

1. Clone this repository.
2. Install the required packages using pip:

```bash
pip install -r requirements.txt
```

3. Make sure MongoDB is running on your machine or set up a MongoDB Atlas cluster and add the connection string to the `app.config['MONGODB_SETTINGS']` in `app.py`.

## Usage

1. Run the Flask application:

```bash
python app.py
```

2. Open your web browser and navigate to `http://localhost:5000`.

3. Fill out the registration form and click "Submit". The data you entered will be saved to the MongoDB database and displayed on the webpage.
