# CS50 Week 9 - Flask

[Watch lecture on Youtube](https://youtu.be/CUIK3tKNH5E)

---

## Flask

```
from flask import Flask
```

Flask is a Python web framework built with a small core and easy-to-extend philosophy.

`app.py`\
`requirements.txt`\
`static/`\
`templates/`

## app.py

```
$ code app.py
```

`Python`

```
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
  name = request.args.get("name")
  return render_template("index.html", name=name)
```

```
$ flask run
```

`HTML`

```
...

<body>
  Hello, {{ name }}
</body>
```

> Decorator are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of function or class. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it. But before diving deep into decorators let us understand some concepts that will come in handy in learning the decorators.

## Forms

`Python - app.py`

```
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html)

@app.route("/greet")
def greet():
  name = request.args.get("name")
  return render_template("greet.html", name=name)
```

`HTML - index.html`

```
<!DOCTYPE html>
...
<body>
  <form action="/greet" method="get">
    <input autocomplete="off" name="name" placeholder="Name" text="text">
    <input type="submit">
  </form>
</body>
```

`HTML - greet.html`

```
<!DOCTYPE html>
...
<body>
  Hello, Greet {{ name }}
</body>
```

## Templates

`HTML - layout.html`

```
<!DOCTYPE html>

<html lang="en">
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello</title>
  </head>
  <body>
	  {% block body %}{% endblock %}
  </body>
</html>
```

`HTML - index.html`

```
{% extends "layout.html" %}

{% block body %}

  <form action="/greet" method="get">
    <input autocomplete="off" name="name" placeholder="Name" text="text">
    <input type="submit">
  </form>

{% endblock %}
```

`HTML - greet.html`

```
{% extends "layout.html" %}

{% block body %}

  Hello, {{ name }}

{% endblock %}
```

## GET vs. POST

`Python - app.py`

```
...

@app.route("/greet", method ["POST"])
def greet():
  name = request.args.get("name")
  return render_template("greet.html, name=name")
```

`HTML - index.html`

```
...
  <form action="/greet" method="post">
    ...
  </form>
...
```

> `method="get"` isn't private\
> `method="post"` is private\
> With `POST` you cannot cache the information entered by the user in case of page refresh.

`request.args` is for get requests\
`request.form` is for post requests

```
...

@app.route("/greet", method ["POST"])
def greet():
  name = request.form.get("name")
  return render_template("greet.html, name=name")
```

## CSS and Flask

`style.css` goes under the static folder.\

## Jinja Loops

`Python - app.py`

```
from flask import Flask, render_template, request

app = Flask(__name__)

SPORTS = [
  "Basketball"
  "Football"
  "Ultimate Frisbee"
]

@app.route("/")
def index():
  return render_template("index.html", sports=SPORTS)

@app.route("/register", method=["POST"])
def register():
  if not request.form.get("sport") or request.form.get("sport") not in SPORTS:
    return render_template("failure.html")
  elif:
    return render_template("success.html")
```

`HTML - index.html`

```
<select>
  <option disable selected>Sport</option>
    {% for sport in sports %}
      <option>{{ sport }}</option>
    {% endfor %}
</select>
```

```
{% for sport in sports %}
  <input name="sport" type="checkbox" value"{{sport}}">{{ sport }}
{% endfor %}
```

## Model

`Python - app.py`

```
from flask import Flask, render_template, request

app = Flask(__name__)

REGISTANTS = {}

SPORTS = [
  "Basketball"
  "Football"
  "Ultimate Frisbee"
]

@app.route("/")
def index():
  return render_template("index.html", sports=SPORTS)

@app.route("/register", method=["POST"])
def register():
  # Validate name
  name = request.form.get("name")
  if not name:
    return render_template("error.html", message="Missing name")

  # Validate sport
  sport = request.form.get("sport")
  if not sport:
    return render_template("error.html", message="<Missing sport")
  if sport not in SPORTS:
    return render_template("error.html", message="<Invalid sport")

  # Remember registrant
  REGISTRANTS[name] = sport

  # Confirm registrant
  return render_template("registrants.html")

```

`HTML - error.html`

```
{% extends "layout.html" %}

{% block body %}

  <h1>Error</h1>
  <p>{{ message }}</p>
  <img alt="Grumpy Cat" src="/static/cat.jpg">

{% endblock %}
```

## SQLite and FLask

`Python - app.py`

```
from flask import Flask, render_template, request

app = Flask(__name__)

db = SQL("sqlite:///registrants.db")

SPORTS = [
  "Basketball"
  "Football"
  "Ultimate Frisbee"
]

@app.route("/")
def index():
  return render_template("index.html", sports=SPORTS)

@app.route("/deregister", method=["POST"])
def deregister():
  # Forget registrant
  id = request.form.get("id")
  if id:
    db.execute("DELETE FROM registrants WHERE id = ?", id)
  return redirect("registrants.html")
```

## Email

`Python - app.py`

```
from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config["MAIL_DEFAUL_SENDER"] = os.environ["MAIL_DEFAUL_SENDER"]
app.config["MAIL_PASSWORD"] = os.environ["MAIL_PASSWORD"]
app.config["MAIL_PORT"] = 587
app.config["MAIL_SERVER"] = "smpt.gmail.com"
app.config["MAIL_USE_TILS"] = True
app.config["MAIL_USERNAME"] = os.environ["MAIL_USERNAME"]
mail = Mail(app)

...

@app.route("/register", method=["POST"])
def register():
  # Validate submission
  name = request.form.get("name")
  email = request.form.get("email")
  sport = request.form.get("sport")
  if not name or not email or sport not in SPORTS:
    return render_template("failure.html")

  # Send email
  message = Message("You are registered!", recipients=[email])
  mail.send(message)

  # Confirm registration
  return render_template("success.html")
```

## Sessions and Cookies

`Python - app.py`

```
from flask import Flask, render_template, request, session
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
  if not session.get("name"):
    return redirect/login")
  return render_template("index.html")
```

## Login

`Python - app.py`

```
...

@app.route("/login", method=["GET", "POST"])
def login():
  if request.method == "POST":
    session["name"] = request.form.get("name")
    return redirect("/")
  return render_template("login.html")

@app.route("/logout")
def logout():
  session["name"] = None
  return redirect("/")
```

`HTML - index.html`

```
{% extends "layout.html" %}

{% block body %}

  {% if session["name"] %}
    You are logged in as {{ session["name"] }}. <a href="/logout">Log out</a>
  {% else %}
    You are not logged in. <a href="/login">Log in</a>
  {% endif %}

{% endblock %}
```

## JSON

Javascript Object Notation
