import tkinter as tk

'''
border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

window = tk.Tk()

for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()

window.mainloop()

window = tk.Tk()

frame1 = tk.Frame(master=window,relief=tk.GROOVE, width=100, height=100, bg="red")
frame1.pack()

frame2 = tk.Frame(master=window,relief=tk.GROOVE, width=50, height=50, bg="yellow")
frame2.pack()

frame3 = tk.Frame(master=window,relief=tk.GROOVE, width=25, height=25, bg="blue")
frame3.pack()

window.mainloop()'''''''''

root = tk.Tk()

root.geometry("800x500")
title = root.title('My First GUI')

label1 = tk.Label(master=root, text='Hello World!', font=('Arial', '18'))
label1.pack(padx=10, pady=25)

textbox = tk.Text(master=root, height=3, font=('Arial', 14))
textbox.pack(padx=15,pady=10)
button_frame = tk.Frame(master=root)

button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

btn1 = tk.Button(button_frame, text="1", font=('Arial', 18))
btn1.grid(row=0, column=0,sticky=tk.W+tk.E)

btn2 = tk.Button(button_frame, text="2", font=('Arial', 18))
btn2.grid(row=0, column=1,sticky=tk.W+tk.E)


btn3 = tk.Button(button_frame, text="3", font=('Arial', 18))
btn3.grid(row=0, column=2,sticky=tk.W+tk.E)

button_frame.pack(fill='x')

# Optional
# btn=tk.Button(root,text='Click Me!', font=('Arial',18))
# btn.pack(padx=10,pady=10)
# my_entry=tk.Entry(root)
# my_entry.pack()


root.mainloop()
