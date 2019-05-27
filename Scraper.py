import requests
import pymongo
from pymongo import MongoClient
from selenium import webdriver
com_list = dict()

client = MongoClient("mongodb+srv://florent:<Montali007>@jdscrawler-hpmbd.azure.mongodb.net/test?retryWrites=true")
db = client.test

driver = webdriver.Chrome(executable_path ='C:\driver\chromedriver.exe')
driver.get("https://item.jd.com/1384071.html")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver.implicitly_wait(5)
driver.execute_script("window.scrollBy(500,document.body.scrollHeight)")
comment_name = driver.find_element_by_class_name('user-info').text
com_list = {'User_name' : comment_name}
comment_date = driver.find_element_by_class_name('order-info').text
com_list = {'Order_date' : comment_date}
comment_txt = driver.find_element_by_class_name('comment-con').text
com_list = {'Comments' : comment_txt}

print(com_list)
# comment_star = driver.find_element_by_css_selector('class="comment-star"').get_attribute('star')



# print(comment_txt)



# for com in comment_txt:
#     com_list.append(comment_txt.text)
# print (com_list)



driver.close()

# result = open('sc-result.txt', 'w+'/)
# for obj in comment_txt:
#     result.write(obj.text)