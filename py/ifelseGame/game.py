import os

print('Welcome to neverland')

print('you fall from the sky and break both legs, you hear wolves in the distance')
 
print('1. You can crawl to the nearest weapon a rock for safety')
print('2. Or you can crawl up the nearest tree')
print('what to do')

def inputFunc():
    val = input()
    return int(val)

def clear():
    os.system('clear')

scene1Ans = inputFunc()

if scene1Ans == 1:
    clear()
    print('you picked up a small rock for safety')
    print('the wolves are approaching and your weapon doesnt seem very helpful now')
    print('1. do you want to play dead?')
    print('2. Fight for your life')
    scene2Ans = inputFunc()
    
    if scene2Ans == 1:
        clear()
        print('You play dead!')
        print('The wolves eat you alive.')
        print('The End')
    elif scene2Ans == 2:

        print('You choose to fight')
        print('2 hours pass youve killed 2 and there are 3 remaining')
        print('but your too tired to carry on and you die a warriors death')

elif scene1Ans == 2:
    print('You climbed up the tree')
    print('you see the horizon in the distance')
    print('A settlement to the west')
    
else:
    print('Issue with input, enter valid value')


