import time
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
from selenium import webdriver
import requests as req
from splinter import browser
from selenium import webdriver


def scrape():
    url = "https://mars.nasa.gov/news/"
    response = req.get(url)
    soup = bs(response.text, 'html5lib')


    news_title = soup.find("div", class_="content_title").text
    paragraph_text = soup.find("div", class_="rollover_description_inner").text




    executable_path = {'executable_path' : 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)


    html = browser.html
    soup = bs(html, "html.parser")


    browser.click_link_by_partial_text('FULL IMAGE')


    browser.click_link_by_partial_text('more info')


    new_html = browser.html
    new_soup = bs(new_html, 'html.parser')
    temp_img_url = new_soup.find('img', class_='main_image')
    back_half_img_url = temp_img_url.get('src')

    recent_mars_image_url = "https://www.jpl.nasa.gov" + back_half_img_url


    twitter_response = req.get("https://twitter.com/marswxreport?lang=en")
    twitter_soup = bs(twitter_response.text, 'html.parser')


    tweet_containers = twitter_soup.find_all('div', class_="js-tweet-text-container")
    for i in range(10):
        tweets = tweet_containers[i].text
        if "Sol " in tweets:
            mars_weather = tweets
            break


    request_mars_space_facts = req.get("https://space-facts.com/mars/")


    mars_space_table_read = pd.read_html(request_mars_space_facts.text)
    df = mars_space_table_read[0]


    df.set_index(0, inplace=True)
    mars_data_df = df


    mars_data_html = mars_data_df.to_html()
    mars_data_html.replace('\n', '')
    mars_data_df.to_html('mars_table.html')


    usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    usgs_req = req.get(usgs_url)




    soup = bs(usgs_req.text, "html.parser")
    hemi_attributes_list = soup.find_all('a', class_="item product-item")

    hemisphere_image_urls = []
    for hemi_img in hemi_attributes_list:
        
        img_title = hemi_img.find('h3').text
        print(img_title)
        link_to_img = "https://astrogeology.usgs.gov/" + hemi_img['href']
        print(link_to_img)
        img_request = req.get(link_to_img)
        soup = bs(img_request.text, 'lxml')
        img_tag = soup.find('div', class_='downloads')
        img_url = img_tag.find('a')['href']
        hemisphere_image_urls.append({"Title": img_title, "Image_Url": img_url})

    mars_data = {
     "News_Title": news_title,
     "Paragraph_Text": paragraph_text,
     "Most_Recent_Mars_Image": recent_mars_image_url,
     "Mars_Weather": mars_weather,
     "mars_h": hemisphere_image_urls
     }

    return mars_data
