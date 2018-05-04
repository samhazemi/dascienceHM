from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pymongo
from pymongo import MongoClient
app = Flask(__name__)
mongo = PyMongo(app)
#conn = MongoClient('mongodb://localhost:27017/mars')
#client = pymongo.MongoClient(conn)
#db = client.mars
#mars = db.mars
#mongo = PyMongo(app)
@app.route('/')
def index():
    mars =mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route('/scrape')
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update(
        {},
        mars_data,
        upsert=True
    )
    return redirect('/', code=302)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
