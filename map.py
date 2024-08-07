import heapq
import json
import math
class Node :
    def __init__(self , x , y, name) -> None:
        self._name = name
        self._x = x
        self._y = y 
        self._edges = []
    def node_x_getter(self):
        return self._x
    def node_y_getter(self):
        return self._y
    def garage_bool_getter(self):
        return self._garage_bool  
    def add_edge(self, destination, weight):
        self._edges.append({'destination' : destination , 'weight' : weight})
    def edges_getter(self):
        return self._edges
    
    def get_name(self):
        return self._name
    
    def get_neighbor(self):
        neighbors = []
        for edge in self._edges:
            neighbors.append((edge['destination'], edge['weight']))
        return neighbors
class Maps : 
    def __init__(self) -> None:
        self.nodes_list = []


    def return_jason_to_map (self) : 
        with open("graph.json", 'r') as graph_file:
            g = json.load(graph_file)
            nodes = g["nodes"]
            edges = g["edges"]
            for node in nodes:
                self.add_node(node['X'], node['Y'], node['Name'])
            for edge in edges:
                weight = edge['Distance']
                source = edge['Source']
                destination = edge['Destination']
                self.nodes_list[source].add_edge(destination, weight)
                self.nodes_list[destination].add_edge(source, weight)

    def coordinate_to_node(self, x, y):
        min_distance = float('inf')
        wanted_node = None
        for node in self.nodes_list:
            node : Node
            x_node = node.node_x_getter()
            y_node = node.node_y_getter()
            dis = (((x - x_node) + (y - y_node))**2)**0.5
            if dis < min_distance :
                min_distance = dis
                wanted_node = node
        return wanted_node
            

    
    def get_diatance(self, start_x, start_y, goal_x, goal_y):
        start_node = self.coordinate_to_node(start_x, start_y)
        goal_node = self.coordinate_to_node(goal_x, goal_y)

        return self.a_star(start_node, goal_node)
    
    def add_node(self, x, y):
        self.nodes_list.append(Node(x, y))
    
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
    
        

