# Import Dependencies 
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars
import os
import pymongo

# Create an instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection locally 
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
# connect to a database
db = client.mars_app

#Drop collection if avaible to remove duplates 
#db.mars_info.drop()

@app.route("/")
def index(): 
    # Return template and data
    # Find data
    mars_info_data = db.mars.find_one()
    return render_template("index.html", mars_info=mars_info_data)

@app.route("/scrape")
def scrape():
    try:
        mars_news = scrape_mars.scrape_mars_news()
        mars_image = scrape_mars.scrape_mars_image()
        mars_facts = scrape_mars.scrape_mars_facts()
        mars_weather = scrape_mars.scrape_mars_weather()
        data = scrape_mars.scrape_mars_facts()
        mars_hemispheres = scrape_mars.scrape_mars_hemispheres()   

        # Create Mission to Mars dictionary, which will be imported into Mongo
        mars_info = {}   

        # Dictionary entry from MARS NEWS
        mars_info['news_title'] = mars_news[0]
        mars_info['news_paragraph'] = mars_news[1]
        # Dictionary entry from fetured image created in line 14
        mars_info['featured_image_url'] = mars_image 
        # Dictionary entry from Weather twitts 
        mars_info['weather_tweet'] = mars_weather
        # Dictionary entry from MARS FACTS
        mars_info['mars_facts'] = data
        mars_info['hiu'] = mars_hemispheres

        db.mars.update({}, mars_info, upsert=True)
        mars_info_data = db.mars.find_one()
    except:
        mars_info_data = db.mars.find_one() 

    return render_template("index.html", mars_info=mars_info_data)

if __name__ == "__main__": 
    app.run(debug=False)