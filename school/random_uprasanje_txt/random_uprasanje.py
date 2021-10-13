import random


def getuprasanje():
    uprasanje = random.choice(open('uprasanja.txt').readlines())
    if any((c.isalpha()) or (c.isnumeric()) for c in uprasanje):
        print(uprasanje)
    else:
        getuprasanje()


getuprasanje()
