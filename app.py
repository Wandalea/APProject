from flask import Flask, render_template, request, redirect, url_for, session
# from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/categories")
def categories():
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


if __name__ == "__main__":
    app.run(debug=True)