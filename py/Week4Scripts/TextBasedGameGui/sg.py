import PySimpleGUI as sg
import time

sg.theme('Dark Blue 3')  # please make your windows colorful
layout = [[sg.Text('Choose one of the options below and live your destiny:', justification='center')],
          [sg.Text('You wake up in a white room with gold trim, \n'
                   'out the window the morning sun creeps across the horizon.. \nWhere the heck am I?',
                   key='storyLine', size=(50, 7))],
          [sg.Text('', key='error', size=(20,1))],
          [sg.Text('What do you want to do?', key='Q0')],
          [sg.Text('1. Check the door?', key='Q1', size=(60, 2))],
          [sg.Text('2. Look around?', key='Q2', size=(60, 2))],
          [sg.Input(key='choice', do_not_clear=False)],
          [sg.Button('Show'), sg.Button('Back'), sg.Button('Exit')]]
window = sg.Window('THE MIND PALACE', layout)
global clientChoice
clientChoice = 0
global path
path = ''


def resetchoice():
    values['choice'] = 0
# goes as follows the staring is 0
# path is as follows, the choice you make is appended to a string which will serve as the path variable
# '12' means the client chose option 1 then 2 and so on. could add a back button with the use of a pop function


def statements(p, c):
    if p == '' and c == 1:
        resetchoice()
        window['storyLine'].update('You open the door and an amazing theatre lies within, \n'
                                    'A showing of pinochio rumbles on down the other end.')
        window['Q1'].update('1. Hold pinochio hostage and ask for a ransom')
        window['Q2'].update('2. Examine room')
        scene = 10
        p = p + '1'
        c = 0
        return p, c
    if p == '' and c == 2:
        resetchoice()
        window['storyLine'].update('You look around the room and find a hair pin,\n '
                                    'you could use it to unlock a door sometime.\n\n'
                                    'You jump for joy and stumble, falling out the window!!')
        window['Q1'].update('1. Try to grab on to something')
        window['Q2'].update('2. Cry out for help before you hit the ground')
        scene = 20
        p = p + '2'
        c = 0
        return p, c
    # A and b for the first question children
    if p == '1' and c == 1:
        resetchoice()
        window['storyLine'].update('You grab pinochio by the nose and begin running down the room,\n'
                                    'angry theatre goers chase you down. \n\n'
                                    'pinochio shrieks with terror! ')
        window['Q1'].update('1. Take the bird exit, left door')
        window['Q2'].update('2. Take same room.')
        p = p + '1'
        c = 0
        return p, c
    # if path is 11 and the choice is 2
    if p == '11' and c == 2:
        resetchoice()
        window['storyLine'].update('You run into the white room, its now empty, no windows and nowhere to hide..\n\n'
                                   'Pinochio tries to bargain with you for his life, saying let him go in '
                                   'exchange for the biggest secret that has ever been told....')
        window['Q1'].update('1. Whats the secret?')
        window['Q2'].update('')
        p = p + '2'
        c = 0
        return p, c
    if p == '112' and c == 1:
        resetchoice()
        window['storyLine'].update('Pinochio leans over and tells you...\n\n'
                                   'Life is always meant to be hard!\n\n'
                                   'A beam of light appears and swallows you, just before you disapear you '
                                   'see his nose begin to grow.....')
        window['Q0'].update('END OF GAME')
        window['Q1'].update('')
        window['Q2'].update('')
        c = 0
        return p, c
    if p == '1' and c == 2:
        resetchoice()
        window['storyLine'].update('Theres a door on the right, people watching the show,\n '
                                   'and a you see a line in the wall that looks like a door!!!\n'
                                   'Is this a secret door?')
        window['Q1'].update('1. Try it out')
        window['Q2'].update('')
        p = p + '2'
        c = 0
        return p, c
    if p == '2' and c == 1:
        resetchoice()
        window['storyLine'].update('You try to grab something but you have slow reflexes and grabbed at the air'
                                    'long after you had any reach.\n'
                                    'but you realise your not falling....\n\n'
                                    'your floating!')
        window['Q1'].update('1. Swim in the air!')
        window['Q2'].update('')
        p = p + '1'
        c = 0
        return p, c
    # End screen for scream for help
    if p == '2' and c == 2:
        resetchoice()
        window['storyLine'].update('You scream at the top of your lungs, you feel the adrenaline rush through you as'
                                   'you plummet toward the ground.'
                                   'Your still alive, the feeling of agony shoots through your body.\n'
                                   'You cant move and no one is around to help you.\nIs this a dream?')
        window['Q0'].update('End of game!')
        window['Q1'].update('')
        window['Q2'].update('')
        p = p + '1'
        c = 0
        return p, c
    # A and b for the b 2nd question children
    if p == '11' and c == 1:
        resetchoice()
        window['storyLine'].update('You take the bird exit, only to realise its a strraight drop to the ground!\n'
                                    'You and pinochio both scream, just as you feel your face touch'
                                    ' the cement...\n\nYou wake up, safe and sound in your bed.')
        window['Q0'].update('END OF GAME.')
        window['Q1'].update('')
        window['Q2'].update('')
        c = 0
        return p, c
    if p == '12' and c == 1:
        resetchoice()
        window['storyLine'].update('You open the secret door, just as the light breaches the room,\n'
                                    'you wake up safe and sounds in your bed.')
        window['Q0'].update('END OF GAME.')
        window['Q1'].update('')
        window['Q2'].update('')
        c = 0
        return p, c
    if p == '21' and c == 1:
        resetchoice()
        window['storyLine'].update('You swim though the air like a fish in the sea...\n'
                                   'You notice you cant swim back down.. you float higher and higher till'
                                   'the earth is no longer visible and drift in space for the remainder of your life.')
        window['Q0'].update('END OF GAME.')
        window['Q1'].update('')
        window['Q2'].update('')
        c = 0
        return p, c

while True:  # on the path str
    # Event Loop
    event, values = window.read()
    print(event, values)
    window['Q0'].update('')
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    #     The back button only seems to work when it is used on one of the end screens,
    # maybe because i mutate the path and then return it through the function? unsure at this point
    if event == 'Back':
        theList = list(path)
        clientChoice = int(theList.pop())
        print(type(clientChoice), clientChoice)
        res = ''
        for x in theList:
            res = res + str(x)
        path = res
        print(type(path), path)
        event = 'Show'
        values['choice'] = str(clientChoice)
        pathvar, clientVar = statements(path, clientChoice)
        path = pathvar
        clientChoice = clientVar
        continue
    if str(values['choice']) != str(1) and str(values['choice']) != str(2):
        window['error'].update('Error: Enter a valid choice!')
        continue
    elif int(values['choice']) == 1 or int(values['choice']) == 2:
        window['error'].update('')
        clientChoice = int(values['choice'])
    if values['choice'] == 'undefined':
        continue
    if event == 'Show':
        pathvar, clientVar = statements(path, clientChoice)
        path = pathvar
        clientChoice = clientVar
window.close()
