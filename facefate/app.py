from flask import Flask, render_template, request
from utils import generate_responses

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        image_file = request.files["image"]
        image_bytes = image_file.read()

        ugly_score, roast, fortune, age_guess = generate_responses(name, image_bytes)

        return render_template("result.html", name=name,
                               ugly_score=ugly_score,
                               roast=roast,
                               fortune=fortune,
                               age_guess=age_guess)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
