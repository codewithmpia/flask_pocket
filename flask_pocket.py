from flask import Flask, g
from pocketbase import PocketBase


class FlaskPocket:
    def __init__(self, app=None):
        self.client = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        required_configs = [
            "POCKETBASE_URL", 
            "POCKETBASE_ADMIN_EMAIL", 
            "POCKETBASE_ADMIN_PASSWORD"
        ]
        
        for config in required_configs:
            app.config.setdefault(config, None)
            
            if not app.config[config]:
                raise ValueError(f"La configuration {config} est requise.")

        self.client = PocketBase(app.config["POCKETBASE_URL"])
        self.client.admins.auth_with_password(
            app.config["POCKETBASE_ADMIN_EMAIL"],
            app.config["POCKETBASE_ADMIN_PASSWORD"]
        )
        app.teardown_appcontext(self.teardown)
        app.before_request(self.before_request)

    def before_request(self):
        g.pocketbase_client = self.client

    def collection(self, name):
        return self.client.collection(name)

    def teardown(self, exception):
        g.pocketbase_client = None

def create_app():
    app = Flask(__name__)
    pocketbase = FlaskPocket(app)
    app.pocketbase_client = pocketbase
    return app