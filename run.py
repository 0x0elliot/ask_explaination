from flask import Flask
from flask_ask import integrate #A library we can work on for better implementation of this feature?


def create_app():
    app = Flask(__name__)
    app.secret_key = secrets.token_hex(16)

    return app

app = create_app()

app.register_blueprint(integrate('apis.ask', "label")) #You can maybe make this look like something else, achieving the same thing.

if __name__ == "__main__":
    app.run(debug=True,)
