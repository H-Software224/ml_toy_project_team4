import matplotlib.pyplot as plt
from matplotlib import rc
import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

plt.rcParams["axes.unicode_minus"] = False
rc("font", family="Malgun Gothic")
url = "https://www.starbucks.co.kr/store/store_map.do"
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get(url)

location_button = driver.find_element(By.CSS_SELECTOR, value='#container > div > form > fieldset > div > section > article.find_store_cont > article > header.loca_search > h3 > a')
location_button.click()
time.sleep(3)
seoul_choice = driver.find_element(By.CSS_SELECTOR, value='#container > div > form > fieldset > div > section > article.find_store_cont > article > article:nth-child(4) > div.loca_step1 > div.loca_step1_cont > ul > li:nth-child(1) > a')
seoul_choice.click()
time.sleep(3)
whole = driver.find_element(By.CSS_SELECTOR, value='#mCSB_2_container > ul > li:nth-child(1) > a')
whole.click()

req = driver.page_source
soup = BeautifulSoup(req, "html.parser")
content = soup.find("ul", "quickSearchResultBoxSidoGugun")
contents = content.find_all("li")
starbucks_list = []
for li in contents:
    name = li.find("strong").text.strip()
    address = li.find("p").text.strip().replace("1522-3232", "")
    each = {
        "매장이름" : name,
        "주소" : address,
        "브랜드" : "스타벅스"
    }
    starbucks_list.append(each)

print(len(starbucks_list))
driver.quit()
df_starbucks = pd.DataFrame(starbucks_list)
print(df_starbucks.head(10))