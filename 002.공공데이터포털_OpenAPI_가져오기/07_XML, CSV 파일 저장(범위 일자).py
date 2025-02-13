# Open API를 불러와서 XML, CSV파일로 저장하는 코드(자동으로 기준 날짜(연, 월, 일) 조정)

import requests # Open API 사용하기 위해 선언
import xml.etree.ElementTree as ET # xml 형태로 불러오고 xml로 저장하기 위해 선언
import csv # xml로 저장된 파일을 csv로 바꿀때
import time

## 날짜 설정하기 (예시-완성) (단, 16년 20년 24년도는 윤년)
# URL를 만들 때 하루마다 날짜를 바꿔가며 URL를 작성해야 하므로 날짜 변수를 해당 프레임에 맞게 만들어 사용해야됨
# '년-월-일' 형식으로 작성해야 되며, 자리수를 꼭 2자리로 한자리 숫자 앞에는 0을 붙여서 형식을 맞춰야 함 
# 또한 15년도부터 데이터를 가져오는 것이므로 16년부터 4년마다 돌아오는 윤년을 생각하여 코드 작성
for num_year in range(2024, 2025): # 년도 설정
    for num_month in range(5, 6): # 월 설정
        if num_month == 1 or num_month == 3 or num_month == 5 or num_month == 7 or num_month == 8 or num_month == 10 or num_month == 12:
            max_day = 31
        elif num_month == 2:
            max_day = 28
        else:
            max_day = 30
        if num_year == 2016 and num_month == 2 :
            max_day = 29
        if num_year == 2020 and num_month == 2 :
            max_day = 29            
        if num_year == 2024 and num_month == 2 :
            max_day = 29  

        for num_day in range(1, max_day+1): # 달 설정
            if len(str(num_day)) == 1:
                num_day = '0' + str(num_day)
            if len(str(num_month)) == 1:
                num_month = '0' + str(num_month)

            # 최종적으로 년, 월, 일을 합쳐서 날짜 변수를 생성
            num_date = str(num_year) + "-" + str(num_month) + "-" + str(num_day)
            

            ## 4. OpenAPI 데이터를 파이썬으로 출력하는 코드 작성
            # 'Call Back URL'를 설정
            url = 'http://apis.data.go.kr/1390802/AgriWeather/WeatherObsrInfo/GnrlWeather/getWeatherTimeList'

            ## 찾고자 하는 지역의 이름 및 코드 설정
            local_name = '성주군 대가면' # 2015년 01월 01일부터 사용 
            local_number = '719862A001'
            
            # local_name = '서귀포 감산리' # 2016년 03월 13일부터 사용 
            # local_number = '063531B010'
            
            # local_name = '공주시 우성면' # 2015년 12월 14일부터 사용
            # local_number = '032528A001' # 

            # local_name = '천안시 목천음' # 
            # local_number = '330846A001' # 
            
            # local_name = '홍천군 자운리' # 2016년 5월 10일부터 사용
            # local_number = '250845E001' # 
            
            # local_name = '상주시 외서면' # 2017년 12월 01일부터 사용
            # local_number = '037136F022' # 
            



            # '요청 메시지 명세'에 적혀있는 변수들을 알맞에 설정
            params ={'serviceKey' : '*****', 
                     'Page_No' : '1', 
                     'Page_Size' : '24', 
                     'date_Time' : num_date, 
                     'obsr_Spot_Nm' : local_name, 
                     'obsr_Spot_Code' : local_number }
            root_count = 0

            # 해당 날짜의 데이터가 잘 불러와 졌는지 확인, [200]로 출력되면 잘 불러와졌다는 것을 확인
            response = requests.get(url, params=params)
            print(num_date, " --> ", response)

            # 루트 주소 설정
            root = ET.fromstring(response.content)

            # XML 파일 생성을 생성하여 파이
            tree = ET.ElementTree(root)
            tree.write('농업기상데이터_{}_{}_data.xml'.format(num_date, local_name), encoding='utf-8')



            ## 5. 파이썬으로 불러온 데이터를 CSV 파일로 저장하는 코드 작성

            # 저장할 CSV파일을 만들고 작업을 실행
            with open('농업기상데이터_{}_{}_data.csv'.format(num_date, local_name), 'w', encoding ='utf-8', newline='') as csv_file:
                writer = csv.writer(csv_file)

                # 첫 행에 변수명을 입력
                header = [] 
                root_h = root[1][3]
                for x in root_h[0]:
                    header.append(x.tag)
                writer.writerow(header)

                # 두번째 행부터 해당 데이터를 입력
                for item in root_h:
                    row = None
                    row = []
                    for child in item:
                        row.append(child.text)
                    writer.writerow(row)
                    
 