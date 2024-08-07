import heapq
import math 

class Node :

    def __init__(self , x , y , garage_bool) -> None:
        self.x = x
        self.y = y 
        self.garage_bool = garage_bool

class Maps :
    
    def __init__(self , adjacency_list ) : 
        self.adjacency_list = adjacency_list

    def heuristic (self , node1 , node2 ) : 
        return math.sqrt( (node1.get_x() - node2.get_x()) **2 + (node1.get_y() - node2.get_y()) **2 )

    def A_star (self , start_node , end_node) : 
        open_list = [start_node]
        close_list = set()
        g = {}
        g [start_node.get_name()] = 0 
        while len(open_list) > 0 : 
            mini = open_list[0]
            for node in open_list : 
                if g[node] + self.heuristic(node, end_node) < g[mini] + self.heuristic(mini, end_node) : 
                    mini = node 

        if mini == 0 :
            print ("path does not exist ! ") 
            return None
        if mini.get_name() == end_node.get_name() : 
            return g[mini]
        for (m, weight) in mini.get_neighbors():
            if m not in open_list and m not in close_list: 
                open_list.add(m)
                g[m.get_name()] = g[mini.get_name()] + weight

    def __init__(self) -> None:
        self.nodes_list = []

    def return_jason_to_map (self) : 
        pass 
