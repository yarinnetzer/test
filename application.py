from flask import Flask

application = Flask(__name__)

@application.route('/')
def index():
    return 'Web App with Python Flask!'

if __name__ == "__main__":
    application.debug = True
    application.run()
