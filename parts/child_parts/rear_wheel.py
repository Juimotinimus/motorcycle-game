# File: rear_wheel.py
# Author: Henri Kuoppala, Juuso Äijälä
# Description: rear_wheel class inherited from part

import sys
sys.path.insert(1, "../")
from part import Part

class Rear_Wheel(Part):
    def __init__(self):
        Part.__init__(self, "rear wheel")
        self.__fault = "seat is vibrating"

    def set_fault(self, fault):
        self.__fault = fault

    def get_fault(self):
        return self.__fault
