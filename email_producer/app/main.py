from flask import Flask
from email_kafka.email_producer.app.routes.email_routes import email_blueprint
from dotenv import load_dotenv

load_dotenv(verbose=True)

def create_app():
    app = Flask(__name__)
    app.register_blueprint(email_blueprint, url_prefix="/api/email")
    return app



if __name__ == '__main__':
    app = create_app()
    app.run()