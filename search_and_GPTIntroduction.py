# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 14:03:54 2025

@author: Lenovo
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 20:17:03 2024

@author: cyq
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import os



# 创建 Chrome 浏览器实例
driver = webdriver.Chrome()

# 访问目标 URL
original_paper='A Division Inhibitor and a Topological Specificity Factor Coded for by the Minicell Locus Determine Proper Placement of the Division Septum in E. coli'.replace(' ', '-')
url='https://www.connectedpapers.com/main/d1bee751a0b97a53f9fe968dcaa3ac31d2e2a98f/'+original_paper+'/list'
url='https://www.connectedpapers.com/main/e19ec3ca9c8c5b95fc5c772f4a6bd23d1f5c2e5b/Mapping-the-MinE-Site-Involved-in-Interaction-with-the-MinD-Division-Site-Selection-Protein-of-Escherichia-coli/graph'
print(url)
driver.get(url)
driver.maximize_window()
# 等待页面完全加载
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.searchable-text')))

# 获取完整的页面内容
html_content = driver.page_source
# print(html_content)

titles=[]
links=[]
abstracts=[]

d = driver.find_element(By.XPATH,'//*[@id="desktop-app"]/div[2]/div[4]/div[1]/div/div[2]/div/div[1]/div[2]/h5/div')
print(d.text)
d.click()
d1 = driver.find_element(By.XPATH,'//*[@id="desktop-app"]/div[2]/div[4]/div[3]/div/div[2]/div[1]/div/a')
print('标题：',d1.text)
d_href = ''
for i in range(1,5):
    d2 = driver.find_element(By.XPATH,'//*[@id="desktop-app"]/div[2]/div[4]/div[3]/div/div[2]/div[5]/a['+str(i)+']')
    d_href = d2.get_attribute('href')
    if 'scholar.google' in d_href:
        break
print('链接：',d_href)
d3 = driver.find_element(By.XPATH,'//*[@id="desktop-app"]/div[2]/div[4]/div[3]/div/div[2]/div[6]')
print('内容：',d3.text)

time.sleep(1)

w = driver.find_elements(By.XPATH,'//*[@id="desktop-app"]/div[2]/div[4]/div[1]/div/div[2]/div/div[2]/div/div[1]/h5/div')
for x in w:
    x.click()
    d1 = driver.find_element(By.XPATH, '//*[@id="desktop-app"]/div[2]/div[4]/div[3]/div/div[2]/div[1]/div/a')
    print('标题：',d1.text)
    titles.append(d1.text)
    d_href = ''
    for i in range(1, 10):
        d2 = driver.find_element(By.XPATH,
                                 '//*[@id="desktop-app"]/div[2]/div[4]/div[3]/div/div[2]/div[5]/a[' + str(i) + ']')
        d_href = d2.get_attribute('href')
        if 'scholar.google' in d_href:
            break
    print('链接：',d_href)
    links.append(d_href)
    d3 = driver.find_element(By.XPATH, '//*[@id="desktop-app"]/div[2]/div[4]/div[3]/div/div[2]/div[7]')
    print('内容：',d3.text)
    abstracts.append(d3.text)
    time.sleep(1)
time.sleep(5)

#
# 关闭浏览器
driver.quit()
abstracts_text=''
for i in abstracts:
    abstracts_text=abstracts_text+i

import os
import openai

# optional; defaults to `os.environ['OPENAI_API_KEY']`
openai.api_key = "sk-2lGE4Dgf3WxmEaCtC47330EfB03242F98dB3828147EaA35f"

# all client options can be configured just like the `OpenAI` instantiation counterpart
openai.base_url = "https://free.v36.cm/v1/"
openai.default_headers = {"x-foo": "true"}
prompt='please write a introduction of the area refering all the abstracts：'+abstracts_text
role='user'

completion = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": role,
            "content": prompt,
        },
    ],
)

output=completion.choices[0].message.content
print('introduction:'+output+'\n')