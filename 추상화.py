# 부모 클래스에서 추상 메소드로 선언한 메소드에 대해서는 반드시 상속 받은 자식 클래스에서 해당 기능을 구현해야 함

from abc import *

class NetworkAdaptor(metaclass=ABCMeta) :
    @abstractmethod
    def connect(self) :
        pass

class FiveG(NetworkAdaptor) :
    def __init__(self, company) :
        self.company = company
    def connect(self):
        print(f"{self.company} 5G로 연결하였습니다")
        
class WIFI(NetworkAdaptor) :
    def __init__(self, company) :
        self.company = company
    def connect(self):
        print(f"{self.company} WI-FI로 연결하였습니다")

class LTE(NetworkAdaptor) :
    def __init__(self, company) :
        self.company = company
    def connect(self):
        print(f"{self.company} LTE로 연결하였습니다")

net = input("연결할 네트워크 선택 [1]5G [2]WI-FI [3]LTE: ")
if net == "1" :
    adaptor = FiveG("KT Mega Pass")
    adaptor.connect()
elif net == "2" :
    adaptor = WIFI("SKT Telecom")
    adaptor.connect()
elif net == "3" :
    adaptor = LTE("SKT Telecom")
    adaptor.connect()
else : print("연결할 네트워크가 없습니다")