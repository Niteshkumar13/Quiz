from tkinter import *
import pandas as pd
import pygame
import messagebox
import random
window = Tk()
# read the data from csv
x = pd.read_csv("ws.csv").to_dict(orient="records")
# create a canvas to set image
canvas1 = Canvas(height=600,width=800)
window.config(padx=10,pady=5,background="#a6fe92")
bg1 = PhotoImage(file="card_back.png")
# pygame.mixer.init() this method is used to initilize the music in bg
pygame.mixer.init()
pygame.mixer.music.load("D:\quiz\way.mp3")
pygame.mixer.music.play()
# canvas1.create_image(900,300,image=bg1)
fg1 = PhotoImage(file="card_back.png")
s = canvas1.create_image(405,300,image=fg1)
c = Label(text="Word",font=("arial",50),bg="#91c2af",fg="red")
c.place(x=100,y=200)
c = Label(text="Synonyms",font=("arial",50),bg="#91c2af",fg="red")
c.place(x=400,y=200)
title = canvas1.create_text(180,320,text="",font=("arial",30))
value = canvas1.create_text(550,320,text="",font=("arial",30))
cd = Label(text="max_score:70", font=("arial", 20), bg="#91c2af", fg="yellow")
cd.place(x=550, y=80)

canvas1.grid(row=1,column=4,columnspan=4)
canvas1.config(background="#a6fe92",highlightthickness=0)
canvas1.grid(row=0,column=0,columnspan=2)
i = 0
p = 0
t = ""
syno = ""
l_score = 0
def sp():
    cdd = Label(text=f"score:0{l_score}", font=("arial", 20), bg="#91c2af", fg="yellow")
    cdd.place(x=615, y=110)
sp()
blank_list = []
def random_title():
    i = 0
    global p
    global t
    global blank_list
    global syno
    global l_score

    while i < 1:

        if p < 70:

            i += 1
            t = random.choice(x)["Synonyms"]
            canvas1.itemconfig(value, text=t)
            word = x[p]["Words"]
            syno = x[p]["Synonyms"]

            blank_list.append(syno)

            canvas1.itemconfig(title, text=word)

            p +=1

start = Button()

def a1():
    # random_title()

    if syno == t:
        return 1
    else:
        return 0




right = PhotoImage(file="right.png")
wrong = PhotoImage(file="wrong.png")

q = 0
def wrong_c():
    global q
    global l_score
    random_title()
    # del blank_list[0]
    if a1() ==0:
        pass
        l_score +=1

    else:
        if q > 1:
            messagebox.showinfo("Fault somewhere",f"the right ans is {blank_list[0]}")
            del blank_list[:-1]

        else:
            q+=2






def right_c():
    global q
    global l_score
    random_title()
    if a1() == 1:
        pass
        l_score += 1
    else:
        if q > 1:
            messagebox.showinfo("Fault somewhere",f"the right ans is {blank_list[0]}")
            del blank_list[:-1]

        else:
            q+=2




button = Button(image=wrong,highlightthickness=0,command=wrong_c)
button.grid(row=1,column=0)
button1 = Button(image=right,highlightthickness=0,command=right_c)
button1.grid(row=1,column=1,pady=0)
window.mainloop()
