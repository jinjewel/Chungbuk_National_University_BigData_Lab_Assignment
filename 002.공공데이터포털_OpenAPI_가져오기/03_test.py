import requests
import pprint
import json

url = 'http://apis.data.go.kr/1390802/AgriWeather/WeatherObsrInfo/GnrlWeather/getWeatherTimeList'
params ={'serviceKey' : '*****', 
         'Page_No' : '1', 
         'Page_Size' : '24', 
         'date_Time' : '2018-01-02', 
         'obsr_Spot_Nm' : '성주군 대가면', 
         'obsr_Spot_Code' : '719862A001' }
res = requests.get(url, params=params)

if res.status_code == 200: # 페이지가 잘 불러왔는지 확인 , 200이면 성공
    response = requests.get(res)
    contents = response.text

    pp = pprint.PrettyPrinter(indent=4)
    print(pp.pprint(contents))
    
else : # 페이지가 잘 안 불러지면
    print("\n웹 페이지를 불러오는데 오류가 생성되었습니다. \n")