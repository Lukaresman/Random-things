import json
# TODO: irregular_verbs.json
#  vsa koda

def compare(l1, l2):
    # here l1 and l2 must be lists
    if len(l1) != len(l2):
        print("False V2")
        return False
    l1.sort()
    l2.sort()
    if l1 == l2:
        return True
    else:
        return False

list_1 = []
list_2 = []

with open("irregular_verbs.json") as f:
    ireguler_verbs_json = json.load(f)

    for i in ireguler_verbs_json:
        list_1.append(int(i))

count = 1
while count <= 80:
    list_2.append(count)
    count += 1

print(list_1)
print(list_2)
print(f"list_1 == list_2: {compare(list_1, list_2)} ")