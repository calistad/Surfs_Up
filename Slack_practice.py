# Import the Flask dependency.
from flask import Flask

# Create a new Flask instance called app.
app = Flask(__name__)

# Create Flask Routes.
@app.route('/')    # Define the start point, the root.
def hello_world():
    return 'Hello world'

# Run thie command in the terminal:
# export FLASK_APP=app.py
# export FLASK_ENV=development
# flask run
