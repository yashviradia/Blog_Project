from flask import Flask, render_template
import requests


app = Flask(__name__)

blog_url = "https://api.npoint.io/8c8cb60a3116ae7e94ed"
response = requests.get(url=blog_url)
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/blog/<id>")
def get_complete_post(id):
    print(id)
    return render_template("post.html", post_=all_posts[int(id) - 1])


if __name__ == "__main__":
    app.run(debug=True)
