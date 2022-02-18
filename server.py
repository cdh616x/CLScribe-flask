from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/review", methods=["post"])
def review():
    x = request.form["filename"]
    y = request.form["greeting"]
    z = request.form["opening"]
    a = request.form["closing"]
    document_components = [y, z, a]
    with open("./output/" + x + ".txt", "w") as letter:
        for component in document_components:
            letter.write(component + "\n\n")
    return render_template("review.html", greeting=y, opening=z, closing=a)


if __name__ == "__main__":
    app.run(debug=True)