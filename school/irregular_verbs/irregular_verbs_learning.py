import json
import random
# TODO: add items to irregular_verbs.json


def debug_count():
    f = open(f'irregular_verbs.json')
    verbs_json = json.load(f)
    count = 0
    for i in verbs_json:
        if verbs_json[i]["similarities"] != 0:
            # print(f"DEBUG: count = {count}; i = {i}")
            pass
        else:
            print(f"DEBUG: count = {count}; i = {i}")
            return
        count += 1


def ask_for_past_simple():
    f = open(f'irregular_verbs.json')
    verbs_json = json.load(f)
    count = 0
    random_num = random.randint(1, 49)
    for i in verbs_json:
        count += 1
        if count == random_num:
            verb_infinitive = str(verbs_json[i]["infinitive"])
            verb_past_simple = verbs_json[i]["past_simple"]
            verb_si = verbs_json[i]["si_meaning"]
            user_input = input(f"Past simple for {verb_infinitive.capitalize()}: ").lower()
            if user_input == "exit":
                verbs_menu_script()
            elif user_input == "kill":
                return
            elif verb_past_simple == user_input:
                print(f"Pravilno! Pomen: {verb_si}\n\n")
            else:
                print(f"Narobe!\nRešitev: {verb_infinitive.capitalize()} = {verb_past_simple.capitalize()},"
                      f" Pomen: {verb_si}\n\n")
    f.close()
    ask_for_past_simple()


def get_verb_info():
    f = open(f'irregular_verbs.json')
    verbs_json = json.load(f)
    user_input = input("Input verb: ")
    if user_input == "kill":
        return
    elif user_input == "exit":
        verbs_menu_script()
    for i in verbs_json:
        verb_infinitive = str(verbs_json[i]["infinitive"])
        verb_past_simple = verbs_json[i]["past_simple"]
        verb_past_principle = verbs_json[i]["past_participle"]
        if user_input in (verb_infinitive, verb_past_principle, verb_past_simple):
            verb_si = verbs_json[i]["si_meaning"]
            print(f"Info for {user_input.capitalize()}:\n"
                  f"    Infinitive: {verb_infinitive} \n"
                  f"        Pronunciation: https://dictionary.cambridge.org/dictionary/english/{verb_infinitive}\n"
                  f"    Past Simple: {verb_past_simple}\n"
                  f"        Pronunciation: https://dictionary.cambridge.org/dictionary/english/{verb_past_simple}\n"
                  f"    Past Participle: {verb_past_principle}\n"
                  f"        Pronunciation: https://dictionary.cambridge.org/dictionary/english/{verb_past_principle}\n"
                  f"    SI meaning: {verb_si}\n"
                  )
    f.close()


def verbs_menu_script():
    start_input = input("1) Uprašaj po past simple.\n"
                        "2) Get info for verb."
                        "Unesi število: ")
    if start_input == "1":
        ask_for_past_simple()
    elif start_input == "2":
        get_verb_info()
    elif start_input == "kill":
        return
    else:
        print("\nUnesi eno od dovoljenih vrednosti (1)\n")
        verbs_menu_script()


verbs_menu_script()
