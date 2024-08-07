import math
import random
import pickle

class Mechanic:
    def __init__(self, name, X, Y, id, service, map) -> None:
        self.__name = name
        self.__X = X
        self.__Y = Y
        self.__id = id
        self.__service = None
        self.__map = map
        self._base_price = 0
        self._hourly_price = 0

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_service(self):
        return self.__service

    def set_service(self, service):
        self.__service = service

    def get_x(self):
        return self.__X

    def get_y(self):
        return self.__Y

    def calculate_total_price(self, service_time):
        return service_time * self._hourly_price + self._base_price


class MechanicIndirect(Mechanic):
    def __init__(self, name, X, Y, id, service, map):
        super().__init__(name, X, Y, id, service, map)
        self.__base_price = 250000
        self.__price_per_hour = 100000
        self.__speed = 60

    def get_base(self):
        return self.__base_price

    def get_hour(self):
        return self.__price_per_hour

    def get_speed(self):
        return self.__speed

    def get_distance(self, x, y):
        distance_to_garage = self.garage_manager.get_distance_to(
            self.get_x(), self.get_y()
        )
        distance_from_garage = self.garage_manager.get_distance_to(x, y)
        all_distances = [
            i + j for i, j in zip(distance_to_garage, distance_from_garage)
        ]
        return min(all_distances)


class MechanicManager:
    def __init__(self):
        self.__drone_list = []
        self.__direct_list = []
        self.__indirect_list = []
    
    def initialize(self, mapp):
        names = ["Ali", "Mamad", "Reza", "Mohsen"]
        for i in range(3):
            self.__drone_list.append(
             Mechanic(
                random.choice(names),
                random.randint(1, 100),
                random.randint(1, 100),
                i,
                None,
                mapp,
            ))
        for i in range(3):
            self.__direct_list.append(
             Mechanic(
                random.choice(names),
                random.randint(1, 100),
                random.randint(1, 100),
                i,
                None,
                mapp,
            ))
        for i in range(3):
            self.__indirect_list.append(
             Mechanic(
                random.choice(names),
                random.randint(1, 100),
                random.randint(1, 100),
                i,
                None,
                mapp,
            ))
            

    def load(self,mapp) -> None:
        try:
            with open('mechanic_data.pkl', 'rb') as inp:
                data = pickle.load(inp)
                inp.close()
                self.__mechanic_list = data
        except:
            MechanicManager.initialize(mapp)


    def save_users(self):
        with open('mechanic_data.pkl', 'wb') as otp:
            pickle.dump(self.__mechanic_list , otp)
            
            
    def get_mechanic_drone_list(self):
        return self.__drone_list

    def get_mechanic_direct_list(self):
        return self.__direct_list

    def get_mechanic_indirect_list(self):
        return self.__indirect_list


    def find_mechanic_indirect(self, x, y):
        mechanic: MechanicIndirect
        min_distance = math.inf
        assigned_mechanic = None
        for mechanic in self.get_mechanic_indirect_list():
            if mechanic.get_service():
                continue
            distance = mechanic.get_distance(x, y)
            if distance < min_distance:
                min_distance = distance
                assigned_mechanic = mechanic
        return assigned_mechanic, min_distance
    
    def find_mechanic_direct(self, x, y):
        mechanic: MechanicDirect
        min_distance = math.inf
        assigned_mechanic = None
        for mechanic in self.get_mechanic_direct_list():
            if mechanic.get_service():
                continue
            distance = mechanic.get_distance(x, y)
            if distance < min_distance:
                min_distance = distance
                assigned_mechanic = mechanic
        return assigned_mechanic, min_distance

    def find_mechanic_drone(self, x, y):
        mechanic: MechanicDrone
        min_distance = math.inf
        assigned_mechanic = None
        for mechanic in self.get_mechanic_drone_list():
            if mechanic.get_service():
                continue
            distance = mechanic.get_distance(x, y)
            if distance < min_distance:
                min_distance = distance
                assigned_mechanic = mechanic
        return assigned_mechanic, min_distance



class MechanicDirect(Mechanic):
    def __init__(self, name, X, Y, id, service, map):
        super().__init__(name, X, Y, id, service, map)
        self.__base_price = 100000
        self.__price_per_hour = 100000
        self.__speed = 60

    def get_base_price(self):
        return self.__base_price

    def get_price_per_hour(self):
        return self.__price_per_hour

    def get_speed(self):
        return self.__speed

    def get_distance(self, x, y):
        distance = self.__map.parsa(self.get_x(), self.get_y(), x, y)
        return distance


class MechanicDrone(Mechanic):
    def init(self, name, X, Y, id, service, map):
        super().__init__(name, X, Y, id, service, map)
        self.__base_price = 240000
        self.__speed = 50

    def get_base(self):
        return self.__base_price

    def get_speed(self):
        return self.__speed

    def get_distance(self, x, y):
        distance = self.__map.parsa(self.get_x(), self.get_y(), x, y)
        return distance
    
    
    