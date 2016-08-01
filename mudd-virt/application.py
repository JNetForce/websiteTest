from flask import Flask

# Set our site to the main applcation
application = Flask(__name__)

# Homepage
@application.route("/")
def index():
    # Hello World in h1 type
    return '<h1>Hello World!</h1>'

if __name__ == "__main__":
    # allow debug mode
    application.debug = True
    application.run()
