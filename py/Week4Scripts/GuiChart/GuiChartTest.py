import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


message=''
def receive():
    """Handles receiving of messages."""
    while True:
        try:
            global msg_list
            msg_list = []
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.append(msg)
            window['msg'].update(msg_list)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = message
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{end}":
        client_socket.close()
        window.close()


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    msg = "{end}"
    send()

fig = matplotlib.figure.Figure(figsize=(3, 2), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

# Define the window layout
layout = [
    [sg.Text("Plot test")],
    [sg.Canvas(key="-CANVAS-")],
    [sg.Text('Chat Below', size=(20,2))],
    [sg.Text('',key='msg', size=(50,3))],
    [sg.Input(key='choice', do_not_clear=False)],
    [sg.Button("Ok", key='Send')],
]

matplotlib.use("TkAgg")

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg


# Create the form and show it without the plot
window = sg.Window(
    "Matplotlib Single Graph",
    layout,
    location=(0, 0),
    finalize=True,
    element_justification="center",
    font="Helvetica 18",
)

# ----Now comes the sockets part----
# HOST = input('Enter host: ')
# PORT = input('Enter port: ')
HOST = ""
PORT = 33000
if not HOST:
    HOST = '127.0.0.1'
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()

# Add the plot to the window
draw_figure(window["-CANVAS-"].TKCanvas, fig)

while True:  # on the path str
    # Event Loop
    event, values = window.read()
    print(event, values)
    window['msg'].update(msg_list)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Send':
        global my_msg
        my_msg = values['choice']
        message = my_msg
        send()
        print(my_msg)

window.close()
