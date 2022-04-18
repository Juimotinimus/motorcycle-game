# File: generate_parts.py
# Author: Henri Kuoppala, Juuso Äijälä
# Description: functions to generate all the parts to motorcycle

from part import Part

def generate_parts():
    pd = {
        "front wheel assembly" : [
            Part(0, "break caliber(front)", "bike wont stop"),
            Part(1, "break pads(front)", "whining under braking"),
            Part(2, "wheel(front)", "handlebars vibrating")
            ],
        "rear wheel assembly" :[
            Part(3, "break caliber(rear)", "bike wont stop"),
            Part(4, "break pads(rear)", "whining under braking"),
            Part(5, "wheel(rear)", "squealing sound when accelerating")
            ],
        "engine & exhaust" :[
            Part(6, "starter motor", "bike wont start"),
            Part(7, "spark plug", "engine is misfiring"),
            Part(8, "exhaust pipe", "bike makes a loud popping sound")
            ],
        "drivetrain" : [
            Part(9, "drive chain", "bike feels jerky"),
            Part(10, "front sprocket", "bike vibrates"),
            Part(11, "rear sprocket", "bike vibrates")
        ]
    }
    pd["front wheel assembly"][1].add_part_to_remove(pd["front wheel assembly"][0]) #caliber before the pads
    pd["front wheel assembly"][2].add_part_to_remove(pd["front wheel assembly"][0]) #caliber before the wheel
    pd["rear wheel assembly"][1].add_part_to_remove(pd["rear wheel assembly"][0]) #caliber before pads
    pd["rear wheel assembly"][0].add_part_to_remove(pd["rear wheel assembly"][2]) #wheel before caliber
    pd["drivetrain"][1].add_part_to_remove(pd["drivetrain"][0]) #chain before sprocket
    pd["drivetrain"][2].add_part_to_remove(pd["drivetrain"][0]) #chain before sprocket
    pd["drivetrain"][2].add_part_to_remove(pd["rear wheel assembly"][2]) #wheel before rear sprocket
    return pd

def generate_list_of_parts(all_the_parts):
    pl = []
    for category in all_the_parts:
        for part in all_the_parts[category]:
            pl.append(part)
    return pl
