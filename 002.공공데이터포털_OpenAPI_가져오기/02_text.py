from urllib.request import urlopen
from bs4 import BeautifulSoup # bs4 설치 필요
import requests # requests 설치 필요
import re

# URL 전체로 사용
# url='http://apis.data.go.kr/1390802/AgriWeather/WeatherObsrInfo/GnrlWeather/getWeatherTimeList?serviceKey=*****&Page_No=1&Page_Size=20&search_Year=2024&date_Time=2018-04-08&obsr_Spot_Nm=성주군 대가면&obsr_Spot_Code=719862A001'
# response = urlopen(url)

url = 'http://apis.data.go.kr/1390802/AgriWeather/WeatherObsrInfo/GnrlWeather/getWeatherTimeList'
params ={'serviceKey' : '*****', 'Page_No' : '1', 'Page_Size' : '24', 'date_Time' : '2018-01-02', 'obsr_Spot_Nm' : '성주군 대가면', 'obsr_Spot_Code' : '719862A001' }
response = requests.get(url, params=params)
print(response.text)

# if response.status_code == 200: # 페이지가 잘 불러왔는지 확인 , 200이면 성공
#     soup = BeautifulSoup(response.text, "html.parser") # 파서의 종류, html.parser, lxml, html5lib
#     print(soup)
    
# else : # 페이지가 잘 안 불러지면
#     print("\n웹 페이지를 불러오는데 오류가 생성되었습니다. \n")

# soup = BeautifulSoup(response.text, "html.parser")
# box1 = soup.find("div", {"class":"header"}).find("span").text
# print(box1)
# # box2 = box1.find("div", {"class":"opened"})
# # box3 = box2.find_all("div", {"class":"line"})[1]
# # box4= box3.find("span").text
# # print(box4)

# # 문자열 자르기(예시-미완성)
#     print(data)
#     try:
#         found = re.search("<date>(.+?)</date>", data).group(1)
#         print(found)
#     except AttributeError:
#         pass



# # 날짜 설정하기 (예시-완성) (단, 16년 24년도 2월은 29일까지 있음)
# for num_year in range(2015, 2025): # 년도 설정
#     for num_month in range(1, 13): # 월 설정
#         if num_month == 1 or num_month == 3 or num_month == 5 or num_month == 7 or num_month == 8 or num_month == 10 or num_month == 12:
#             max_day = 31
#         elif num_month == 2:
#             max_day = 28
#         else:
#             max_day = 30

#         for num_day in range(1, max_day+1): # 달 설정
#             num_date = str(num_year) + "-" + str(num_month) + "-" + str(num_day)
#             print(num_date)


# # 날짜 변경하기 (예시-완성)
# for year in range(2018, 2020):
#     test_data = str(year) + "-01-01"
    
#     url = 'http://apis.data.go.kr/1390802/AgriWeather/WeatherObsrInfo/GnrlWeather/getWeatherTimeList'
#     params ={'serviceKey' : '*****', 'Page_No' : '1', 'Page_Size' : '24', 'date_Time' : test_data, 'obsr_Spot_Nm' : '성주군 대가면', 'obsr_Spot_Code' : '719862A001' }
#     response = requests.get(url, params=params)
#     print(response.text) # 잘 불러왔는지 확인 , 200이면 성공
