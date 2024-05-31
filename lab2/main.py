from tkinter.ttk import Combobox

import numpy as NUM
import bezier as BZ
import skfuzzy as FZ
from tkinter import *

import matplotlib.pyplot as plt
from collections import deque
import random

def simulate():
    pass

def clean():
    pass


if __name__ == "__main__":
    window = Tk()
    window.title("Лабораторная #2")
    sw = 1600
    sh = 900
    window.geometry('%dx%d' % (sw - 300, sh - 300))

    btn = Button(window, text="Симмулировать!", command=simulate)
    btn.grid(column=1, row=0)

    btn = Button(window, text="Очистить полотно!", command=clean)
    btn.grid(column=2, row=0)

    combo = Combobox(window)
    combo['values'] = (1, 2, 3, 4, 5, "Текст")
    combo.current(1)  # установите вариант по умолчанию
    combo.grid(column=1, row=2)

    combo = Combobox(window)
    combo['values'] = (1, 2, 3, 4, 5, "Текст")
    combo.current(1)  # установите вариант по умолчанию
    combo.grid(column=2, row=2)

    lbl = Label(window, text="Fuzzy")
    lbl.grid(column=1, row=4)
    txt = Entry(window, width=10)
    txt.grid(column=2, row=4)

    lbl = Label(window, text="Defuzzy")
    lbl.grid(column=1, row=6)
    txt = Entry(window, width=10)
    txt.grid(column=2, row=6)

    window.mainloop()