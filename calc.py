import PySimpleGUI as psg

# --------------------------------- Variables -------------------------------- #
entry = '0'

# --------------------------------- Functions -------------------------------- #
def addEntry(n):
    global entry
    if entry == '0':
        entry = n
    else:
        entry += n

def backspace():
    global entry
    entry = entry[:-1]

def clearNumber():
    global entry
    entry = '0'

def evaluate():
    global entry
    try:
        entry = str(round(float(eval(entry)), 3))
        if int(entry.split('.')[1]) == 0:
            entry = entry.split('.')[0]
    except:
        entry = "ERR"

# ---------------------------------- Layout ---------------------------------- #
layout = [
    [psg.Text(text=entry, key='in', font=('Helvetica', 20), justification='right', expand_x=True, enable_events=True)],
    [psg.Button('C', size=(5,2), expand_x=True), psg.Button('<=', size=(5,2)), psg.Button('/', size=(5,2))],
    [psg.Button('7', size=(5,2)), psg.Button('8', size=(5,2)), psg.Button('9', size=(5,2)), psg.Button('x', size=(5,2))],
    [psg.Button('4', size=(5,2)), psg.Button('5', size=(5,2)), psg.Button('6', size=(5,2)), psg.Button('+', size=(5,2))],
    [psg.Button('1', size=(5,2)), psg.Button('2', size=(5,2)), psg.Button('3', size=(5,2)), psg.Button('-', size=(5,2))],
    [psg.Button('0', size=(5,2), expand_x=True), psg.Button('.', size=(5,2)), psg.Button('=', size=(5,2))]
]

# ---------------------------------- Window ---------------------------------- #
window = psg.Window(title="Calculator", layout=layout, element_padding=(0,0), font=('Helvetica', 14),return_keyboard_events=True)

# ---------------------------------- Events ---------------------------------- #
while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED:
        break
    
    elif event == '0':
        addEntry('0')
    elif event == '1':
        addEntry('1')
    elif event == '2':
        addEntry('2')
    elif event == '3':
        addEntry('3')
    elif event == '4':
        addEntry('4')
    elif event == '5':
        addEntry('5')
    elif event == '6':
        addEntry('6')
    elif event == '7':
        addEntry('7')
    elif event == '8':
        addEntry('8')
    elif event == '9':
        addEntry('9')

    elif event in ('<=', 'BackSpace:855638143'):
        backspace()
    elif event in ('C', 'Escape:889192475'):
        clearNumber()
    elif event == '.':
        addEntry('0.')

    elif event == '+':
        addEntry(' + ')
    elif event == '-':
        addEntry(' - ')
    elif event in ('x', '*'):
        addEntry(' * ')
    elif event == '/':
        addEntry(' / ')

    elif event in ('=', 'Return:603979789'):
        evaluate()

    # print(event)

    window['in'].update(entry)

window.close()