import tkinter as tk
import time


def update_time():
    current_time = time.strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, update_time)  


root = tk.Tk()
root.title("Digital Clock")


label = tk.Label(root, font=('Helvetica', 48,'bold'), bg="green", fg="black")
label.pack(anchor='center')

update_time()

root.mainloop()
