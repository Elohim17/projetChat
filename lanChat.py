# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 02:12:30 2023

@author: mysys
"""

from tkinter import *
#import leServeur2
#from clients2 import *

def create_fen():
    new_fen = Toplevel()
    new_fen.title('Chat en Local: Client')
    new_fen.geometry("500x50")
    
    #frame client
    frame = Frame(new_fen, bg="pink")
    frame.pack(side=BOTTOM)
    message = Label(frame, text="Ecrire le message:")
    message.pack(side=TOP)
    zSaisie = Entry(frame, 
                        font=("ink free", 20),
                        fg="black",
                        bg="khaki", 
                        width="25")
    zSaisie.pack(side=LEFT)

    envoyer = Button(frame, text='Envoyer',
                     activeforeground="black",
                     activebackground="blue")
    envoyer.pack(side=RIGHT)

    suprimer = Button(frame, text='Suprimer',
                      activeforeground="black",
                      activebackground="red")
    suprimer.pack(side=RIGHT)


fenetre = Tk()
fenetre.geometry('500x700')
fenetre.title('Chat en Local')

#fenetre.config()

label=Label(fenetre, text="Bienvenue dans le Chat !")
label.pack(side=TOP)

#frame serveur
frames = Frame(fenetre, bg="aqua", bd=8, relief=SUNKEN, width="500", height="500")
frames.pack(side=TOP)

clients = Button(fenetre, text="Commencer une discution", command=create_fen).pack()


fenetre.mainloop()