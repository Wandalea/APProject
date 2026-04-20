from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_session import Session
import os

app = Flask(__name__)


app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = "filesystem"
Session(app)

file_save_location = "static/images"

def session_storage():
    if "crystals" not in session:
        session["crystals"] = []
    if "next_crystal" not in session:
        session["next_crystal"] = 1

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    session_storage()

    if request.method == "POST":
        crystal_name = request.form["name"]
        crystal_description = request.form["description"]
        crystal_image = request.files["image"]
        crystal_category = request.form["category"]

        filename = crystal_image.filename
        filepath = os.path.join(file_save_location, filename)
        crystal_image.save(filepath)

        new_crystal = {
            "id": session["next_crystal"],
            "name": crystal_name,
            "description": crystal_description,
            "image": filename,
            "category": crystal_category
        }

        crystals = session["crystals"]
        crystals.append(new_crystal)
        session["crystals"] = crystals
        session["next_crystal"] = session["next_crystal"] +1
        
        return redirect(url_for("category_page", category_name =crystal_category))
    return render_template("insert.html")



@app.route('/categories')
def categories():
    session_storage()

    crystalTypes = [
        {
            "name": "Raw Crystals",
            "description": "Natural and unpolished crystals",
            "image" : "rawCrystals.jpg",
            "crystals" : ["Raw Amethyst", "Raw Quartz"]
        },
        {
            "name": "Tumbled Crystals",
            "description": "Smooth polished pocket crystals",
            "image": "tumbledCrystals.jpg",
            "crystals" : ["Tumbled Rose Quartz", "Tumbled Obsidian"]
        },
        {
            "name": "Crystal Towers",
            "description": "Pointed standing crystal pieces",
            "image": "towerCrystals.jpg",
            "crystals" : ["Selenite Tower", "Obsidian Tower", "Amethyst Tower"]
        },
        {
            "name": "Carved Crystals",
            "description": "Hand carved crystal pieces",
            "image": "carvedCrystals.jpg",
            "crystals" : ["Amazonite Cat", "Aquamarine Dog"]
        },
        {
            "name": "Crystal Hearts",
            "description": "Heart shaped crystal pieces",
            "image": "heartCrystals.jpg",
            "crystals" : ["Axinite Heart", "Black Moonstone Heart"]
        },
        {
            "name": "Crystal Clusters",
            "description": "Grouped crystal pieces",
            "image": "clusterCrystals.jpg",
            "crystals" : ["Blue Aragonite Cluster", "Black Tourmaline Cluster"]
        },
    ]
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