# Open API를 불러와서 XML, CSV파일로 저장하는 코드(수동으로 기준 날짜(월) 조정)

import requests
import time

num_year = '2020'
num_month = '04'
for num_day in range(17,32):
    if len(str(num_day)) == 1:
        num_day = '0' + str(num_day)
    num_date = str(num_year) + "-" + str(num_month) + "-" + str(num_day)

    ## 찾고자 하는 지역의 이름 및 코드 설정
    # local_name = '성주군 대가면' # 2015년 01월 01일부터 사용 
    # local_number = '719862A001'
            
    # local_name = '서귀포 감산리' # 2016년 03월 13일부터 사용 
    # local_number = '063531B010'
            
    # local_name = '공주시 우성면' # 2015년 12월 14일부터 사용
    # local_number = '032528A001' # 

    # local_name = '천안시 목천음' # 
    # local_number = '330846A001' # 
            
    # local_name = '홍천군 자운리' # 2016년 5월 10일부터 사용
    # local_number = '250845E001' # 
            
    local_name = '상주시 외서면' # 
    local_number = '037136F022' # 

    url = 'http://apis.data.go.kr/1390802/AgriWeather/WeatherObsrInfo/GnrlWeather/getWeatherTimeList'
    params ={'serviceKey' : '*****', 
            'Page_No' : '1', 
            'Page_Size' : '24', 
            'date_Time' : str(num_date), 
            'obsr_Spot_Nm' : local_name, 
            'obsr_Spot_Code' : local_number }

    response = requests.get(url, params=params)
    print(str(num_date)," --> ", response)

    # xml 형태로 불러오고 xml로 저장할 때
    import xml.etree.ElementTree as ET

    root = ET.fromstring(response.content)
    tree = ET.ElementTree(root)
    tree.write('농업기상데이터_{}_{}_data.xml'.format(num_date, local_name), encoding='utf-8') 
    
    # xml로 저장된 파일을 csv로 바꿀때
    import csv

    # csv 파일 열기
    with open('농업기상데이터_{}_{}_data.csv'.format(num_date,local_name), 'w', encoding ='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # 변수명 작성
        header = []
        root_h = root[1][3]
        for x in root_h[0]:
            header.append(x.tag)
        writer.writerow(header)

        # 해당 데이터 작성
        for item in root_h:
            row = None
            row = []
            for child in item:
                row.append(child.text)
            writer.writerow(row)
