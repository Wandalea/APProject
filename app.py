from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_session import Session
import os
from flask_bootstrap import Bootstrap5
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}

app = Flask(__name__)
app.secret_key = "mysecretkey123"
bootstrap = Bootstrap5(app)

app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = "filesystem"
Session(app)

file_save_location = "static/images"

def session_storage():
    if "crystals" not in session:
        session["crystals"] = []
    if "next_crystal" not in session:
        session["next_crystal"] = 1

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    session_storage()

    if request.method == "POST":
        crystal_name = request.form["name"].strip()
        crystal_description = request.form["description"].strip()
        crystal_image = request.files["image"]
        crystal_uses = request.form["uses"].strip()
        crystal_category = request.form["category"]

        valid_categories = [
            "Raw Crystals",
            "Tumbled Crystals",
            "Crystal Towers",
            "Carved Crystals",
            "Crystal Hearts",
            "Crystal Clusters"
        ]

        if crystal_name == "":
            flash("Crystal name is required.")
            return redirect(url_for("insert"))

        if len(crystal_name) < 2:
            flash("Crystal name must be at least 2 characters.")
            return redirect(url_for("insert"))

        if len(crystal_description) > 200:
            flash("Description must be 200 characters or less.")
            return redirect(url_for("insert"))

        if len(crystal_uses) > 100:
            flash("Uses must be 100 characters or less.")
            return redirect(url_for("insert"))

        if crystal_category not in valid_categories:
            flash("Invalid category selected.")
            return redirect(url_for("insert"))

        if not crystal_image or crystal_image.filename == "":
            flash("Please upload an image.")
            return redirect(url_for("insert"))

        if not allowed_file(crystal_image.filename):
            flash("Only PNG, JPG, JPEG, and WEBP image files are allowed.")
            return redirect(url_for("insert"))

        filename = secure_filename(crystal_image.filename)
        filepath = os.path.join(file_save_location, filename)
        crystal_image.save(filepath)

        new_crystal = {
            "id": session["next_crystal"],
            "name": crystal_name,
            "description": crystal_description,
            "image": filename,
            "uses": crystal_uses,
            "category": crystal_category
        }

        crystals = session["crystals"]
        crystals.append(new_crystal)
        session["crystals"] = crystals
        session["next_crystal"] += 1
        
        return redirect(url_for("category_page", category_name =crystal_category))
    return render_template("insert.html")

@app.route("/remove", methods=["GET", "POST"])
def remove():
    session_storage()

    if request.method == "POST":
        crystal_name = request.form["name"]
        crystal_category = request.form["category"]
        updated_crystals = []

        for crystal in session["crystals"]:
            if not (crystal["name"].lower() == crystal_name.lower()
                    and crystal["category"].lower() == crystal_category.lower()):
                updated_crystals.append(crystal)
        session["crystals"] = updated_crystals

        return redirect(url_for("category_page", category_name= crystal_category))
    return render_template("remove.html")

@app.route('/categories')
def categories():
    session_storage()

    if "crystalTypes" not in session:

        session["crystalTypes"] = [
            {
                "name": "Raw Crystals",
                "description": "Natural and unpolished crystals",
                "image" : "rawCrystals.jpg",
                "uses" : "",
            },
            {
                "name": "Tumbled Crystals",
                "description": "Smooth polished pocket crystals",
                "image": "tumbledCrystals.jpg",
                "uses" : "",
            },
            {
                "name": "Crystal Towers",
                "description": "Pointed standing crystal pieces",
                "image": "towerCrystals.jpg",
                "uses" : "",
                
            },
            {
                "name": "Carved Crystals",
                "description": "Hand carved crystal pieces",
                "image": "carvedCrystals.jpg",
                "uses" : "",
                
            },
            {
                "name": "Crystal Hearts",
                "description": "Heart shaped crystal pieces",
                "image": "heartCrystals.jpg",
                "uses" : "",
                
            },
            {
                "name": "Crystal Clusters",
                "description": "Grouped crystal pieces",
                "image": "clusterCrystals.jpg",
                "uses" : "",
                
            },
        ]
    crystalTypes = session["crystalTypes"]

    return render_template("categories.html", crystalTypes=crystalTypes)


@app.route("/category/<category_name>")
def category_page(category_name):
    session_storage()

    organized_crystals = []
    for crystal in session["crystals"]:
        if crystal["category"] == category_name:
            organized_crystals.append(crystal)

    return render_template("category_page.html", category_name=category_name, crystals= organized_crystals)


if __name__ == "__main__":
    app.run(debug=True)