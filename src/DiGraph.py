from src.GraphInterface import GraphInterface
from src.Node_Data import  Node_Data
from src.Edge_Data import Edge_Data
from typing import Dict

class DiGraph(GraphInterface):
    def __init__(self):
        self.__mc = 0
        self.__Size_e = 0
        self.__vertexs: Dict[int, Node_Data] = dict()
        self.__edges: Dict[int, Dict[int, Edge_Data]] = dict()

    def v_size(self) -> int:
        return len(self.__vertexs)

    def e_size(self) -> int:
        return self.__Size_e

    def get_mc(self) -> int:
        return self.__mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        edge=Edge_Data(id1,id2,weight)
        if  weight >= 0 and id1 is not id2 and id1 in self.__vertexs and id2 in self.__vertexs and id2 not in self.__edges.get(id1):
            self.__edges.get(id1).update({id2: edge})
            self.__Size_e += 1
            self.__mc += 1

            self.__vertexs.get(id2).in_edges +=1
            self.__vertexs.get(id1).out_edges += 1

            return True
        else: return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id not in self.__vertexs:
            node = Node_Data(node_id, pos)
            self.__edges.update({node_id: dict()})
            self.__vertexs.update({node_id: node})
            self.__mc += 1
            return True
        else: return False

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.__vertexs:
            in_edge = self.all_in_edges_of_node(node_id)
            out_edge = self.all_out_edges_of_node(node_id)
            self.__mc += len(in_edge)+len(out_edge)
            self.__Size_e -= len(in_edge)
            self.__Size_e -= len(out_edge)
            for x in in_edge:
                self.__edges.get(x).pop(node_id)

            self.__edges.pop(node_id)
            self.__mc += 1
            #remove vertex
            self.__vertexs.pop(node_id)
            return True
        else: return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 is not node_id2 and node_id1 in self.__vertexs and node_id2 in self.__vertexs and node_id2 in self.__edges.get(node_id1):
            self.__edges.get(node_id1).pop(node_id2)
            self.__Size_e -= 1
            self.__mc += 1

            self.__vertexs.get(node_id2).in_edges -= 1
            self.__vertexs.get(node_id1).out_edges -= 1

            return True
        else:
            return False

    def get_all_v(self) -> dict:
        return self.__vertexs

    def all_in_edges_of_node(self, id1: int) -> dict:
        empty:Dict[int, Edge_Data] = dict()
        for x in self.__vertexs:
            if id1 in self.__edges.get(x):
                empty.update({x: self.__edges.get(x)[id1]})
        return empty

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.__edges.get(id1)

    def __eq__(self, o: object) -> bool:
        if type(o) is not DiGraph:
            return False
        if self.v_size() != o.v_size():
            return False
        if self.e_size() != o.e_size():
            return False
        if self.get_mc() != o.get_mc():
            return False

        for node in self.get_all_v().keys():
            if node not in o.get_all_v():
                return False

            for x in self.all_out_edges_of_node(node).keys():
                if x not in o.all_out_edges_of_node(node):
                    return False
            for x in self.all_out_edges_of_node(node).keys():
                if x not in o.all_in_edges_of_node(node):
                    return False

        return True


    def __repr__(self):
        return "Graph: |V|=%s , |E|=%s" % (self.v_size(), self.e_size())