from typing import Tuple
#my class node data
class Node_Data:
    def __init__(self,key:int,p:Tuple):
        self.__key=key
        self.__position = p
        self.info=""
        self.weight=0
        self.tag=0
        self.in_edges=0
        self.out_edges=0

    def getKey(self) :
        return self.__key
    def getPos(self):
        return self.__position

    def setPos(self,pos:tuple):
        self.__position=pos
    def getInfo(self):
        return self.info
    def getW(self):
        return self.weight
    def getT(self):
        return self.tag
    def setT(self,tag:int):
        self.tag=tag
    def setW(self,W:int):
        self.weight=W
    def setI(self,I:str):
        self.info=I
    def __repr__(self):
        return "%s: |edges out| %s |edges in| %s" % (self.__key,self.out_edges,self.in_edges)