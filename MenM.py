import random
def MenM(amount):
    lijst = []
    kleuren = ['oranje', 'blauw', 'groen', 'bruin']
    for x in range(amount):
        lijst.append(random.choice(kleuren))
    return lijst
hoeveel =int(input('hoeveel MMs wil ? '))   
print(MenM(hoeveel))
