# Import Dependecies 
from bs4 import BeautifulSoup 
from splinter import Browser
import pandas as pd 
import requests 

# Initialize browser

def init_browser(): 
    executable_path = {'executable_path': r"C:\Users\Sisay\Documents\chromedriver.exe"}
    return Browser('chrome', **executable_path, headless=True)

# Nasa Mars News
def scrape_mars_news():
    # Initializing the browser 
    browser = init_browser()
    # Visit Nasa news url 
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # HTML Object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve the latest element that contains news title and news_paragraph
    news_title = soup.find('div', class_ = "content_title").text
    news_para = soup.find('div', class_='article_teaser_body').text

    browser.quit()
    return [news_title, news_para]


# Featured images
def scrape_mars_image():
    # Initialize browser 
    browser = init_browser()

    #  Mars Space images using splinter module
    image_url_featured = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url_featured) 

    # HTML Object 
    html_image = browser.html

    # Parse html using Beautiful Soup
    soup = BeautifulSoup(html_image, 'html.parser')

    # Background image of Nasa website using url
    featured_image  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

    # Website Url 
    url = 'https://www.jpl.nasa.gov'

    # Connection  website url with scrapped route
    featured_image_url = url + featured_image

    # Full link to featured image
    #featured_image_url
    browser.quit()
    return featured_image_url

# Mars Weather 
def scrape_mars_weather():
    # Initialize browser 
    browser = init_browser()
    
    # Visit Mars Weather Twitter through splinter module
    weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)

    # HTML Object 
    html_weather = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html_weather, 'html.parser')

    # Find all elements that contain tweets
    latest_tweets = soup.find_all('div', class_='js-tweet-text-container')

    # Retrieving news title  and displaying weather info
    for tweet in latest_tweets: 
        weather_tweet = tweet.find('p').text
        if 'Sol' and 'pressure' in weather_tweet:
            print(weather_tweet)
            break
        else: 
            pass
    browser.quit()
    return weather_tweet

# +
# Mars Facts
def scrape_mars_facts():
# Visit Mars facts url 
    facts_url = 'http://space-facts.com/mars/'
    # Use Panda's `read_html` to parse the url
    mars_facts = pd.read_html(facts_url)
    # Find the mars facts DataFrame in the list of DataFrames as assign it to `mars_df`
    mars_df = mars_facts[0]
    # Assign the columns `['Description', 'Value']`
    mars_df.columns = ['Description','Value']
    # Set the index to the `Description` column without row indexing
    mars_df.set_index('Description', inplace=True)
    # Save html code to folder Assets
    data = mars_df.to_html()
    return data


# Mars Hemispheres 
def scrape_mars_hemispheres():
    #Initialize browser 
    browser = init_browser()
    #Visit hemispheres website through splinter module 
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)
    # HTML Object
    html_hemispheres = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html_hemispheres, 'html.parser')
    # Retreive all items that contain mars hemispheres information
    items = soup.find_all('div', class_='item')
    # Create empty list for hemisphere urls 
    hemis = []
    # Store the main_ul 
    hemispheres_main_url = 'https://astrogeology.usgs.gov' 
    # Loop through the items previously stored
    for i in items: 
        # Store title
        title = i.find('h3').text
        # Store link to a full image website
        partial_img_url = i.find('a', class_='itemLink product-item')['href']
        # Visit the link that contains the full image website 
        browser.visit(hemispheres_main_url + partial_img_url)
        # HTML Object of all hemisphere information  
        partial_img_html = browser.html
        # Parse HTML with Beautiful Soup for every individual hemisphere information website 
        soup = BeautifulSoup( partial_img_html, 'html.parser')
        # Retrieve full image s
        img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
        # Append the retreived information into a list of dictionaries 
        hemis.append({"title" : title, "img_url" : img_url})

    # Return mars_data dictionary 
    browser.quit()
    return hemis
