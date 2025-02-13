from urllib.parse import urlencode, unquote
import requests
import json
import pandas as pd
import csv

# URL 입력
sd_URL = "https://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList&apiKey=ZWRjOTE2ZTQxYTc2ODVhNzY3NjJhYTVmM2RkNGMzNWU=&itmId=T7+&objL1=00+&objL2=&objL3=&objL4=&objL5=&objL6=&objL7=&objL8=&format=json&jsonVD=Y&prdSe=Y&newEstPrdCnt=10&prdInterval=1&outputFields=ORG_ID+TBL_ID+TBL_NM+OBJ_ID+OBJ_NM+OBJ_NM_ENG+NM+NM_ENG+ITM_ID+ITM_NM+ITM_NM_ENG+UNIT_NM+UNIT_NM_ENG+PRD_SE+PRD_DE+&orgId=101&tblId=DT_1B08024"
finall_URL = "https://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList&apiKey=ZWRjOTE2ZTQxYTc2ODVhNzY3NjJhYTVmM2RkNGMzNWU=&itmId=T7+&objL1=00+11+21+22+23+24+25+26+29+31+32+33+34+35+36+37+38+39+&objL2=&objL3=&objL4=&objL5=&objL6=&objL7=&objL8=&format=json&jsonVD=Y&prdSe=Y&newEstPrdCnt=10&prdInterval=1&orgId=101&tblId=DT_1B08024"

# 해당 URL이 잘 연결되었는지 확인(응답이 200이면 정상적인 URL을 뜻함)
response = requests.get(finall_URL)
print(response)

# 해당 결과들을 Json 형식으로 변경하여 저장
file = response.json()

# # 내용 출력하기
# print(file) # 전체 출력
# for zone in file:
#     print("PRD_SE : ", zone['PRD_SE']) # 특정 내용만 출력(PRD_SE)

# 데이터 프레임으로 만들기
dataframe = pd.json_normalize(file)
print(dataframe)

# 데이터 프레임을 csv 파일로 만들기
from collections import OrderedDict 

df = pd.DataFrame.from_dict(dataframe)
df.to_csv('KOSIS_test02data.csv') #csv파일로 생성














