import requests # Open API 사용하기 위해 선언
import xml.etree.ElementTree as ET # xml 형태로 불러오고 xml로 저장하기 위해 선언
import csv # xml로 저장된 파일을 csv로 바꿀때

# 날짜 설정하기 (예시-완성) (단, 16년 24년도 2월은 29일까지 있음)
for num_year in range(2015, 2016): # 년도 설정
    for num_month in range(1, 13): # 월 설정
        if num_month == 1 or num_month == 3 or num_month == 5 or num_month == 7 or num_month == 8 or num_month == 10 or num_month == 12:
            max_day = 31
        elif num_month == 2:
            max_day = 28
        else:
            max_day = 30

        for num_day in range(1, max_day+1): # 달 설정
            num_date = str(num_year) + "-" + str(num_month) + "-" + str(num_day)
            
            url = 'http://apis.data.go.kr/1390802/AgriWeather/WeatherObsrInfo/GnrlWeather/getWeatherTimeList'
            params ={'serviceKey' : '*****', 
                     'Page_No' : '1', 
                     'Page_Size' : '24', 
                     'date_Time' : num_date, 
                     'obsr_Spot_Nm' : '성주군 대가면', 
                     'obsr_Spot_Code' : '719862A001' }
            root_count = 0

            response = requests.get(url, params=params)
            print(num_date, " --> ", response)

            root = ET.fromstring(response.content)
            tree = ET.ElementTree(root)
            tree.write('농업기상데이터_{}_성주군대가면_data.xml'.format(num_date), encoding='utf-8')

            # # csv 파일 열기
            # with open('response.csv', 'w', encoding ='utf-8', newline='') as csv_file:
            #     writer = csv.writer(csv_file)

            #     header = []

            #     # root는 xml.etree.ElementTree.Element 타입
            #     root_h = root[1][3]

            #     for x in root_h[0]: # 첫번 째 행, 변수 이름 설정
            #         header.append(x.tag)
            #     writer.writerow(header)

            #     for item in root_h: # 그 날짜의 데이터 입력
            #         row = []
            #         for child in item:
            #             row.append(child.text)
            #         writer.writerow(row)