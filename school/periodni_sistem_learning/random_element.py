import json
import random


def random_element_info():
    f = open('elementi.json', )
    elementi_json = json.load(f)
    count = 0
    random_element_num = random.randint(1, 118)
    for i in elementi_json:
        count += 1
        if count == random_element_num:
            element_symbol = i
            # element_id = elementi_json[i]["id"]
            element_name = elementi_json[i]["name"]
            print(f"{str(element_symbol).capitalize()} = {str(element_name).capitalize()}")
            # print(f"Kemijski simbol: {str(element_symbol).capitalize()}\nKemijski element: {str(element_name).capitalize()}\nAtomsko št.: {element_id}")
    # print(f"\n\n[DEBUG]\nCount: {count}\nTested number: {random_element_num}")
    # Closing file
    f.close()


def ask_for_element_name():
    f = open('elementi.json', )
    elementi_json = json.load(f)
    count = 0
    random_element_num = random.randint(1, 118)
    for i in elementi_json:
        count += 1
        if count == random_element_num:
            element_symbol = str(i)
            # element_id = int(elementi_json[i]["id"])
            element_name = str(elementi_json[i]["name"])
            if element_name == input(f"Ime za {element_symbol.capitalize()}: ").lower():
                print("Pravilno!")
            else:
                print(f"Narobe!\nRešitev: {element_symbol.capitalize()} = {element_name.capitalize()}")
    # print(f"\n\n[DEBUG]\nCount: {count}\nTested number: {random_element_num}")
    f.close()


def ask_for_element_symbol():
    f = open('elementi.json', )
    elementi_json = json.load(f)
    count = 0
    random_element_num = random.randint(1, 118)
    for i in elementi_json:
        count += 1
        if count == random_element_num:
            element_symbol = str(i)
            # element_id = int(elementi_json[i]["id"])
            element_name = str(elementi_json[i]["name"])
            if element_symbol == input(f"Kemijski simbol za {element_name.capitalize()}: ").lower():
                print("Pravilno!")
            else:
                print(f"Narobe!\nRešitev: {element_symbol.capitalize()} = {element_name.capitalize()}")
    # print(f"\n\n[DEBUG]\nCount: {count}\nTested number: {random_element_num}")
    f.close()


start_input = input("1) Prikaži podatke za naključen element\n"
                    "2) Ugotovi ime elementa glede z kemijskim simbolom\n"
                    "3) Ugotovi kemijski simbol z imenom elementa\n"
                    "Unesi število: ")
if start_input == "1":
    random_element_info()
elif start_input == "2":
    ask_for_element_name()
elif start_input == "3":
    ask_for_element_symbol()
