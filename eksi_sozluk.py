from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

#driver = webdriver.Chrome("C:/chromedriver")
driver = webdriver.Chrome(ChromeDriverManager().install())
pageCount = 1
entryCount = 1
entries = []
while pageCount <= 3:
    randomPage = random.randint(1,1290)
    driver.get("https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="+str(randomPage))
    contents = driver.find_elements_by_css_selector(".content")
    for content in contents:
        entries.append(content.text)
    pageCount = pageCount + 1
    time.sleep(1)
with open("eksi_sozluk.txt","w",encoding="UTF-8") as file:
    for entry in entries:
        file.write(str(entryCount)+".\n"+entry+"\n")
        file.write("********************\n")
        entryCount = entryCount + 1

driver.close()