from tkinter import *
from tkinter import messagebox
import time

def licz():
    x=0
    m = int(Entry.get(n1))  # minuty
    s = int(Entry.get(n2))
    t=m*60
    t+=s
    for x in range(t):
        time.sleep(1)
        x+=1
        print("Waiting")
    messagebox.showinfo("UWAGA", "JUZ CZAS")


root = Tk()
x= Entry(root)
Label(root, text="Ile minut:").grid(row=0, column=0)
Label(root, text="Ile sekund:").grid(row=1, column=0)
n1= Entry(root)
n1.grid(row=0, column=2)
n2= Entry(root)
n2.grid(row=1, column=2)
Button(root, text="Start", command=licz).grid(row=2, column=2)
check = StringVar()
root.mainloop()

