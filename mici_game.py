from random import *
from time import *
import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from math import *


window = Tk()
window.title('Mici game')

c = Canvas(window,  width=600, height=400, bg='white')
c.pack()

mici = c.create_oval(200, 200, 300, 300, fill='black')
miš = c.create_oval(400, 200, 450, 250, fill='grey')

def poz_1(co1, co2, co3, co4):
    pozicija_1 = (co1, co2)
    pozicija_2 = (co3, co4)
    return pozicija_1, pozicija_2

def poz_2(co1, co2, co3, co4):
    pozicija_1 = (co1, co2)
    pozicija_2 = (co3, co4)
    return pozicija_1, pozicija_2

def poz_3(co1, co2, co3, co4):
    pozicija_1 = (co1, co2)
    pozicija_2 = (co3, co4)
    return pozicija_1, pozicija_2

def poz_4(co1, co2, co3, co4):
    pozicija_1 = (co1, co2)
    pozicija_2 = (co3, co4)
    return pozicija_1, pozicija_2

def poz_5(co1, co2, co3, co4):
    pozicija_1 = (co1, co2)
    pozicija_2 = (co3, co4)
    return pozicija_1, pozicija_2

def poz_6(co1, co2, co3, co4):
    pozicija_1 = (co1, co2)
    pozicija_2 = (co3, co4)
    return pozicija_1, pozicija_2

def poz_7(co1, co2, co3, co4):
    pozicija_1 = (co1, co2)
    pozicija_2 = (co3, co4)
    return pozicija_1, pozicija_2

def random_koords():
    izbira = randint(1, 7)
    if izbira == 1:
        c.move(miš, poz_1())
    elif izbira == 2:
        c.move(miš, poz_2())
    elif izbira == 3:
        c.move(miš, poz_3())
    elif izbira == 4:
        c.move(miš, poz_4())
    elif izbira == 5:
        c.move(miš, poz_5())
    elif izbira == 6:
        c.move(miš, poz_6())
    elif izbira == 7:
        c.move(miš, poz_7())

r_mici = 50
r_miš = 25

def beri_koords(id_štev):
    pos = c.coords(id_štev)
    x = (pos[0] + pos[2])/2
    y = (pos[1] + pos[3])/2
    return x, y

def razdalja(id1, id2):
    x1, y1 = beri_koords(id1)
    x2, y2 = beri_koords(id2)
    return sqrt((x2-x1)**2 + (y2-y1)**2)

def premik_mici(event):
    if event.keysym == 'Left':
        c.move(mici, 0, -10)
    elif event.keysym == 'Right':
        c.move(mici, 0, 10)
    elif event.keysym == 'Up':
        c.move(mici, -10, 0)
    elif event.keysym == 'Down':
        c.move(mici, 10, 0)
c.bind_all('<Key>', premik_mici)

točke = 0

def premik_miš():
    if razdalja(mici, miš) < (r_mici + r_miš):
        random_koords()
        točke =+ 1

time = 30

def odstevanje(time):
    if time > 0 and time <= 30 and točke != 10:
        time =- 1
        sleep(1.00)

def konec():
    c.create_text(200, 150, 400, 200, text='GAME OVER!', fill='black', font='helvecija')

def win():
    c.create_text(200, 150, 400, 200, text='YOU WIN!', fill='black', font='helvecija')

#     OSREDNJA ZANKA IGRE

while time > 0 and točke != 10:
    premik_miš()
    odstevanje(time)
    window.after(100)

if time == 0 and točke != 10:
    konec()

if time > 0 and točke == 10:
    win()

window.mainloop()