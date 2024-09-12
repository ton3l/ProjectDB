import tkinter
from tkinter import ttk

root = ttk.Tk()
root.geometry("400x400")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Login").grid(column=0, row=0)
ttk.Entry(root).grid(column=0,row=1,pady=2.5,padx=2.5)
ttk.Entry(root).grid(column=0,row=2,pady=2.5,padx=2.5)
root.mainloop()
