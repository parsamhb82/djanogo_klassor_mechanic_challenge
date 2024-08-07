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
            nodes = g["Nodes"]
            edges = g["Edges"]
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
            dis = (((x - x_node)**2 + (y - y_node)**2))**0.5
            if dis < min_distance :
                min_distance = dis
                wanted_node = node
        return wanted_node
            

    
    def get_distance(self, start_x, start_y, goal_x, goal_y):
        start_node = self.coordinate_to_node(start_x, start_y)
        goal_node = self.coordinate_to_node(goal_x, goal_y)

        return self.A_star(start_node, goal_node)
    
    def add_node(self, x, y, name):
        self.nodes_list.append(Node(x, y, name))
    
    def heuristic (self , node1 , node2 ) : 
        node1 : Node
        node2 : Node
        return math.sqrt( (node1.node_x_getter() - node2.node_x_getter()) **2 + (node1.node_y_getter() - node2.node_y_getter()) **2 )

    def A_star (self , start_node , end_node) : 
        open_list = []
        heapq.heappush(open_list, (0, start_node))
        closed_list = set()
        g = {start_node.get_name(): 0}
        came_from = {}

        while open_list:
            current_cost, current_node = heapq.heappop(open_list)

            if current_node.get_name() in closed_list:
                continue

            if current_node.get_name() == end_node.get_name():
                return g[current_node.get_name()]

            closed_list.add(current_node.get_name())

            for neighbor_name, weight in current_node.get_neighbor():
                neighbor_node = self.nodes_list[neighbor_name]
                tentative_g_score = g[current_node.get_name()] + weight

                if neighbor_name in closed_list:
                    continue

                if tentative_g_score < g.get(neighbor_name, float('inf')):
                    came_from[neighbor_name] = current_node
                    g[neighbor_name] = tentative_g_score
                    f_score = tentative_g_score + self.heuristic(neighbor_node, end_node)
                    heapq.heappush(open_list, (f_score, neighbor_node))

        return float('inf')

        

