# File: main.py
# Author: Henri Kuoppala, Juuso Äijälä
# Description: main file

import motorcycle
import part

def select_part_to_remove(motorcycle):
    parts = motorcycle.get_parts()
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
    return motorcycle.get_parts()[a_part -1]

def remove_part(a_part):
    first_remove = a_part.get_parts_to_remove()
    if len(first_remove) > 0:
        for i in first_remove:
            if i.get_attached() == True:
                print(f"you must first remove {i}")
                return False
    else:
        a_part.set_attached(False)
        return True

def inspect_part(a_part):
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


def main():

    # setting up
    my_bike = motorcycle.Motorcycle()

    b_caliber_front = part.Part("break caliber(front)")
    b_pads_front = part.Part("break pads(front)")

    b_pads_front.set_faulty(True)
    b_pads_front.add_part_to_remove(b_caliber_front)

    my_bike.set_fault("the front break is sloppy")

    part_list = []
    part_list.append(b_caliber_front)
    part_list.append(b_pads_front)

    my_bike.set_parts(part_list)

    my_bike.check_parts()

    # game loop
    while my_bike.get_working() == False:
        print(my_bike)
        part_to_check = select_part_to_remove(my_bike)
        if remove_part(part_to_check) == False:
            continue
        inspect_part(part_to_check)
        
        # at this part putting the bike back together needs to be implemented
        # also replacing the part is automated right now and it probably shouldn't be


        my_bike.check_parts()
        if my_bike.get_working() == True:
            print(my_bike)
            break
        else:
            continue


main()