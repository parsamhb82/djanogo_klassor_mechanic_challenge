import pickle
import random
class  Garage:
    def __init__(self, x, y , map):
        self.__x = x 
        self.__y = y
        self.__map = map
    def get_distance(self, x , y):
        return self.__map.get_distance(self.__x, self.__y, x , y)
        



class GarageMananger:
    def __init__(self, map) -> None:
        self.map = map
        
    def load(self):
        try:
            with open("garage_data.pkl" ,"rb") as inp:
                data = pickle.load(inp)
                self.garage_list = data
        except:
            self.garage_list = []
        
    def initiate(self , map):

         return [Garage(random.randint(1,100),random.randint(1,100) ,map) for i in range(5)]
        
        
            
    def save(self):
        with open("garage_data.pkl" ,"wb") as otp:
            pickle.dump(self.garage_list , otp)
            
        
    def get_distance_to(self, x, y):
        ret = []
        for garage in self.garage_list:
            ret.append(garage.get_distance(x, y))
        
        return ret
    
    def add_garage(self, x, y):
        self.garage_list.append(Garage(x, y, self.map))