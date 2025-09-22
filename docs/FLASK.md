# 🐍 What is Flask?

Flask is a **lightweight web framework in Python** that helps you build web applications and APIs. Instead of writing everything from scratch, Flask gives you the basic tools to:

- Handle **routes** (decide what happens when someone visits a URL).
- Process **requests and responses**.
- Render **HTML templates** or return data (like JSON for APIs).

It’s called a “**microframework”** because it only includes the essentials, letting you add extra features (like databases, authentication, etc.) through extensions when you need them. This makes it very flexible — you can use it for small projects, or scale it up to bigger ones.

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run()
```

- When you run this code, Flask starts a small development server.
- By default, it runs on http://127.0.0.1:5000/ → Port 5000 is Flask’s default if you don’t specify one.
- You can change the port if needed:

```python
app.run(port=8080)
```

## 🔑 Key points to remember

- Default host: 127.0.0.1 (localhost).
- Default port: 5000.
- Great for learning, prototyping, and even production (with a proper WSGI server like Gunicorn or uWSGI).

**👉 In short:**
Flask = a simple, flexible way to build web apps and APIs in Python.

---

**Resource Links:**

1. Official Documentation

    - [Flask Official Documentation](https://flask.palletsprojects.com/en/stable/) – The most authoritative and up-to-date resource. Includes Quickstart, Tutorials, and API Reference.

2. Tutorials

    - [Flask Mega-Tutorial by Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
– In-depth, step-by-step tutorial for building real Flask applications.

    - [Real Python Flask Tutorials](https://realpython.com/tutorials/flask/) – Beginner-friendly guides and projects.

    - [Corey Schafer’s Flask YouTube Series](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)
– Practical video tutorials covering Flask basics and advanced topics.

3. Interactive Learning

    - [PythonAnywhere Flask Tutorial](https://help.pythonanywhere.com/pages/Flask/)
– Hands-on deployment tutorial with live coding environment.

    - [FreeCodeCamp Flask Full Course](https://www.youtube.com/watch?v=Z1RJmh_OqeA)
– Full 4-hour video course teaching Flask from scratch.
