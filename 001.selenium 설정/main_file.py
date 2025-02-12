from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options # 창 닫힘 방지
import requests

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

url='http://apis.data.go.kr/1390802/AgriWeather/WeatherObsrInfo/GnrlWeather/getWeatherTimeList?serviceKey=*****&Page_No=1&Page_Size=20&search_Year=2024&date_Time=2018-01-01&obsr_Spot_Nm=성주군 대가면&obsr_Spot_Code=719862A001'
# url = 'http://apis.data.go.kr/1390802/AgriWeather/WeatherObsrInfo/GnrlWeather/getWeatherTimeList'
# params ={'serviceKey' : '*****', 'Page_No' : '1', 'Page_Size' : '24', 'date_Time' : '2018-01-01', 'obsr_Spot_Nm' : '성주군 대가면', 'obsr_Spot_Code' : '719862A001' }
# response = requests.get(url, params=params)


driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

for data in driver.find_elements("span", {"class":"html-tag"}):
    print(data)

# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
    
driver.close()