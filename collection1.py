#dagen opdarcht
def days():
    dagen = ['Zondag','Maandag' , 'dinsdag', 'woensdag', 'Vrijdag','Zaterdag' ]
    print(dagen)
    print(dagen[1:5])
    print(dagen[0], dagen[-1])
    dagen.reverse()
    print(dagen)
    print(dagen[0], dagen[-1])

##################################
# sum opdracht 
num = [1,2,3,4,5,6,7,8,9,10]
num2 = [2,4,6,8,10,12,14,16,18,20]
def addAndDisplayListse():
    print('==========================================')
    for i in range(len(num)):
        print(num[i],' + ', num2[i], ' = ', num[i]+num2[i])
    print('==========================================')
def multiplyAndDisplayLists():
    for i in range(len(num)):
        print(num[i],' x ', num2[i], ' = ', num[i]*num2[i])
    print('==========================================')
def substractAndDisplayLists():
    for i in range(len(num)):
        print(num[i],' / ', num2[i], ' = ', num[i]/num2[i])
    print('==========================================')
def divideAndDisplayLists():
    for i in range(len(num)):
        print(num[i],' - ', num2[i], ' = ', num[i]-num2[i])
    print('==========================================')
# addAndDisplayListse()
# multiplyAndDisplayLists()
# substractAndDisplayLists()
# divideAndDisplayLists()

####################################################
#programma opdracht 
import random
def spelProgramma(spellist,minimaal,maximaal):
    spellen = []
    number = random.randint(minimaal,maximaal)
    for i in range(number):
        spellen.append(random.choice(spellist))
    return spellen

spellist =['Monopoly','Yathzee','Bridge','Poker','Pesten','Mens erger je niet','Cluedo']
list = spelProgramma(spellist,3,10)
print(list)




