## Ex3

## The project

In this project, we used Python in order to build a directed and weighted graph.
- Weighted means that the edge has a weight superior to 0.
- Directed means that we have 2 nodes : one of them is a src and the other is dest.

## The Classes

Edgedata : this class gives each edge in a weighted graph 2 nodes. Each edge is connected to 2 nodes (vertex) - src and dest - and has a weight. 
 
Nodedata : this class gives each node in a weighted graph, an id, a location, a weight and a tag

Digraph : we used a dict which has a key and value. The dic is a dictionnary that plays the role of an hashmap within an hashmap.
              The first dict is for the vertices and the second one is for the edges.

GraphAlgo : like in the Ex_2 we used the 2 algorithms : Tarjan and Dijkstra.

Tarjan : an algorithm that divides the graph into components. Each node is placed on a stack in order of their visit.
         We send one node and he returns  We use it to know in which component the nodes are situated. 

Dijkstra : It recieves 2 nodes - src ad dest. It goes from the src to the dest node and go in the direction of the node with the lowest weight.

One component : We send one node and he returns the component in which each node is connected to it.

All component : If the graph is valid, we can access from any node and go to any node.


Our goal was to compare the running time in different languages : Python, Java and NetworkX. 

excel to compare the results 
