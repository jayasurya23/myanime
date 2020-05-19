import bs4
import lxml.html
from selenium.common.exceptions import NoSuchElementException
from lxml import etree
from selenium import webdriver
import selenium
import requests
import csv
names=[]
data={}
# res=requests.get('https://myanimelist.net/people/118/Hiroshi_Kamiya')
driver = webdriver.Chrome(executable_path=r'C:\Users\bsury\Downloads\chromedriver.exe')
driver.get("https://myanimelist.net/animelist/animefankitty?status=7")
artist="Ak"
i=2
while(True):
    try:
        t2 = driver.find_element_by_xpath('/html/body/div[3]/div[4]/div/table/tbody['+str(i)+']/tr[1]/td[4]/a')
        names.append(t2.text)
        i+=1
    except NoSuchElementException:
        break
print("-------------------------------------------------------------")
w = csv.writer(open(artist+".csv", "w",encoding="utf-8"))
for x in names:
    w.writerow([x])
driver.close()
# w = csv.writer(open("products.csv", "w"))
# for key, val in total_d.items():
#     
# tit=soup.find_all()
# # print(tit)
# for i in tit:
#     print(i.text)