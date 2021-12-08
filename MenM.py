import random

def MenM(amount):
    lijst = {
        'groen' : 0,
        'blauw' : 0,
        'oranje': 0,
        'bruin' : 0
    }
    kleuren = ['oranje', 'blauw', 'groen', 'bruin']
    for x in range(amount):
        lijst[random.choice(kleuren)] += 1  
    return lijst

hoeveel =int(input('hoeveel MMs wil ? '))   
print(MenM(hoeveel))

