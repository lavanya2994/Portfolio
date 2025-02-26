from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        print(f"Received message from {name} ({email}): {subject} - {message}")
        return "Your message has been sent. Thank you!"
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
