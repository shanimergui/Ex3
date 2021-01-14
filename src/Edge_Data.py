#my class node data
class Edge_Data:
    def __init__(self,src:int,dest:int,weight:float):
        self.__src=src
        self.__dest = dest
        self.__w=weight
        self.info=""
        self.tag=0

    def getsrc(self):
        return self.__src
    def getdest(self):
        return self.__dest
    def getW(self):
        return self.__w
    def getT(self):
        return self.tag
    def getI(self):
        return self.info
    def setT(self,tag:int):
        self.tag=tag
    def setI(self,I:str):
        self.info=I
    def __repr__(self):
        return str(self.__w)