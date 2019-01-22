from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import urllib.request

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.instagram.com/accounts/login/")

time.sleep(1)

username_input = driver.find_element_by_name("username")
username_input.clear()
username_input.send_keys("your_username")

password_input = driver.find_element_by_name("password")
password_input.clear()
password_input.send_keys("your_password")

login_button = driver.find_element_by_xpath("//*[@type='submit' and contains(text(), 'Log in')]")
login_button.click()
time.sleep(1)

driver.get("https://www.instagram.com/baris_askin")
images = driver.find_elements_by_tag_name('img')
i = 0 
for image in images:
    i = i + 1
    print(image.get_attribute('src'))
    urllib.request.urlretrieve(image.get_attribute('src'), "instagram_images/"+str(i)+".jpg")

time.sleep(1)

driver.close()







"""
notifications_button = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[3]/button[2]")
notifications_button.click()
profile_button = driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[3]/a/span")
profile_button.click()
time.sleep(1)
followers_button = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
followers_button.click()
time.sleep(2)
lenOfPage = driver.execute_script("followers = document.querySelector('.isgrP'); followers.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = driver.execute_script("followers = document.querySelector('.isgrP'); followers.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            match=True
"""