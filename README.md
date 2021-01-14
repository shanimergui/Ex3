## Ex3

#### The project

In this project, we used Python in order to build a directed and weighted graph.
- Weighted means that the edge has a weight superior to 0.
- Directed means that we have 2 nodes : one of them is a src and the other is dest.


#### The Classes

###Edgedata : this class gives each edge in a weighted graph 2 nodes. Each edge is connected to 2 nodes (vertex) - src and dest - and has a weight. 
 
###Nodedata : this class gives each node in a weighted graph, an id, a location, a weight and a tag

###Digraph : we used a dict which has a key and value. The dic is a dictionnary that plays the role of an hashmap within an hashmap.
              The first dict is for the vertices and the second one is for the edges.

###GraphAlgo : like in the Ex_2 we used the 2 algorithms : Tarjan and Dijkstra.

###Tarjan : an algorithm that divides the graph into components.
          
          
The algorithm : Each node is placed on a stack in order of their visit.
                We send one node and he returns  We use it to know in which component the nodes are situated. 
                
Tarjan's algorithm is based on depth first search (DFS). The vertices are indexed as they are traversed by DFS procedure.
                While returning from the recursion of DFS, every vertex V gets assigned a vertex L as a representative. 
                L is a vertex with the least index that can be reach from V. 
                Nodes with the same representative assigned are located in the same strongly connected component.
      
[alt text](https://iq.opengenus.org/content/images/2019/06/Kosaraju.png)
      
One component : We send one node and he returns the component in which each node is connected to it.

All component : If the graph is valid, we can access from any node and go to any node.



###Dijkstra : It recieves 2 nodes - src ad dest. It goes from the src to the dest node and go in the direction of the node with the lowest weight.

The algorithm : we mark the selected initial node with a current distance of 0 and the rest with infinity.
               *We set the non-visited node with the smallest current distance as the current node C.
                For each neighbour N of the current node C: we add the current distance of C with the weight of the edge connecting C-N. 
                If it's smaller than the current distance of N, we define it as the new current distance of N.
                Mark the current node C as visited.
                If there are non-visited nodes, go to step *.


![alt text](https://i.morioh.com/2020/01/15/ca0df6b3edfc.jpg)
