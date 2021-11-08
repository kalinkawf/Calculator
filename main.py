from tkinter import *
from decimal import *
from math import *
from time import *
import time

#okno tkinter
window = Tk()
window.title('Calculator')
window.configure(background="white")

#przyciski kalkulatora
buttons = (('7', '8', '9', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '=', '+', '4'))
styl = 1
#zegar analogowy

#def drawcircle(Alpha, Beta, Rayon, kolor, can):
#    x1,y1,x2,y2=Alpha-Rayon, Beta-Rayon, Alpha+Rayon, Beta+Rayon
#    can.create_oval(x1, y1, x2, y2, fill = kolor)

#def drawPetAig(CoordA, CoordZ, rozm, Omega, can):
#    Pi = 3.141592
#    Omega = ((Omega/60)+1)*30
#    can.create_line(CoordA + (rozm / 3) * cos(Pi * (Omega / 180)), CoordZ + (rozm / 3) * sin(Pi * (Omega / 180)), CoordA - (rozm / 8) * cos(Pi * (Omega / 180)), CoordZ - (rozm / 8) * sin(Pi * (Omega / 180)), fill ="green")

#def drawGrdAig(CoordA, CoordZ, rozm, Omega, can): #function to draw the minute hand, based on center coord and minutes.
#    Pi = 3.141592
#    Omega = (Omega-15)*6
#    can.create_line(CoordA + (rozm / 1.5) * cos(Pi * (Omega / 180)), CoordZ + (rozm / 1.5) * sin(Pi * (Omega / 180)), CoordA - (rozm / 6) * cos(Pi * (Omega / 180)), CoordZ - (rozm / 6) * sin(Pi * (Omega / 180)), fill ="blue")

#def drawSecAig(CoordA, CoordZ, rozm, Omega, can): #function to draw the hour hand
#    Pi = 3.141592
#    Omega = (Omega-15) *6
#    can.create_line(CoordA + (rozm / 1.5) * cos(Pi * (Omega / 180)), CoordZ + (rozm / 1.5) * sin(Pi * (Omega / 180)), CoordA - (rozm / 6) * cos(Pi * (Omega / 180)), CoordZ - (rozm / 6) * sin(Pi * (Omega / 180)), fill ="red")

#def fondhorloge(CoordA, CoordZ, rozm, can1):  #function drawing the backgroud of the clock
#    Pi = 3.141592
#    drawcircle(CoordA, CoordZ, rozm, "ivory3", can1)#backgroud
#    drawcircle(CoordA, CoordZ, rozm / 80, "black", can1)#central point/needle articulation
#    can1.create_line(CoordA + (rozm - (rozm / 15)), CoordZ, CoordA + (rozm - (rozm / 5)), CoordZ) #drawing the N/S/E/W decorativ hour position
#    can1.create_line(CoordA, CoordZ + (rozm - (rozm / 15)), CoordA, CoordZ + (rozm - (rozm / 5)))
#    can1.create_line(CoordA - (rozm - (rozm / 15)), CoordZ, CoordA - (rozm - (rozm / 5)), CoordZ)
#    can1.create_line(CoordA, CoordZ - (rozm - (rozm / 15)), CoordA, CoordZ - (rozm - (rozm / 5)))

#    #here, this 4*2 line defined the position of the 8 intermediate line between the N/S/E/W decorativ line.
#    can1.create_line(CoordA + (rozm / 1.05) * cos(Pi * (30 / 180)), CoordZ + (rozm / 1.05) * sin(Pi * (30 / 180)), CoordA + (rozm / 1.20) * cos(Pi * (30 / 180)), CoordZ + (rozm / 1.20) * sin(Pi * (30 / 180)))
#    can1.create_line(CoordA + (rozm / 1.05) * cos(Pi * (60 / 180)), CoordZ + (rozm / 1.05) * sin(Pi * (60 / 180)), CoordA + (rozm / 1.20) * cos(Pi * (60 / 180)), CoordZ + (rozm / 1.20) * sin(Pi * (60 / 180)))

#    can1.create_line(CoordA - (rozm / 1.05) * cos(Pi * (30 / 180)), CoordZ - (rozm / 1.05) * sin(Pi * (30 / 180)), CoordA - (rozm / 1.20) * cos(Pi * (30 / 180)), CoordZ - (rozm / 1.20) * sin(Pi * (30 / 180)))
#    can1.create_line(CoordA - (rozm / 1.05) * cos(Pi * (60 / 180)), CoordZ - (rozm / 1.05) * sin(Pi * (60 / 180)), CoordA - (rozm / 1.20) * cos(Pi * (60 / 180)), CoordZ - (rozm / 1.20) * sin(Pi * (60 / 180)))

