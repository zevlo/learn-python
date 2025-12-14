from flask import Flask, render_template, request, redirect
import string
import random
import sqlite3

app = Flask(__name__)

# Connect to the SQLite database
conn = sqlite3.connect("urls.db", check_same_thread=False)
db = conn.cursor()

# Create the URLs table if it doesn't exist
db.execute(
    """CREATE TABLE IF NOT EXISTS urls
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
               original_url TEXT NOT NULL,
               short_url TEXT NOT NULL,
               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"""
)
conn.commit()


def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = "".join(random.choice(characters) for _ in range(6))
    return short_url


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        original_url = request.form["original_url"]
        short_url = generate_short_url()

        # Insert the original and short URLs into the database
        db.execute(
            "INSERT INTO urls (original_url, short_url) VALUES (?, ?)",
            (original_url, short_url),
        )
        conn.commit()

        return render_template("index.html", short_url=short_url)

    return render_template("index.html")


@app.route("/<short_url>")
def redirect_to_url(short_url):
    # Retrieve the original URL from the database based on the short URL
    db.execute("SELECT original_url FROM urls WHERE short_url=?", (short_url,))
    result = db.fetchone()

    if result:
        original_url = result[0]
        return redirect(original_url)

    return render_template("index.html")


@app.route("/history")
def history():
    # Retrieve all URLs from the database, ordered by the most recent ones
    db.execute(
        "SELECT original_url, short_url, created_at FROM urls ORDER BY created_at DESC"
    )
    results = db.fetchall()
    return render_template("history.html", results=results)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
