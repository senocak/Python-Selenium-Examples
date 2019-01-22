from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

#driver = webdriver.Chrome("/opt/lampp/htdocs/Python-Selenium-Examples/chromedriver.exe") 
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://twitter.com/login")

username_input = driver.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input")
#The Reason why xpath is used because there are 3 session[username_or_email] class name
username_input.clear()
username_input.send_keys("your_username")

password_input = driver.find_element_by_class_name("js-password-field")
password_input.clear()
password_input.send_keys("your_password")

login_button = driver.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/button")
login_button.click()

time.sleep(1)

search_input = driver.find_element_by_id("search-query")
search_input.send_keys("#yazilimayolver")

search_button = driver.find_element_by_xpath("//*[@id='global-nav-search']/span/button")
search_button.click()

time.sleep(1)

lenOfPage = driver.execute_script("window.scrollTo(0 ,document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(2)
    lenOfPage=driver.execute_script("window.scrollTo(0 ,document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
    if lastCount == lenOfPage:
        match=True

tweets_list = []
tweets = driver.find_elements_by_css_selector(".TweetTextSize.js-tweet-text.tweet-text")
for tweet in tweets:
    tweets_list.append(tweet.text)

tweet_count = 1
with open("twitter.txt","w",encoding="UTF-8") as file:
    for tweet in tweets_list:
        file.write(str(tweet_count)+".\n"+tweet+"\n")
        file.write("-----------------------------\n")
        tweet_count += 1

time.sleep(2)

like_buttons = driver.find_elements_by_css_selector(".ProfileTweet-actionButton.js-actionButton.js-actionFavorite")
#like_buttons = driver.find_elements_by_css_selector(".ProfileTweet-actionCountForPresentation")

for like_button in like_buttons:
    try:
        like_button.click()
        time.sleep(1)
    except Exception:
        print("--------Hata----------")

driver.close()