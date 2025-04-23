from flask import Flask, render_template, request, redirect, url_for, session
from utils import generate_responses

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        image_file = request.files["image"]
        image_bytes = image_file.read()

        ugly_score, roast, fortune, age_guess = generate_responses(name, image_bytes)

        # Store results in session
        session['results'] = {
            'name': name,
            'ugly_score': ugly_score,
            'roast': roast,
            'fortune': fortune,
            'age_guess': age_guess
        }

        return redirect(url_for("loading"))

    return render_template("index.html")


@app.route("/loading")
def loading():
    return render_template("loading.html")


@app.route("/result")
def result():
    data = session.get("results")
    if data:
        return render_template("result.html", **data)
    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)
