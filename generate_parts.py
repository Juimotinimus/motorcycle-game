# File: generate_parts.py
# Author: Henri Kuoppala, Juuso Äijälä
# Description: functions to generate all the parts to motorcycle

from part import Part

def generate_parts():
    pd = {
        "front wheel assembly" :[
            Part(0, "brake caliper(front)", "bike wont stop"),
            Part(1, "brake pads(front)", "whining under braking"),
            Part(2, "wheel(front)", "handlebars vibrating")
            ],
        "rear wheel assembly" :[
            Part(3, "brake caliper(rear)", "rear locks up"),
            Part(4, "brake pads(rear)", "whining under braking"),
            Part(5, "wheel(rear)", "squealing sound when accelerating")
            ],
        "engine & exhaust" :[
            Part(6, "starter motor", "bike wont start"),
            Part(7, "spark plug", "engine is misfiring"),
            Part(8, "exhaust pipe", "bike makes a loud popping sound"),
            Part(9, "battery", "no ignition"),
            Part(10, "carburetor", "bike stalls after starting"),
            Part(11, "air filter", "bike stalls after starting")
            ],
        "drivetrain" :[
            Part(12, "drive chain", "bike feels jerky"),
            Part(13, "front sprocket", "loud noise and loss of power under acceleration"),
            Part(14, "rear sprocket", "loud noise and loss of power under acceleration")
        ],
        "instruments" :[
            Part(15, "throttle handle", "bike wont rev up"),
            Part(16, "clutch lever", "bike won't move forwards"),
            Part(17, "brake lever", "bike wont stop"),
            Part(18, "brake pedal", "rear locks up"),
            Part(19, "gear shifter", "bike wont go to gear")
        ]
    }
    pd["front wheel assembly"][1].add_part_to_remove(pd["front wheel assembly"][0]) #caliper before the pads
    pd["front wheel assembly"][2].add_part_to_remove(pd["front wheel assembly"][0]) #caliper before the wheel
    pd["rear wheel assembly"][1].add_part_to_remove(pd["rear wheel assembly"][0]) #caliper before pads
    pd["rear wheel assembly"][0].add_part_to_remove(pd["rear wheel assembly"][2]) #wheel before caliper
    pd["drivetrain"][1].add_part_to_remove(pd["drivetrain"][0]) #chain before sprocket
    pd["drivetrain"][2].add_part_to_remove(pd["drivetrain"][0]) #chain before sprocket
    pd["drivetrain"][2].add_part_to_remove(pd["rear wheel assembly"][2]) #wheel before rear sprocket
    pd["engine & exhaust"][4].add_part_to_remove(pd["engine & exhaust"][5]) #air filter before carburetor
    return pd

def generate_list_of_parts(all_the_parts):
    pl = []
    for category in all_the_parts:
        for part in all_the_parts[category]:
            pl.append(part)
    return pl
