import heapq
class Node :
    def __init__(self , x , y, garage_bool) -> None:
        self._x = x
        self._y = y 
        self._garage_bool = garage_bool
    def node_x_getter(self):
        return self._x
    def node_y_getter(self):
        return self._y
    def garage_bool_getter(self):
        return self._garage_bool


class Maps : 
    def __init__(self) -> None:
        self.nodes_list = []

    def return_jason_to_map (self) : 
        pass
    
    def coordinate_to_node(self, x, y):
        return #node
    
    def a_star(self, start_x, start_y, goal_x, goal_y):
        start_node = self.coordinate_to_node(start_x, start_y)
        goal_node = self.coordinate_to_node(goal_x, goal_y)
        

