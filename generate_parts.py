# File: generate_parts.py
# Author: Henri Kuoppala, Juuso Äijälä
# Description: function to generate all the parts to motorcycle

from part import Part

def generate_parts():
    pl = [
    Part(0,"break caliber(front)", "bike wont stop"),
    Part(1,"break pads(front)", "whining under braking"),
    Part(2,"wheel(front)","handlebars vibrating")
    ]
    pl[1].add_part_to_remove(pl[0]) #caliber before the pads
    pl[2].add_part_to_remove(pl[0]) #caliber before the wheel
    return pl
