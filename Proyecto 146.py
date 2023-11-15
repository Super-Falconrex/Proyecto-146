# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 20:27:53 2023

@author: falconrex22
"""

from tkinter import*

root = Tk()
root.title("Código ASCII")
root.geometry("400x400")
root.configure(background = "red")

enter_word = Entry(root)
enter_word.place(relx= 0.5, rely= 0.3, anchor=CENTER)

label = Label(root, text="Código ascci", bg="cyan")

def ascciConveter():
    word = enter_word.get()
    
    for letter in word:
        label["text"] += letter + " " + str(ord(letter)) + " "
        
btn = Button(root, text="Muestra el código ascci", command= ascciConveter, bg="blue")
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
label.place(relx= 0.5, rely= 0.7, anchor=CENTER)

root.mainloop()