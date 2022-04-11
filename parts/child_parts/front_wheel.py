# File: front_wheel.py
# Author: Henri Kuoppala, Juuso Äijälä
# Description: front_wheel class inherited from part

import sys
sys.path.insert(1, "../parent_parts")
from part import Part

class Front_Wheel(Part):
    def __init__(self):
        Part.__init__(self, "front wheel")
        self.__fault = "handlebars are vibrating"

    def set_fault(self, fault):
        self.__fault = fault

    def get_fault(self):
        return self.__fault
