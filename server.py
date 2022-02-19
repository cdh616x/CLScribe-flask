from flask import Flask, render_template, request
from docx import Document
import smtplib




app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/review", methods=["post", "get"])
def review():
    document = Document()
    file_name = request.form["filename"].strip()
    greeting = request.form["greeting"]
    opening = request.form["opening"]
    qualifications = request.form["qualifications"]
    personal = request.form["personal"]
    closing = request.form["closing"]
    farewell = request.form["farewell"]
    document_components = [greeting, opening, qualifications, personal, closing, farewell]
    for component in document_components:
        document.add_paragraph(component)
        document.save("./static/" + file_name + "_cover_letter.docx")
    return render_template("review.html", file_name=file_name, greeting=greeting, opening=opening,
                           qualifications=qualifications, personal=personal, closing=closing, farewell=farewell, href="./static/" + file_name + "_cover_letter.docx")


if __name__ == "__main__":
    app.run(debug=True)