import json
import random


def clean_temp_scores():
    with open(f"score.json") as f:
        score_json = json.load(f)

    for i in score_json["current_scores"]:
        score_json["current_scores"][i] = 0

    json_object = json.dumps(score_json, indent=4)
    with open(f"score.json", "w") as outfile:
        outfile.write(json_object)


def reset_ask_for_element_name():
    print("\nScore reset!\n")
    clean_temp_scores()
    ask_for_element_name()


def reset_ask_for_element_symbol():
    print("\nScore reset!\n")
    clean_temp_scores()
    ask_for_element_symbol()


def random_element_info():
    f = open('elementi.json', )
    elementi_json = json.load(f)
    count = 0
    random_element_num = random.randint(1, 118)
    for i in elementi_json:
        count += 1
        if count == random_element_num:
            element_symbol = i
            element_name = elementi_json[i]["name"]
            element_group = elementi_json[i]["group"]
            element_period = elementi_json[i]["period"]
            element_state = elementi_json[i]["state"]
            print(f"\n{str(element_symbol).capitalize()} = {str(element_name).capitalize()}\n"
                  f"Agregatno stanje: {str(element_state).capitalize()}\n\n"
                  f"Skupina: {element_group}\nPerioda: {element_period}\n\n")
    f.close()
    elementi_menu_script()


def ask_for_element_name():
    with open(f"score.json") as f:
        score_json = json.load(f)
    f = open('elementi.json')
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
            current_correct = score_json["current_scores"]["ask_for_element_name_correct"]
            current_total = score_json["current_scores"]["ask_for_element_name_correct"] + \
                            score_json["current_scores"]["ask_for_element_name_fail"]
            user_input = input(f"Ime za {element_symbol.capitalize()}: ").lower()
            if user_input == "exit":
                elementi_menu_script()
            elif user_input == "kill":
                return
            elif user_input == "reset":
                reset_ask_for_element_name()
            elif element_name == user_input:
                print(f"Pravilno! Skupina: {element_group}, Perioda: {element_period} ({current_correct + 1}"
                      f"/{current_total + 1})\n\n")
                score_json["current_scores"]["ask_for_element_name_correct"] += 1
                if score_json["current_scores"]["ask_for_element_name_fail"] == 0 and score_json["current_scores"][
                    "ask_for_element_name_correct"] > score_json["best_score"]["ask_for_element_name"]:
                    score_json["best_score"]["ask_for_element_name"] = score_json["current_scores"][
                        "ask_for_element_name_correct"]

            else:
                print(f"Narobe!\nRešitev: {element_symbol.capitalize()} = {element_name.capitalize()},"
                      f" Skupina: {element_group}, Perioda: {element_period} ({current_correct}/{current_total + 1})\n\n")
                score_json["current_scores"]["ask_for_element_name_fail"] += 1
    json_object = json.dumps(score_json, indent=4)
    with open(f"score.json", "w") as outfile:
        outfile.write(json_object)
    f.close()
    ask_for_element_name()


def ask_for_element_symbol():
    with open(f"score.json") as f:
        score_json = json.load(f)
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
            current_correct = score_json["current_scores"]["ask_for_element_symbol_correct"]
            current_total = score_json["current_scores"]["ask_for_element_symbol_correct"] + score_json["current_scores"]["ask_for_element_symbol_fail"]
            user_input = input(f"Kemijski simbol za {element_name.capitalize()}: ").lower()
            if user_input == "exit":
                elementi_menu_script()
            elif user_input == "kill":
                return
            elif user_input == "reset":
                reset_ask_for_element_symbol()
            elif element_symbol == user_input:
                print(f"Pravilno! Skupina: {element_group}, Perioda: {element_period} ({current_correct + 1}/{current_total + 1})\n\n")
                score_json["current_scores"]["ask_for_element_symbol_correct"] += 1
                if score_json["current_scores"]["ask_for_element_symbol_fail"] == 0 and score_json["current_scores"][
                    "ask_for_element_symbol_correct"] > score_json["best_score"]["ask_for_element_symbol"]:
                    score_json["best_score"]["ask_for_element_symbol"] = score_json["current_scores"][
                        "ask_for_element_symbol_correct"]
            else:
                print(f"Narobe!\nRešitev: {element_symbol.capitalize()} = {element_name.capitalize()},"
                      f" Skupina: {element_group}, Perioda: {element_period} ({current_correct}/{current_total + 1})\n\n")
                score_json["current_scores"]["ask_for_element_symbol_fail"] += 1
    json_object = json.dumps(score_json, indent=4)
    with open(f"score.json", "w") as outfile:
        outfile.write(json_object)
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
    elementi_menu_script()


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
    elementi_menu_script()


def elementi_menu_script():
    clean_temp_scores()
    start_input = input("1) Prikaži podatke za naključen element\n"
                        "2) Ugotovi ime elementa z kemijskim simbolom\n"
                        "3) Ugotovi kemijski simbol z imenom elementa\n"
                        "4) Dobi informacije o elementu z kemijskim simbolom\n"
                        "5) Dobi informacije o elementu z imenom elementa\n"
                        "6) Show highest streak\n"
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
    elif start_input == "6":
        with open(f"score.json") as f:
            score_json = json.load(f)
        best_ask_for_element_name = score_json["best_score"]["ask_for_element_name"]
        best_ask_for_element_symbol = score_json["best_score"]["ask_for_element_symbol"]
        print(f"\nUgotovi ime elementa z kemijskim simbolom: {best_ask_for_element_symbol}\n"
              f"Ugotovi kemijski simbol z imenom elementa: {best_ask_for_element_name}\n")
        elementi_menu_script()
    elif start_input == "kill":
        return
    else:
        print("\nUnesi eno od dovoljenih vrednosti (1,2,3,4,5)\n")
        elementi_menu_script()


elementi_menu_script()