#    can1.create_line(CoordA + (rozm / 1.05) * cos(Pi * (30 / 180)), CoordZ - (rozm / 1.05) * sin(Pi * (30 / 180)), CoordA + (rozm / 1.20) * cos(Pi * (30 / 180)), CoordZ - (rozm / 1.20) * sin(Pi * (30 / 180)))
#    can1.create_line(CoordA + (rozm / 1.05) * cos(Pi * (60 / 180)), CoordZ - (rozm / 1.05) * sin(Pi * (60 / 180)), CoordA + (rozm / 1.20) * cos(Pi * (60 / 180)), CoordZ - (rozm / 1.20) * sin(Pi * (60 / 180)))

#    can1.create_line(CoordA - (rozm / 1.05) * cos(Pi * (30 / 180)), CoordZ + (rozm / 1.05) * sin(Pi * (30 / 180)), CoordA - (rozm / 1.20) * cos(Pi * (30 / 180)), CoordZ + (rozm / 1.20) * sin(Pi * (30 / 180)))
#   can1.create_line(CoordA - (rozm / 1.05) * cos(Pi * (60 / 180)), CoordZ + (rozm / 1.05) * sin(Pi * (60 / 180)), CoordA - (rozm / 1.20) * cos(Pi * (60 / 180)), CoordZ + (rozm / 1.20) * sin(Pi * (60 / 180)))

#def HORLOGE1(Gamma, Pi, Epsylon):# draw a clock with the center position x/x = gamma/pi and the radius = epsylon

#    fondhorloge(Gamma, Pi, Epsylon, label3)
#    strzalki = localtime()
#    hrs = strzalki[3] + 2
#    min = strzalki[4]
#    sec = strzalki[5]

#    print(hrs, min, sec)
#    drawPetAig(Gamma, Pi, Epsylon, hrs, label3)
#    drawGrdAig(Gamma, Pi, Epsylon, min, label3)
#    drawSecAig(Gamma, Pi, Epsylon, sec, label3)
#    window.after(1000, lambda: HORLOGE1(250, 250, 200))

#zegar cyfrowy
def czas():
    display_time = time.strftime('%H:%M:%S %p')
    label2.config(text=display_time)
    label2.after(200 , czas)

activeStr = ''
stack = []

#proces liczenia
def calculate():
    global stack
    global label
    result = 0
    operand2 = Decimal(stack.pop())
    operation = stack.pop()
    operand1 = Decimal(stack.pop())

    if operation == '+':
        result = operand1 + operand2
    if operation == '-':
        result = operand1 - operand2
    if operation == '/':
        result = operand1 / operand2
    if operation == '*':
        result = operand1 * operand2
    label.configure(text=str(result))

#pobranie przyciskow
def click(text):
    global activeStr
    global stack
    if text == 'CE':
        stack.clear()
        activeStr = ''
        label.configure(text='0')
    #elif text == 'Styl zegarka':
    #    if styl == 0 :
    #        styl = 1
    #       label2 = Label(window, font=("arial", 50), fg="black")
    #       label2.grid(row=8, column=0, columnspan=4, sticky="nsew")
    #    else:
    #        styl = 0
    #        label2 = Label(window, font=("arial", 50), fg="black")
    #        label2.grid(row=7, column=0, columnspan=4, sticky="nsew")
    #        label3 = Canvas(window, bg="white", height=500, width=500)
    #        label3.grid(row=7, column=0, columnspan=4, sticky="nsew")

    elif '0' <= text <= '9':
        activeStr += text
        label.configure(text=activeStr)
    elif text == '.':
        if activeStr.find('.') == -1:
            activeStr += text
            label.configure(text=activeStr)
    else:
        if len(stack) >= 2:
            stack.append(label['text'])
            calculate()
            stack.clear()
            stack.append(label['text'])
            activeStr = ''
            if text != '=':
                stack.append(text)
        else:
            if text != '=':
                stack.append(label['text'])
                stack.append(text)
                activeStr = ''
                label.configure(text='0')


#okno liczenia
label = Label(window, text='0', width=55)
label.grid(row=0, column=0, columnspan=4, sticky="nsew")
label2 = Label(window, font=("arial",50),fg ="black")
label2.grid(row=7, column=0, columnspan=4, sticky="nsew")
#label3 = Canvas(window, bg="white", height=500, width=500)
#.grid(row=7, column=0, columnspan=4, sticky="nsew")

#HORLOGE1(250, 250, 200)

button = Button(window, text='CE', fg ='black', bg='white',
                command=lambda text='CE': click(text))
button.grid(row=1, column=3, sticky="nsew")

for row in range(4):
    for col in range(4):
        button = Button(window, text=buttons[row][col], fg ='black', bg='white',
                        command=lambda row=row, col=col: click(buttons[row][col]))
        button.grid(row=row + 2, column=col, sticky="nsew")

window.grid_rowconfigure(10, weight=20)
window.grid_columnconfigure(8, weight=20)

czas()
window.mainloop()