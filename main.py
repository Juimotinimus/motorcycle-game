# File: main.py
# Author: Henri Kuoppala, Juuso Äijälä
# Description: main file

import sys
import motorcycle

sys.path.insert(1, "./parts/parent_parts")
from part import Part
sys.path.insert(1, "./parts/child_parts")
from front_wheel import Front_Wheel
from rear_wheel import Rear_Wheel

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

def remove_part(a_part, list_of_parts, list_of_removed_parts):
    first_remove = a_part.get_parts_to_remove()
    if len(first_remove) > 0:
        for i in first_remove:
            if i.get_attached() == True:
                print(f"you must first remove {i}")
                return False
        a_part.set_attached(False)
        list_of_parts.remove(a_part)
        list_of_removed_parts.append(a_part)
        return True
    else:
        a_part.set_attached(False)
        list_of_parts.remove(a_part)
        list_of_removed_parts.append(a_part)
        return True

def inspect_part(a_part, list_of_parts, list_of_removed_parts):
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
    attach_part(a_part, list_of_parts, list_of_removed_parts)


# The Motorcycle class itself should have attributes for attached and non-attached parts!!! Pending...

def attach_part(a_part, list_of_parts, list_of_removed_parts):
    while True:
        attach = input(f"do want to re-attach the part? (y/n): ")
        if attach != "y" and attach != "n":
            print(f"invalid input")
            continue
        else:
            break
    if attach == "y":
        a_part.set_attached(True)
        list_of_removed_parts.remove(a_part)
        list_of_parts.append(a_part)

def main():

    # setting up
    my_bike = motorcycle.Motorcycle()

    b_caliber_front = Part("break caliber(front)")
    b_pads_front = Part("break pads(front)")
    wheel_front = Front_Wheel()
    wheel_rear = Rear_Wheel()

    b_pads_front.add_part_to_remove(b_caliber_front)
    wheel_front.add_part_to_remove(b_caliber_front)

    #THESE TWO WILL CHANGE THE FAULTY PART
    wheel_front.set_faulty(True)
    my_bike.set_fault(wheel_front.get_fault())
    #THESE TWO WILL CHANGE THE FAULTY PART

    part_list = []
    part_list.append(b_caliber_front)
    part_list.append(b_pads_front)
    part_list.append(wheel_front)
    part_list.append(wheel_rear)

    removed_part_list = []

    my_bike.set_parts(part_list)

    my_bike.check_parts()

    # game loop
    print(my_bike)
    while my_bike.get_working() == False:
        part_to_check = select_part_to_remove(part_list)
        if remove_part(part_to_check, part_list, removed_part_list) == False:
            continue
        inspect_part(part_to_check, part_list, removed_part_list)

        # at this part putting the bike back together needs to be implemented
        # also replacing the part is automated right now and it probably shouldn't be


        my_bike.check_parts()
        if my_bike.get_working() == True:
            print(my_bike)
            break
        else:
            continue


main()
