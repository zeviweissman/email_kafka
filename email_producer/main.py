from flask import Flask
from routes.email_routes import email_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(email_blueprint, url_prefix="/api/email")
    return app



if __name__ == '__main__':
    app = create_app()
    app.run()