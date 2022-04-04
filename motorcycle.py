# File: motorcycle.py
# Author: Henri Kuoppala, Juuso Äijälä
# Description: motorcycle class

import part

class Motorcycle:
    def __init__(self):
        self.__is_working = True
        self.__fault_description = None
        self.__parts = []

    def set_working(self, condition):
        self.__is_working = boolean

    def set_fault(self, description):
        self.__fault_description = description

    def set_parts(self, list_of_parts):
        self.__parts = list_of_parts
    
    def get_working(self):
        return self.__is_working

    def get_fault(self):
        return self.__fault_description

    def get_parts(self):
        return self.__parts

    def check_parts(self):
        for part in self.__parts:
            if part.get_faulty() == True:
                self.__is_working = False
                return
        self.__is_working = True
    
    def __str__(self):
        if self.__is_working == True:
            return f"Everything is working"
        else:
            return f"Something is not right, {self.__fault_description}"