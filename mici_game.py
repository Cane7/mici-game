from math import *
from random import *
from tkinter import *

# GLOBALNE SPREMENLJIVKE

# canvas na katerega rišemo
canvas: Canvas

# velikost canvas-a
canvas_width = 600
canvas_height = 400

# identifikacijska številka objekta miši
miš: int

# identifikacijska številka objekta mici
mici: int

# obseg mici
r_mici = 50

# obseg miši
r_miš = 25

# točke igralca
točke = 0

# čas igre
game_time = 300


def poz_1(co1, co2, co3, co4):
    pozicija_1 = (co1, co2)
    pozicija_2 = (co3, co4)
    return pozicija_1, pozicija_2


def random_koords():
    random_x = randint(1, 5) * 100
    random_y = randint(1, 4) * 100

    canvas.coords(miš, random_x, random_y, random_x + 50, random_y + 50)


def beri_koords(id_štev: int):
    pos = canvas.coords(id_štev)
    x = (pos[0] + pos[2]) / 2
    y = (pos[1] + pos[3]) / 2
    return x, y


def razdalja(id1, id2):
    x1, y1 = beri_koords(id1)
    x2, y2 = beri_koords(id2)
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def premik_mici(event):
    premik_miš()
    if event.keysym == 'Left':
        canvas.move(mici, -10, 0)
    elif event.keysym == 'Right':
        canvas.move(mici, 10, 0)
    elif event.keysym == 'Up':
        canvas.move(mici, 0, -10)
    elif event.keysym == 'Down':
        canvas.move(mici, 0, 10)


def premik_miš():
    if razdalja(mici, miš) < (r_mici + r_miš):
        random_koords()
        global točke
        točke += 1


def odstevanje():
    global game_time
    print(f"Točke: {točke}")
    if 0 <= game_time:
        if točke >= 10:
            win()
    else:
        lose()

    game_time -= 1


def lose():
    canvas.create_text(300, 200, text='GAME OVER!', fill='red', font='helvecija')


def win():
    canvas.create_text(300, 200, text='YOU WIN!', fill='red', font='helvecija')


# ta funkcija se izvede vsakih 100 milisekund
def posodobitev():
    odstevanje()
    # ko mine 100 milisekund, se zopet pokliče funkcija `posodobitev`
    window.after(100, posodobitev)


if __name__ == '__main__':
    window = Tk()
    window.title('Mici game')

    canvas = Canvas(window, width=canvas_width, height=canvas_width, bg='white')
    canvas.bind_all('<Key>', premik_mici)
    canvas.pack()

    mici = canvas.create_oval(200, 200, 300, 300, fill='black')
    miš = canvas.create_oval(400, 200, 450, 250, fill='grey')

    # OSREDNJA ZANKA IGRE
    posodobitev()

    window.mainloop()
