# Flask Pocket

FlaskPocket is a Flask extension that integrates PocketBase, a backend service.

## Prerequisites

- [PocketBase](https://pocketbase.io/)
- [PocketBase Python SDK](https://github.com/vaphes/pocketbase)

## Installation

```bash
pip install flask-pocket
```

Or install from the cloned repository:

```bash
git clone https://github.com/codewithmpia/flask_pocket.git
cd flask_pocket
pip install .
```

## Configuration

Add the following configurations to your Flask app:

```python
app.config["POCKETBASE_URL"] = "your_pocketbase_url"
app.config["POCKETBASE_ADMIN_EMAIL"] = "your_admin_email"
app.config["POCKETBASE_ADMIN_PASSWORD"] = "your_admin_password"
```

## Usage

```python
from flask import Flask
from flask_pocket import FlaskPocket

app = Flask(__name__)

app.config["POCKETBASE_URL"] = "your_pocketbase_url"
app.config["POCKETBASE_ADMIN_EMAIL"] = "your_admin_email"
app.config["POCKETBASE_ADMIN_PASSWORD"] = "your_admin_password"
pocket = FlaskPocket(app)
```

## Queries

### Get All Objects

```python
try:
    posts = pocket.collection("posts").get_full_list()
except pocket.ClientResponseError as e:
    # Handle error
    print(f"Error: {e}")
```

### Get One Object

```python
try:
    post = pocket.collection("posts").get_one(post_id)
    # Generate image url
    image_url = pocket.client.get_file_url(post, post.image)
except pocket.ClientResponseError as e:
    # Handle error
    print(f"Error: {e}")
```

### Create

```python
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
```

### Edit

```python
try:
    pocket.collection("contacts").update(contact_id, {
        "name": new_name,
        "email": new_email,
        "message": new_message
    })
except pocket.ClientResponseError as e:
    # Handle error
    print(f"Error: {e}")
```

### Delete

```python
try:
    pocket.collection("contacts").delete(contact_id)
except pocket.ClientResponseError as e:
    # Handle error
    print(f"Error: {e}")
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions

Contributions are welcome.

