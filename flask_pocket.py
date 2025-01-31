from flask import Flask, g
from pocketbase import PocketBase
from pocketbase.errors import ClientResponseError


class FlaskPocket:
    """
    FlaskPocket is an extension for Flask that integrates PocketBase, a backend service.
    
    Attributes:
        client (PocketBase): The PocketBase client instance.
        ClientResponseError (Exception): The exception class for handling client response errors.
    
    Example:
    from flask import Flask
    from flask_pocket import FlaskPocket

    app = Flask(__name__)

    app.config["POCKETBASE_URL"] = "your_pocketbase_url"
    app.config["POCKETBASE_ADMIN_EMAIL"] = "your_admin_email"
    app.config["POCKETBASE_ADMIN_PASSWORD"] = "your_admin_password"
    pocket = FlaskPocket(app)

    Queries:

    1. GET ALL OBJECTS
        try:
            posts = pocket.collection("posts").get_full_list()
        except pocket.ClientResponseError as e:
            # Handle error
            print(f"Error: {e}")

    2. GET ONE OBJECT
        try:
            post = pocket.collection("posts").get_one(post_id)
            # Generate image url
            image_url = pocket.client.get_file_url(post, post.image)
        except pocket.ClientResponseError as e:
            # Handle error
            print(f"Error: {e}")

    3. CREATE 
        try:
            pocket.collection("contacts").create({
                "name": name,
                "email": email,
                "message": message
            })
            return redirect(url_for("contact"))
        except pocket.ClientResponseError as e:
            # Handle error
            print(f"Error: {e}")

    4. EDIT
        try:
            pocket.collection("contacts").update(contact_id, {
                "name": new_name,
                "email": new_email,
                "message": new_message
            })
        except pocket.ClientResponseError as e:
            # Handle error
            print(f"Error: {e}")

    5. DELETE
        try:
            pocket.collection("contacts").delete(contact_id)
        except pocket.ClientResponseError as e:
            # Handle error
            print(f"Error: {e}")
    """
    def __init__(self, app=None):
        self.client = None
        # Rendre l'exception accessible
        self.ClientResponseError = ClientResponseError  
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