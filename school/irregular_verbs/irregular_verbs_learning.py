import json
import random
# TODO: irregular_verbs.json

def ask_for_past_simple():
    f = open(f'irregular_verbs.json')
    verbs_json = json.load(f)
    count = 0
    random_num = random.randint(1, 34)
    for i in verbs_json:
        # if int(i) >= 38:
            # return
        count += 1
        if count == random_num:
            # verb_id = str(i)
            verb_infinitive = str(verbs_json[i]["infinitive"])
            verb_past_simple = verbs_json[i]["past_simple"]
            verb_si = verbs_json[i]["si_meaning"]
            user_input = input(f"Past simple for {verb_infinitive.capitalize()}: ").lower()
            # if user_input == "exit":
                # elementi_menu_script()
            if user_input == "kill":
                return
            elif verb_past_simple == user_input:
                print(f"Pravilno! Pomen: {verb_si}\n\n")
            else:
                print(f"Narobe!\nRešitev: {verb_infinitive.capitalize()} = {verb_past_simple.capitalize()},"
                      f" Pomen: {verb_si}\n\n")
    f.close()
    ask_for_past_simple()

def verbs_menu_script():
    start_input = input("1) Uprašaj po past simple.\n"
                        "Unesi število: ")
    if start_input == "1":
        ask_for_past_simple()
    elif start_input == "kill":
        return
    else:
        print("\nUnesi eno od dovoljenih vrednosti (1)\n")
        verbs_menu_script()


verbs_menu_script()