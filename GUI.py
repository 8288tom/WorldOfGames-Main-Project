import tkinter as tk
from time import sleep

import Live
from Live import print_games
from tkinter import messagebox

window = tk.Tk()
window.geometry("700x800")
frame1 = window.frame()
label1 = tk.Label(master=window, text=Live.welcome("Tom"))
label1.pack()

button1=tk.Button(master=window, text="game 1")
button1.pack()


window.mainloop()
