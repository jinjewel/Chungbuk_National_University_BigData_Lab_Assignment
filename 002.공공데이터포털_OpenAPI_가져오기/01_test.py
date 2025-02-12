from urllib.request import urlopen
from bs4 import BeautifulSoup # bs4 설치 필요
import time
import requests # requests 설치 필요
import sys

# url = "http://apis.data.go.kr/1390802/AgriWeather/WeatherObsrInfo/GnrlWeather/getWeatherTimeList?serviceKey=*****&Page_No=1&Page_Size=20&search_Year=2024&date_Time=2018-01-01&obsr_Spot_Nm=성주군 대가면&obsr_Spot_Code=719862A001"
# response = urlopen(url)
# soup = BeautifulSoup(response, 'html.parser')
# for data in soup.find_all('span'):
#     print(data.get('class'))

# url = 'http://apis.data.go.kr/1390802/AgriWeather/WeatherObsrInfo/GnrlWeather/getWeatherTenMinList'
# params ={'serviceKey' : '*****', 'Page_No' : '1', 'Page_Size' : '20', 'date' : '2018-01-01', 'time' : '1300', 'obsr_Spot_Nm' : '성주군 대가면', 'obsr_Spot_Code' : '719862A001' }

# response = requests.get(url, params=params).text

# # response = urlopen('http://apis.data.go.kr/1390802/AgriWeather/WeatherObsrInfo/GnrlWeather/getWeatherTimeList?serviceKey=*****&Page_No=1&Page_Size=20&search_Year=2024&date_Time=2018-01-01&obsr_Spot_Nm=%EC%84%B1%EC%A3%BC%EA%B5%B0%20%EB%8C%80%EA%B0%80%EB%A9%B4&obsr_Spot_Code=719862A001')


response = urlopen('https://www.naver.com/')

soup = BeautifulSoup(response, 'html.parser')
for data in soup.select("span.service_name"):
    print(data)

# response = requests.get(url)

# if response.status_code == 200:
#     print("scuss                            dfdf1111111111111111111111111111111")
#     # HTML 코드를 가져온다
#     html = response.text
#     soup = BeautifulSoup(html, 'html.parser')
    
#     # ----태그를 모두 찾음
#     a = soup.find_all('div',{'class':'html-tag'})
    
#     for i in a:
#         print(i.get_text(),end="\n")
# else:
#     print("error22222222222222222222222222222222")



