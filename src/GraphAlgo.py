from typing import List
from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from queue import PriorityQueue
import json
import math
import matplotlib.pyplot as myplot

# global variables
list_path = []
list_all_path = []
import random


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, other=DiGraph()):
        self.gr = other

    def get_graph(self) -> GraphInterface:
        return self.gr

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, 'r') as file_read:
                obj = json.load(file_read)
            self.gr = DiGraph()
            # {"pos":"35.18910131880549,32.103618700840336,0.0","id":10}
            # {"id": 0}
            for nodes in obj['Nodes']:
                if nodes.get('pos') is None:
                    self.gr.add_node(nodes.get('id'))
                else:
                    pos = tuple(map(float, nodes.get('pos').split(',')))
                    self.gr.add_node(nodes.get('id'), pos)

            # {"src": 0,"w": 1.0286816758196655,"dest": 1}
            for edges in obj['Edges']:
                self.gr.add_edge(edges.get('src'), edges.get('dest'), edges.get('w'))
            return True
        except FileNotFoundError:
            return False

    def save_to_json(self, file_name: str) -> bool:
        nodes = []
        edges = []
        for node in self.gr.get_all_v().values():
            if node.getPos() is None:
                nodes.append({"id": node.getKey()})
            else:
                pos = str(node.getPos()[0]) + ',' + str(node.getPos()[1]) + ',' + str(node.getPos()[2])
                nodes.append({"pos": pos, "id": node.getKey()})
        # {"src": 0,"w": 1.0286816758196655,"dest": 1}
        for x in self.gr.get_all_v():
            for edge in self.gr.all_out_edges_of_node(x).values():
                edges.append({"src": edge.getsrc(), "w": edge.getW(), "dest": edge.getdest()})

        graphtofile = {"Edges": edges, "Nodes": nodes}
        try:
            with open(file_name, 'w') as file_write:
                json.dump(graphtofile, file_write)
            return True
        except FileNotFoundError:
            return False

    # shortest path using dijsktra algorithm
    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if id1 not in self.gr.get_all_v() or id2 not in self.gr.get_all_v():
            return math.inf, []
        self.__dijsktra(id1)
        dest = self.gr.get_all_v()[id2]

        if dest.getW() is math.inf:
            return math.inf, []

        list_path = []
        list_path.insert(0, id2)
        str = dest.getInfo()
        while str != "":
            node = self.gr.get_all_v()[str]
            list_path.insert(0, node.getKey())
            str = node.getInfo()
        return dest.getW(), list_path

    def __init_all_nodes(self):
        for vertex in self.gr.get_all_v().values():
            vertex.setT(0)
            vertex.setW(math.inf)
            vertex.setI("")

    # private help functio dijsktra
    def __dijsktra(self, start: int):
        self.__init_all_nodes()
        q = PriorityQueue()
        s = self.gr.get_all_v()[start]
        s.setW(0)
        q.put((s.getW(), s.getKey(), s))

        while not q.empty():
            v1 = q.get()[2]
            for e in self.gr.all_out_edges_of_node(v1.getKey()).values():
                v2 = self.gr.get_all_v()[e.getdest()]
                weight = v1.getW() + e.getW()
                if weight < v2.getW():
                    v2.setW(weight)
                    v2.setI(v1.getKey())
                    q.put((v2.getW(), v2.getKey(), v2))

    def connected_component(self, id1: int) -> list:
        if self.gr is None or id1 not in self.gr.get_all_v():
            return []
        self.__init_all_nodes()
        # for using global variables need to write global
        global list_path

        list_path = []
        # java
        self.__dfs(id1)
        return list_path

    # def __dfs(self,at:int):
    #     global s, id_per_node, list_path ,list_all_path
    #     at_node = self.gr.get_all_v()[at]
    #     s.append(at_node)
    #     id_per_node+=1
    #
    #     # on stack - info , ids - weight low - tag
    #     at_node.setW(id_per_node)
    #     at_node.setT(id_per_node)
    #     at_node.setI("true")
    #     for to in self.gr.all_out_edges_of_node(at):
    #         node_to = self.gr.get_all_v()[to]
    #         if node_to.getW() is math.inf: self.__dfs(node_to.getKey())
    #         if node_to.getInfo() == "true": at_node.setT(min(at_node.getT(),node_to.getT()))
    #
    #     if at_node.getW() is at_node.getT() :
    #         # java
    #         list_path=[]
    #         while s:
    #             node = s.pop()
    #             # java
    #             list_path.insert(0, node.getKey())
    #             node.setI("")
    #             node.setT(at_node.getW())
    #             if node.getKey() is at : break
    #         #java
    #         list_all_path.insert(0,list_path)
    #         #sccCount++

    def __dfs(self, at: int):
        global list_path, list_all_path
        s = []
        id_per_node = 0
        stack = [(at, 0)]
        while stack:
            at, i = stack[-1]
            del stack[-1]
            at_node = self.gr.get_all_v()[at]
            if i == 0:
                s.append(at_node)
                id_per_node += 1

                # on stack - info , ids - weight low - tag
                at_node.setW(id_per_node)
                at_node.setT(id_per_node)
                at_node.setI("true")
            flag = False
            n = 0
            for to in self.gr.all_out_edges_of_node(at):
                node_to = self.gr.get_all_v()[to]
                if node_to.getW() is math.inf:
                    stack.append((at, n + 1))
                    stack.append((to, 0))
                    n += 1
                    flag = True
                    break
                if node_to.getInfo() == "true": at_node.setT(min(at_node.getT(), node_to.getT()))
            if flag == True: continue
            if at_node.getW() is at_node.getT():
                # java
                list_path = []
                while s:
                    node = s.pop()
                    list_path.insert(0, node.getKey())
                    node.setI("")
                    node.setT(at_node.getW())
                    if node.getKey() is at: break
                list_all_path.insert(0, list_path)
            if stack:
                to = at
                at, _ = stack[-1]
                node_to = self.gr.get_all_v()[to]
                at_node.setT(min(at_node.getT(), node_to.getT()))

    def connected_components(self) -> List[list]:
        if self.gr is None:
            return []
        self.__init_all_nodes()
        # for using global variables need to write global
        global list_path, list_all_path

        list_path = []
        list_all_path = []
        for x in self.gr.get_all_v().values():
            if x.getW() is math.inf:
                self.__dfs(x.getKey())
        # java
        return list_all_path

    def plot_graph(self) -> None:
        xnode = []
        ynode = []
        for node in self.gr.get_all_v().values():
            if node.getPos() is None:
                node.setPos((random.uniform(35.18, 35.2), random.uniform(32.1, 32.2)))
                xnode.append(node.getPos()[0])
                ynode.append(node.getPos()[1])
            else:
                xnode.append(node.getPos()[0])
                ynode.append(node.getPos()[1])

        # plot the data
        keys = [n for n in self.gr.get_all_v().keys()]
        for i, txt in enumerate(keys):
            myplot.annotate(txt, (xnode[i], ynode[i]))

        myplot.plot(xnode, ynode, 'o', color='blue')

        for n in self.gr.get_all_v().keys():
            for edge in self.gr.all_out_edges_of_node(n).keys():
                pos1 = self.gr.get_all_v().get(n).getPos()
                pos2 = self.gr.get_all_v().get(edge).getPos()

                myplot.arrow(pos1[0], pos1[1], (pos2[0] - pos1[0]), (pos2[1] - pos1[1]),
                             length_includes_head=True,
                             width=0.00003, head_width=0.00025, color='green')
        myplot.show()
