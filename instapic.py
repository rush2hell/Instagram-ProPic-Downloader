from selenium import webdriver
import urllib
import urllib.request

webpage = webdriver.Chrome("Chromedriver")
username = input("Enter the Insta-id of user: ")
link = 'https://www.instagram.com/'+ username + '/'
webpage.get(link)

try:
    public = webpage.find_element_by_xpath('//img[@class="_6q-tv"]')
    link = public.get_attribute('src')
except:
    private = webpage.find_element_by_xpath('//img[@class="be6sR"]')
    link = private.get_attribute('src')
    
print("Downloading the Profile Picture.....")
path = "F:\\Projects\\My project\\Alien Brains\\Instagram PP Downloader\\pics\\"+username+".jpg"
urllib.request.urlretrieve(link, path)
print('Path where pic is stored '+path)
