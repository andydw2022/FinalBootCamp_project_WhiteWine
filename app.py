from flask import Flask, render_template, redirect
#from flask_pymongo import PyMongo
import new_wine_predictor

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/internetspeeds"
# mongo = PyMongo(app)


@app.route("/")
def index():
    #scrape_data.scrape_info()
    #internet_data = mongo.db.countryspeed.find_one()
    return render_template("index.html")

@app.route("/predict_new_wine")
def predict_new_wine():
    new_wine_predictor
    return render_template("predict_new_wine.html")

@app.route("/tableau_viz1")
def tableau_viz():
     return render_template("tableau_viz1.html")

@app.route("/tableau_viz2")
def tableau_viz2():
     return render_template("tableau_viz2.html")

@app.route("/tableau_viz3")
def tableau_viz3():
     return render_template("tableau_viz3.html")


if __name__ == "__main__":
    app.run(debug=True)

