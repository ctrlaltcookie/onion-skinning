import pyautogui
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

window = tk.Tk()

# function for closing the window quickly and easily
def close_win(e):
   window.destroy(e)

window.bind("<Escape>", lambda e: close_win(e))
window.mainloop()