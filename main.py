# File: main.py
# Author: Henri Kuoppala, Juuso Äijälä
# Description: main file

import random
import motorcycle
from part import Part

def select_part_to_remove(list_of_parts):
    parts = list_of_parts
    number = 1
    for a_part in parts:
        print(f"{number}. {a_part}")
        number += 1
    while True:
        try:
            a_part = int(input(f"select what part to remove: "))
            if a_part < 1 or a_part > len(parts):
                print("invalid input")
                continue
            else:
                break
        except ValueError:
            print("invalid input")
    return parts[a_part -1]

def remove_part(a_part, bike):
    first_remove = a_part.get_parts_to_remove()
    if len(first_remove) > 0:
        for i in first_remove:
            if i.get_attached() == True:
                print(f"you must first remove {i}")
                return False
        a_part.set_attached(False)
        bike.remove_part(a_part)
        return True
    else:
        a_part.set_attached(False)
        bike.remove_part(a_part)
        return True

def inspect_part(a_part, bike):
    while True:
        inspect = input(f"do want to inspect the part? (y/n): ")
        if inspect != "y" and inspect != "n":
            print(f"invalid input")
            continue
        else:
            break
    if inspect == "y":
        if a_part.get_faulty() == True:
            print(f"this part is faulty... replacing part")
            a_part.replace()
        else:
            print(f"this part seems to be fine")
    attach_part(a_part, bike)

def attach_part(a_part, bike):
    while True:
        attach = input(f"do want to re-attach the part? (y/n): ")
        if attach != "y" and attach != "n":
            print(f"invalid input")
            continue
        else:
            break
    if attach == "y":
        a_part.set_attached(True)
        bike.add_part(a_part)

def break_part(bike):
    part = bike.get_parts()[random.randint(0, len(bike.get_parts())-1)]
    part.set_faulty(True)
    bike.set_fault(part.get_issue())

def main():

    # setting up
    my_bike = motorcycle.Motorcycle()

    break_part(my_bike)

    my_bike.check_parts()

    # game loop
    print(my_bike)
    while my_bike.get_working() == False:
        part_to_check = select_part_to_remove(my_bike.get_parts())
        if remove_part(part_to_check, my_bike) == False:
            continue
        inspect_part(part_to_check, my_bike)

        # at this part putting the bike back together needs to be implemented
        # also replacing the part is automated right now and it probably shouldn't be


        my_bike.check_parts()
        if my_bike.get_working() == True:
            print(my_bike)
            break
        else:
            continue


main()
