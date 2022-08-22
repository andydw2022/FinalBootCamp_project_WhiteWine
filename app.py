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
    return render_template("predict_new_wine.html")

@app.route("/predict_new_wine")
def predict_new_wine():
    new_wine_predictor
    return render_template("predict_new_wine.html")

# @app.route("/map_cbs")
# def map_cbs():
#     return render_template("world_map_cbs.html")

# @app.route("/barchart")
# def barchart():
#     return render_template("barchart.html")

# @app.route("/scatterplot")
# def scatterplot():
#     return render_template("scatter_plot.html")


if __name__ == "__main__":
    app.run(debug=True)
