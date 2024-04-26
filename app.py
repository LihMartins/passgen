# Import necessary modules from flask
from flask import Flask, render_template, request

# Import string and random for generating random strings
import string
import random


# Create a Flask web server from the Flask app.
app = Flask(__name__)


# Function to generate a password of a given length
def password_generator(length=8):
    # Check if length is a positive integer
    if not isinstance(length, int) or length <= 0:
        # If not, raise an error
        raise ValueError("Length must be a positive integer.")

    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a password of the given length using the characters
    password = "".join(random.choice(characters) for i in range(length))
    # Return the generated password
    return password


# Define the route for the URL
@app.route("/", methods=["GET", "POST"])
def home():
    # Initialize the password as an empty string
    password = ""
    # If the request method is POST
    if request.method == "POST":
        try:
            # Try to convert the length to an integer and generate a password
            # The length is retrieved from the form data
            password = password_generator(int(request.form.get("length")))
        except ValueError:
            # If a ValueError is raised,
            # set an error message as the password
            password = "Error: Length must be a positive integer."

    # Render the index.html template and pass in the password
    # The password is either the generated password or the error message
    return render_template("index.html", password=password)


# If this file is run directly (not imported), start the web server
if __name__ == "__main__":
    app.run(debug=True)
