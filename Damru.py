from turtle import *
import random
#import pygame
#pygame.mixer.init()
#pygame.mixer.music.load("st.mp3")
#pygame.mixer.music.play()
w=Turtle()
s=Screen()
#shape("turtle")
l=[ "red","blue","orange","yellow","green"]
s.bgcolor("white")
w.color("black","#8B4513")
w.speed(-1)
#w.lt(45)
#def t(x):
#    w.rt(120)
#    w.fd(x)
#    w.rt(120)
#    w.fd(x)
#    w.rt(120)
#    w.fd(x)
#    
#w.begin_fill()
#for i in range(45):
#    w.rt(.94)
#    w.fd(4)
#w.rt(80)
#for i in range(45):
#    w.rt(.6)
#    w.fd(4)
#w.rt(80)
#for i in range(45):
#    w.rt(.94)
#    w.fd(4)
#    
#w.penup()
#w.setpos(0,-34)
#w.pendown()
#w.lt(90)
#for i in range(45):
#    w.rt(.94)
#    w.fd(4)
#w.rt(80)
#for i in range(45):
#    w.rt(.6)
#    w.fd(4)
#w.rt(80)
#for i in range(45):
#    w.rt(.94)
#    w.fd(4) 
#w.end_fill()

#w.penup()
#w.setpos(0,0)
#w.pendown()
#w.lt(140)
#w.pensize(6)

#for i in range(45):
#    w.lt(2.5)
#    w.fd(5)
#for i in range(35):
#    w.rt(2.5)
#    w.fd(5)
#w.color("#8B4513")
#w.rt(210)
#w.begin_fill()
#t(25)
#w.end_fill()

#w.penup()
#w.setpos(0,-34)
#w.pendown()
#w.lt(140)
#w.pensize(6)

#w.color("black")
#for i in range(45):
#    w.lt(2.5)
#    w.fd(5)
#for i in range(35):
#    w.rt(2.5)
#    w.fd(5)
#w.color("#8B4513")
#w.rt(210)
#w.begin_fill()
#t(25)
#w.end_fill()
def damru(s,posd,x):
    w.color("black","#8B4513")
    w.speed(-1)
    w.lt(45)
    def t(x):
        w.rt(120)
        w.fd(x)
        w.rt(120)
        w.fd(x)
        w.rt(120)
        w.fd(x)
        
    w.begin_fill()
    for i in range(45):
        w.rt(.94)
        w.fd(s)
    w.rt(80)
    for i in range(45):
        w.rt(.6)
        w.fd(s)
    w.rt(80)
    for i in range(45):
        w.rt(.94)
        w.fd(s)
        
    w.penup()
    w.setpos(x,posd)
    w.pendown()
    w.lt(90)
    for i in range(45):
        w.rt(.94)
        w.fd(s)
    w.rt(80)
    for i in range(45):
        w.rt(.6)
        w.fd(s)
    w.rt(80)
    for i in range(45):
        w.rt(.94)
        w.fd(s) 
    w.end_fill()

    w.penup()
    w.setpos(x,posd)
    w.pendown()
    w.lt(120)
    w.pensize(6)

    for i in range(45):
        w.lt(2.5)
        w.fd(s)
    for i in range(35):
        w.rt(2.5)
        w.fd(s)
    w.color("#8B4513")
    w.rt(210)
    w.begin_fill()
    t(25)
    w.end_fill()

    w.penup()
    w.setpos(x,posd)
    w.pendown()
    #w.lt(140)
    
    w.pensize(6)
    #dhage
    w.color("black")
    w.lt(20)
    for i in range(45):
        w.lt(2.5)
        w.fd(s)
    for i in range(35):
        w.rt(2.5)
        w.fd(s)
    w.color("#8B4513")
    w.rt(210)
    w.begin_fill()
    t(25)
    w.end_fill()

def trishul(x,y,posd):
    
    w.speed(0)
    w.color("black")
    w.setpos(x,y)
    w.pensize(15)
    w.fd(600)
    w.penup()
    w.setpos(x,y+600)
    w.pendown()
    w.lt(90)
    for i in range(45):
        w.lt(2)
        w.bk(5)
    w.bk(100)
    w.rt(60)
    w.fd(25)
    w.lt(150)
    w.fd(40)
    w.lt(150)
    w.fd(25)
    for i in range(5):
        w.lt(2)
        w.bk(5)
    w.penup()
    w.setpos(x,y+600)
    w.pendown()
    w.rt(160)
    for i in range(45):
        w.rt(2)
        w.bk(5)
    w.bk(100)
    w.rt(60)
    w.fd(25)
    w.lt(150)
    w.fd(40)
    w.lt(150)
    w.fd(25)
    w.penup()
    w.setpos(x,y+600)
    w.pendown()
    w.rt(60)
    w.color("black","#8B4513")
    w.fd(280)
    w.lt(135)
    for i in range(4):
        w.fd(25)
        w.lt(90)
  
    w.penup()
    w.setpos(x,y+440)
    w.pendown()
    w.rt(45)
    damru(3,posd,x)
#    w.begin_fill()
#    w.speed(2)
#    w.lt(45)
#    w.fd(75)
#    w.rt(135)
#    w.fd(150)
#    w.lt(135)
#    w.fd(200)
#    w.lt(135)
#    w.fd(300)
#    w.rt(135)
#    w.fd(200)
#    w.rt(130)
#    w.fd(150)
#    w.end_fill(
    w.penup()
    w.setpos(x,y)
    w.pendown()
    w.color("black","grey")
    w.begin_fill()
    w.speed(0)
    w.rt(37)
    w.fd(50)
    w.lt(135)
    w.fd(75)
    w.lt(135)
    w.fd(50)
    w.end_fill()
w.lt(90)
w.penup()
w.setpos(-300,20)
w.pendown()
w.speed(9)
trishul(-300,20,490)    
w.penup()
w.setpos(300,20)
w.pendown()
w.rt(45)
w.speed(7)
trishul(300,20,490)


trishul()
done()