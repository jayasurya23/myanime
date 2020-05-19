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
driver.get("https://myanimelist.net/people/118/Hiroshi_Kamiya")
n= driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[1]/h1/span')
artist=n.text
t2 = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[2]/table[1]/tbody/tr[2]/td[2]/a')
i=1
while(True):
    try:
        t2 = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[2]/table[1]/tbody/tr['+str(i)+']/td[2]/a')
        t3 = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[2]/table[1]/tbody/tr['+str(i)+']/td[3]/a')
        names.append(t2.text)
        data[t2.text]=t3.text
        i+=1
    except NoSuchElementException:
        break
print(data)
print("-------------------------------------------------------------")
w = csv.writer(open(artist+".csv", "w",encoding="utf-8"))

for key, val in data.items():
    w.writerow([key, val])
driver.close()
# w = csv.writer(open("products.csv", "w"))
# for key, val in total_d.items():
#     
# tit=soup.find_all()
# # print(tit)
# for i in tit:
#     print(i.text)