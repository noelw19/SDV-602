# Working with the pySimpleGui Framework

So the framework seems quite simple and is in fact quite fun to use, the items that are stored within the gui window are added to a variable named layout, it includes a list that hold the components and the values that are needed for the application.(nested lists)

To initialise the window, run the PySimpleGui.Window() method with 2 arguements, the first being the title of the window and the second being the nested lists variable name which in this case is 'layout'.

You are able to use the key property within the component methods to allow you to use the key names to change the values of the components, have mainly used it on only text components but i beleive this functionality could be spread further than just the text component.

## PySimpleGui Setup
`import PySimpleGUI as sg

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
window = sg.Window('THE MIND PALACE', layout)`

## Dynamically updating content
`window['storyLine'].update('You look around the room and find a hair pin,\n '
                    'you could use it to unlock a door sometime'                                    'You jump for joy and stumble, falling out the window!!')
        window['Q1'].update('1. Try to grab on to something')
        window['Q2'].update('2. Cry out for help before you hit the ground')`

The code above looks into the window object, then within the square brackets we enter the value we entered for the key property and then with the update method on the end we are able to dynamically change the rendered values.


