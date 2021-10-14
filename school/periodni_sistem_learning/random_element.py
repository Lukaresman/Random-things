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
            element_group = elementi_json[i]["group"]
            element_period = elementi_json[i]["period"]
            element_state = elementi_json[i]["state"]
            print(f"\n{str(element_symbol).capitalize()} = {str(element_name).capitalize()}\n"
                  f"Agregatno stanje: {str(element_state).capitalize()}\n\n"
                  f"Skupina: {element_group}\nPerioda: {element_period}\n\n")
    f.close()
    menu_script()


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
            element_group = elementi_json[i]["group"]
            element_period = elementi_json[i]["period"]
            if element_name == input(f"Ime za {element_symbol.capitalize()}: ").lower():
                print(f"Pravilno! Skupina: {element_group}, Perioda: {element_period}\n\n")
            else:
                print(f"Narobe!\nRešitev: {element_symbol.capitalize()} = {element_name.capitalize()},"
                      f" Skupina: {element_group}, Perioda: {element_period}\n\n")
    f.close()
    ask_for_element_name()


def ask_for_element_symbol():
    f = open('elementi.json', )
    elementi_json = json.load(f)
    count = 0
    random_element_num = random.randint(1, 118)
    for i in elementi_json:
        count += 1
        if count == random_element_num:
            element_symbol = str(i)
            element_name = str(elementi_json[i]["name"])
            element_group = elementi_json[i]["group"]
            element_period = elementi_json[i]["period"]
            if element_symbol == input(f"Kemijski simbol za {element_name.capitalize()}: ").lower():
                print(f"Pravilno! Skupina: {element_group}, Perioda: {element_period}\n\n")
            else:
                print(f"Narobe!\nRešitev: {element_symbol.capitalize()} = {element_name.capitalize()},"
                      f" Skupina: {element_group}, Perioda: {element_period}\n\n")
    f.close()
    ask_for_element_symbol()


def get_info_from_symbol():
    f = open('elementi.json', )
    elementi_json = json.load(f)
    get_element = input("Vpiši kemijski simbol elementa: ").lower()
    for i in elementi_json:
        if i == get_element:
            element_symbol = str(i)
            element_name = str(elementi_json[get_element]["name"])
            element_group = elementi_json[i]["group"]
            element_period = elementi_json[i]["period"]
            element_state = str(elementi_json[i]["state"])
            print(f"{element_symbol.capitalize()} = {element_name.capitalize()},\n"
                  f"Agregatno stanje: {element_state.capitalize()}"
                  f" Skupina: {element_group}, Perioda: {element_period}\n\n")
    f.close()
    menu_script()


def get_info_from_name():
    f = open('elementi.json', )
    elementi_json = json.load(f)
    get_element = input("Vpiši ime elementa: ").lower()
    for i in elementi_json:
        if elementi_json[i]["name"] == get_element:
            element_symbol = str(i)
            element_name = str(elementi_json[i]["name"])
            element_group = elementi_json[i]["group"]
            element_period = elementi_json[i]["period"]
            element_state = str(elementi_json[i]["state"])
            print(f"{element_symbol.capitalize()} = {element_name.capitalize()},\n"
                  f"Agregatno stanje: {element_state.capitalize()}"
                  f" Skupina: {element_group}, Perioda: {element_period}\n\n")
    f.close()
    menu_script()


def menu_script():
    start_input = input("1) Prikaži podatke za naključen element\n"
                        "2) Ugotovi ime elementa glede z kemijskim simbolom\n"
                        "3) Ugotovi kemijski simbol z imenom elementa\n"
                        "4) Dobi informacije o elementu z kemijskim simbolom\n"
                        "5) Dobi informacije o elementu z imenom elementa\n"
                        "Unesi število: ")
    if start_input == "1":
        random_element_info()
    elif start_input == "2":
        ask_for_element_name()
    elif start_input == "3":
        ask_for_element_symbol()
    elif start_input == "4":
        get_info_from_symbol()
    elif start_input == "5":
        get_info_from_name()
    else:
        print("\nUnesi eno od dovoljenih vrednosti (1,2,3,4,5)\n")
        menu_script()


menu_script()
