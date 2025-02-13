from urllib.parse import urlencode, unquote
import requests
import json
import pandas as pd
import csv

# URL 입력
URL_03 = "https://kosis.kr/openapi/statisticsData.do?method=getList&apiKey=ZWRjOTE2ZTQxYTc2ODVhNzY3NjJhYTVmM2RkNGMzNWU=&format=json&jsonVD=Y&userStatsId=*****&prdSe=Y&newEstPrdCnt=4&prdInterval=1"

# 해당 URL이 잘 연결되었는지 확인(응답이 200이면 정상적인 URL을 뜻함)
response = requests.get(URL_03)
print(response)

# 해당 결과들을 Json 형식으로 변경하여 저장
file = response.json()

# 내용 출력하기
print(file) # 전체 출력
for zone in file:
    print("DT : ", zone['DT']) # 특정 내용만 출력(PRD_SE)

# 데이터 프레임으로 만들기
dataframe = pd.json_normalize(file)
print(dataframe)

# 데이터 프레임을 csv 파일로 만들기
from collections import OrderedDict 

df = pd.DataFrame.from_dict(dataframe)
df.to_csv('KOSIS_test03data.csv') #csv파일로 생성














