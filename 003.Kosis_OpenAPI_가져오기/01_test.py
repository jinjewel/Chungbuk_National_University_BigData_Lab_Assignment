import json 
from urllib.request import urlopen # python 3.x 버전에서 사용 (2.x 버전이라면 from urllib import urlopen) 
from PyQt5 import QtWidgets # 설피 필요
from PyQt5.QtWidgets import * 
import functools as fc 
import sys 

#클릭한 목록에 대한 하위 목록 생성
class NewWindow(QtWidgets.QMainWindow):    
    def __init__(self, parent=None):        
        super(NewWindow, self).__init__(parent)        
        centralWidget = QWidget()        
        self.setCentralWidget(centralWidget)        
        self.setGeometry(300, 300, 500, 500) 

        Setting(self, List_Id) #최상위 목록 생성
        

class MyWindow(QtWidgets.QMainWindow, QPushButton):    
    def __init__(self):        
        super(MyWindow, self).__init__()        
        centralWidget = QWidget()        
        self.setCentralWidget(centralWidget)        
        self.setGeometry(200, 200, 500, 500)        
        self.setStyleSheet("background-color: white")        
        Setting(self, 'A')        
        
#목록 셋팅 함수
def Setting(self, parentId):    
    
    #url을 통해 json 데이터 가져오기    
    with urlopen("https://kosis.kr/openapi/statisticsList.do?method=getList&apiKey=ZjZjOTI3MjRjNmU1YzdhZTMwOWRjNjgxN2MzNDgwNmY=&vwCd=MT_ZTITLE&parentListId="+parentId+"&format=json&jsonVD=Y") as url:       
        json_file = url.read()    
        
    py_json = json.loads(json_file.decode('utf-8'))    
        
    #하위 목록이 있다면 LinkButton, 하위 목록이 없다면 label로 생성    
    for i, v in enumerate(py_json):        
        if 'LIST_NM' in v:            
            btn = QCommandLinkButton(v['LIST_NM'], self)            
            btn.setStyleSheet("Text-align: left;"                             
                              "border: none;"                             
                             )            
                
            btn.setGeometry(100, 50 * i, 500, 40)            
            btn.clicked.connect(fc.partial(Action, self, v['LIST_ID']))        
        else:            
            lbl = QLabel(v['TBL_NM'], self)            
            lbl.setGeometry(100, 50 * i, 500, 40) 
                
def Action(self, check):    
    global List_Id    
    List_Id = check    
    
    NewWindow(self).show() 

if __name__ == "__main__":    
    app = QtWidgets.QApplication(sys.argv)    
    window = MyWindow()    
    window.show()    
    sys.exit(app.exec_())