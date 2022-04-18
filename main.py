# File: main.py
# Author: Henri Kuoppala, Juuso Äijälä
# Description: main file

import random
import motorcycle
from part import Part

def select_part(dict_of_parts):
    print("\n===========================================")
    number = 1
    cl = []
    for category in dict_of_parts:
        print(f"{number}. {category}")
        number += 1
        cl.append(category)
    while True:
        try:
            user_input = int(input(f"====================\nselect a category: "))
            if user_input < 1 or user_input > number -1:
                print("invalid input")
                continue
            else:
                number = 1
                break
        except ValueError:
            print("invalid input")
            continue
    category = cl[user_input -1]
    print("====================\n")
    for a_part in dict_of_parts[category]:
        print(f"{number}. {a_part}")
        number += 1
    while True:
        try:
            user_input = int(input(f"================\nselect a part: "))
            if user_input < 1 or user_input > number -1:
                print("invalid input")
                continue
            else:
                number = 1
                break
        except ValueError:
            print("invalid input")
            continue
    print("================\n")
    selected_part = dict_of_parts[category][user_input -1]
    return selected_part

def remove_part(a_part, bike):
    while True:
        remove = input(f"do want to remove the part? (y/n): ")
        if remove != "y" and inspect != "n":
            print(f"invalid input")
            continue
        else:
            break
    if remove == "n":
        return False
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

def check_bike(bike):
    while True:
        check = input(f"do want to check if the bike works? (y/n): ")
        if check != "y" and check != "n":
            print(f"invalid input")
            continue
        else:
            break
    if check == "n":
        return False
    else:
        if len(bike.get_removed_parts()) > 0:
            print(f"the bike can't be tested... the following parts need to be installed first:")
            for part in bike.get_removed_parts():
                print(part)
            return False
        else:
            bike.check_parts()
            if bike.get_working() == True:
                print(bike)
                return True
            else:
                print(bike)
                return False
        

def main():

    # setting up
    my_bike = motorcycle.Motorcycle()

    break_part(my_bike)

    my_bike.check_parts()

    # game loop
    print("===========================================\n||            r==                        ||\n||        _  //                          ||\n||       |_)//(''''':                    ||\n||         //  \_____:_____.-----.P      ||\n||        //   | ===  |   /        \     ||\n||    .:'//.   \ \=|   \ /  .:'':.       ||\n||   :' // ':   \ \ ''..'--:'-.. ':      ||\n||   '. '' .'    \:.....:--'.-'' .'      ||\n||    ':..:'                ':..:'       ||\n===========================================\n")
    print(my_bike)
    while my_bike.get_working() == False:
        part_to_check = select_part(my_bike.get_categories())
        if part_to_check.get_attached() == True:
            if remove_part(part_to_check, my_bike) == False:
                continue
            inspect_part(part_to_check, my_bike)
        else:
            inspect_part(part_to_check, my_bike)
        check_bike(my_bike)

main()
