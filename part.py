# File: part.py
# Author: Henri Kuoppala, Juuso Äijälä
# Description: part class

class Part:
    def __init__(self, part_name):
        self.__part_name = part_name
        self.__is_attached = True
        self.__parts_to_remove_first = []
        self.__faulty = False

    def set_part_name(self, part_name):
        self.__part_name = part_name
    
    def set_attached(self, attached):
        self.__is_attached = attached
    
    def set_parts_to_remove(self, parts):
        self.__parts_to_remove_first = parts

    def set_faulty(self, faulty):
        self.__faulty = faulty

    def get_part_name(self):
        return self.__part_name

    def get_attached(self):
        return self.__is_attached

    def get_parts_to_remove(self):
        return self.__parts_to_remove_first

    def get_faulty(self):
        return self.__faulty

    def add_part_to_remove(self, part):
        parts = self.__parts_to_remove_first
        parts.append(part)
        self.__parts_to_remove_first = parts

    def replace(self):
        self.__faulty = False
        self.__is_attached = True

    def __str__(self):
        return f"{self.__part_name}"
    