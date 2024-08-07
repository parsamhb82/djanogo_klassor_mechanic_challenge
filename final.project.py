import pickle
import time
class UserManager:
    

    def __init__(self) -> None:
        try:
            with open('user_data.pkl', 'rb') as inp:
                data = pickle.load(inp)
                inp.close()
                self.__user_list = data
        except:
            self.__user_list = []


    def save_users(self):
        with open('user_data.pkl', 'wb') as otp:
            pickle.dump(self.__user_list , otp)


    def search_user(self, ID):
        for user in self.__user_list:
            if user.get_ID() == ID:
                return user
        return False
    
    def add_member(self ,name, id, x, y, service):
        self.__user_list.append(User(name, id, x, y, service))


class ServiceManager:


    def __init__(self) -> None:
        try:
            with open('service_data.pkl', 'rb') as inp:
                data = pickle.load(inp)
                inp.close()
                self.__service_list = data
        except:
            self.__service_list = []


    def save_services(self):
        with open('service_data.pkl', 'wb') as otp:
            pickle.dump(self.__service_list , otp)

    def show_service(self):
        for i in self.__service_list:
            print(i)

    def add_service(self, service_obj):
        self.__service_list.append(service_obj)

class Service:

    def __init__(self ,x ,y ,id ,price = None ,start_time = None ,finish_time = None ,mechanic = None ) -> None:
        self.__x = x
        self.__y = y
        self.__id = id
    
    def set_price(self , price):
        self.__price = price

    def set_start_time(self):
        start_time = time.time()
        self.__start_time = start_time
    
    def set_finish_time(self):
        finish_time = time.time()
        self.__finish_time = finish_time

    def set_mechanic_type(self , mechanic):
        self.__mechanic = mechanic


class User:
    def __init__(self, name, id, x, y, service):
        self.__name = name
        self.__id = id
        self.__x = x
        self.__y = y
        self.__service = service.add_id(self.id)


    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def get_service(self):
        return self.__service
        
