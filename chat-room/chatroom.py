import datetime
import flask
import redis

app = flask.Flask("labex-sse-chat")
app.secret_key = "labex"
app.config["DEBUG"] = True
r = redis.StrictRedis()


# Home route function
@app.route("/")
def home():
    # If the user is not logged in, redirect to the login page
    if "user" not in flask.session:
        return flask.redirect("/login")
    user = flask.session["user"]
    return flask.render_template("index.html", user=user)


# Message generator
def event_stream():
    # Create a publish-subscribe system
    pubsub = r.pubsub()
    # Use the subscribe method of the publish-subscribe system to subscribe to a channel
    pubsub.subscribe("chat")
    for message in pubsub.listen():
        data = message["data"]
        if type(data) == bytes:
            yield "data: {}\n\n".format(data.decode())


# Login function, login is required for the first visit
@app.route("/login", methods=["GET", "POST"])
def login():
    if flask.request.method == "POST":
        # Store the username in the session dictionary and then redirect to the homepage
        flask.session["user"] = flask.request.form["user"]
        return flask.redirect("/")
    return flask.render_template("login.html")


# Receive data sent by JavaScript using the POST method
@app.route("/post", methods=["POST"])
def post():
    message = flask.request.form["message"]
    user = flask.session.get("user", "anonymous")
    now = datetime.datetime.now().replace(microsecond=0).time()
    r.publish("chat", "[{}] {}: {}\n".format(now.isoformat(), user, message))
    return flask.Response(status=204)


# Event stream interface
@app.route("/stream")
def stream():
    # The return object of this route function must be of type text/event-stream
    return flask.Response(event_stream(), mimetype="text/event-stream")


# Run the Flask application
app.run()
