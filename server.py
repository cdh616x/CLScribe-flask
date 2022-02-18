from flask import Flask, render_template, request
from docx import Document
import smtplib
import keys

document = Document()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/review", methods=["post"])
def review():
    email = request.form["email"].strip()
    file_name = request.form["filename"].strip()
    greeting = request.form["greeting"]
    opening = request.form["opening"]
    qualifications = request.form["qualifications"]
    personal = request.form["personal"]
    closing = request.form["closing"]
    farewell = request.form["farewell"]
    document_components = [greeting, opening, qualifications, personal, closing, farewell]
    # with open("./output/" + file_name + "_cover_letter.txt", "w") as letter:
    for component in document_components:
        document.add_paragraph(component)
    string_doc = str(document.save(file_name + "_cover_letter.docx"))
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="cdhprof@gmail.com", password="Lyr1c@@@")
        connection.sendmail(from_addr="cdhprof@gmail.com",
                            to_addrs=email,
                            msg=f"Subject: {file_name + '_cover_letter.docx'}\n\n{greeting + ','}\n\n{opening}\n\n{qualifications}\n\n{personal}\n\n{closing}\n\n{farewell}")
                            # msg=(f"Subject: {file_name}\n\n{document.save(file_name + '_cover_letter.docx')}"))

    #         letter.write("    " + component + "\n\n")
    return render_template("review.html", file_name=file_name, greeting=greeting, opening=opening,
                           qualifications=qualifications, personal=personal, closing=closing, farewell=farewell)


if __name__ == "__main__":
    app.run(debug=True)