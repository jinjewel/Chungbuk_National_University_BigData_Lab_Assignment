import json 
from urllib.request import urlopen # python 3.x 버전에서 사용 (2.x 버전이라면 from urllib import urlopen) 
import matplotlib.pyplot as plt # 설치 필요


# 한글 폰트 사용을 위해서 세팅
from matplotlib import font_manager, rc 
font_path = "C:/Windows/Fonts/malgun.ttf" 
font = font_manager.FontProperties(fname=font_path).get_name() 
rc('font', family=font) 

#url을 통해 json 데이터 가져오기
# 예제 URL : 
URL_01 = "https://kosis.kr/openapi/statisticsData.do?method=getList&apiKey=ZjZjOTI3MjRjNmU1YzdhZTMwOWRjNjgxN2MzNDgwNmY=&format=json&jsonVD=Y&userStatsId=*****&prdSe=Y&newEstPrdCnt=3"

# 기관명 : 통계청(101) / 통계표명 : 인구밀도(인구주택총조사기준) / 통계표ID : DT_1B08024 
# 해당 URL : 
URL_02 = "https://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList&apiKey=ZWRjOTE2ZTQxYTc2ODVhNzY3NjJhYTVmM2RkNGMzNWU=&itmId=T7+&objL1=00+&objL2=&objL3=&objL4=&objL5=&objL6=&objL7=&objL8=&format=json&jsonVD=Y&prdSe=Y&newEstPrdCnt=10&prdInterval=1&outputFields=ORG_ID+TBL_ID+TBL_NM+OBJ_ID+OBJ_NM+OBJ_NM_ENG+NM+NM_ENG+ITM_ID+ITM_NM+ITM_NM_ENG+UNIT_NM+UNIT_NM_ENG+PRD_SE+PRD_DE+&orgId=101&tblId=DT_1B08024"

# 통계표명 : 사망원인(237항목)/성/연령(5세)별 사망자수, 사망률 / 통계표ID : DT_1B34E07
# 해당 URL : URL_03 = "https://kosis.kr/openapi/statisticsBigData.do?method=getList&apiKey=ZWRjOTE2ZTQxYTc2ODVhNzY3NjJhYTVmM2RkNGMzNWU=&format=xls&userStatsId=*****&prdSe=Y&newEstPrdCnt=10&prdInterval=1"

# https://kosis.kr/openapi/statisticsBigData.do?method=getList&apiKey=ZWRjOTE2ZTQxYTc2ODVhNzY3NjJhYTVmM2RkNGMzNWU=&userStatsId=*****&prdSe=Y&newEstPrdCnt=10&prdInterval=1&format=json



with urlopen(URL_02) as url:    
    json_file = url.read()    
    
py_json = json.loads(json_file.decode('utf-8')) 

#변수 지정 및 데이터 저장

data = [] 

for i, v in enumerate(py_json):    
    value = []    
    value.append(v['PRD_DE'])    
    value.append(v['DT'])        
    data.append(value) 
    print(value)
    
#Table 만들기
fig, ax = plt.subplots(1,1) 
column_labels=["시점", ""] 
ax.axis('tight') 
ax.axis('off') 
ax.table(cellText=data,colLabels=column_labels,colColours =["yellow"] * 2, loc="center", cellLoc='center') 

plt.show()