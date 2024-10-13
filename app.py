# Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv.
# Completed

# Explore the ‘Flask’ module and create a web server using Flask & Python.
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
app.run()