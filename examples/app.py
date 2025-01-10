from flask import Flask, render_template, request, redirect, url_for
from flask_pocket import FlaskPocket

app = Flask(__name__)
app.secret_key = "top secret"

app.config["POCKETBASE_URL"] = "pockect url"
app.config["POCKETBASE_ADMIN_EMAIL"] = "admin email"
app.config["POCKETBASE_ADMIN_PASSWORD"] = "admin password"
flask_pocket = FlaskPocket(app)


@app.route("/")
def index():
    posts = flask_pocket.collection("posts").get_full_list()
    return render_template("index.html", posts=posts)

@app.route("/blog/<string:post_id>/")
def post(post_id):
    post = flask_pocket.collection("posts").get_one(post_id)
    return render_template("post.html", post=post)


@app.route("/contact/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        flask_pocket.collection("contacts").create({
            "name": name,
            "email": email,
            "message": message
        })

        return redirect(url_for("contact"))
    
    
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)