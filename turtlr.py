from turtle import *
import random
import pygame
pygame.mixer.init()
pygame.mixer.music.load("jsk.mp3")
pygame.mixer.music.play()
w=Turtle()
s=Screen()
#shape("turtle")
l=[ "red","blue","orange","yellow","green"]
s.bgcolor("yellow")
w.color("black")
w.speed(-1)
w.rt(40)

def t(x):
        w.rt(120)
        w.fd(x)
        w.rt(120)
        w.fd(x)
        w.rt(120)
        w.fd(x)

def bnsri(siz,x,y):
    w.penup()
    w.setpos(x,y)
    w.pendown()
    w.color("black")
    w.begin_fill()
    for i in range(2):
            for i in range(90):
                w.rt(1)
                w.fd(siz)
            w.rt(90)
    w.end_fill()
    w.lt(40)
    w.fd(20)
    w.rt(40)
    for i in range(90):
        w.rt(1)
        w.fd(siz)
    w.lt(40)
    w.rt(90)
    w.fd(20)
    w.rt(40)
    w.color("black","#8B4513")
    w.begin_fill()
    for i in range(90):
        w.rt(1)
        w.fd(siz)
    w.lt(40)
    w.rt(90)
    w.fd(400)
    w.rt(40)
    for i in range(3):
        for i in range(90):
            w.rt(1)
            w.fd(siz)
            
        w.rt(90)
        w.color("#8B4513")
    w.color("black","#8B4513")
    w.lt(40)
    w.fd(400)
    w.end_fill()

    #leaf
    w.penup()
    w.setpos(x,y)
    w.pendown()
    w.color("green")

    w.begin_fill()
    for i in range(2):
            for i in range(90):
                w.rt(1)
                w.fd(siz)
            w.rt(90)
    w.end_fill()

    #face_of_bansuri
    w.penup()
    w.setpos(x,y)
    w.pendown()
    w.color("black")
    w.lt(140)
    w.begin_fill()
    for i in range(2):
            for i in range(90):
                w.rt(1)
                w.fd(siz)
            w.rt(90)
    w.end_fill()
    w.rt(140)
    

    w.penup()
    w.setpos(x+160,y-20)
    w.pendown()
    for i in range(6):
        w.color("black")
        w.begin_fill()
        w.circle(siz+12)
        w.end_fill()
        x+=siz+40
        w.penup()
        w.setpos(x+160,y-24)
        w.pendown()
    x-=240

    #peacock_feather
    w.penup()
    w.setpos(x+300,y)
    w.pendown()
    w.rt(42)
    w.color("blue")
    w.begin_fill()
    for i in range(2):
            for i in range(90):
                w.rt(1)
                w.fd(siz+1)
            w.rt(90)
    w.end_fill()
    #inner_design
    w.penup()
    w.setpos(x+300,y+25)
    w.pendown()
    w.color("green")
    w.begin_fill()
    for i in range(2):
            for i in range(90):
                w.rt(1)
                w.fd(siz)
            w.rt(90)
    w.end_fill()        
    w.lt(42)
    
    #dhage
    w.penup()
    w.setpos(x+0,y)
    w.pendown()
    w.color("white")
    w.lt(40)
    for i in range(45):
        w.lt(2.5)
        w.fd(siz+2)
        w.color(random.choice(l))
        w.begin_fill()
        w.circle(2)
        w.end_fill()
        w.color("black")
    for i in range(35):
        w.rt(2.5)
        w.fd(siz)
        w.color(random.choice(l))
        w.begin_fill()
        w.circle(2)
        w.end_fill()
        w.color("black")
    w.color("green")
    w.rt(210)
    w.begin_fill()
    w.circle(7)
    w.end_fill()
    
    w.color("black")
    w.penup()
    w.setpos(x+0,y)
    w.pendown()
    w.rt(190)
    for i in range(45):
        w.lt(2.5)
        w.fd(siz+2)
        w.color(random.choice(l))
        w.begin_fill()
        w.circle(2)
        w.end_fill()
        w.color("black")
    for i in range(35):
        w.rt(2.5)
        w.fd(siz)
        w.color(random.choice(l))
        w.begin_fill()
        w.circle(2)
        w.end_fill()
        w.color("black")
    w.color("red")
    
    w.begin_fill()
    w.circle(7)
    w.end_fill()

    w.rt(90)
    w.penup()
    w.setpos(x+0,y)
    w.pendown()
   # w.rt(90)
    w.color("black")
    w.fd(81)
    w.bk(81)


    w.penup()
    w.setpos(x+20,y)
    w.pendown()
    w.rt(180)
    for i in range(90):
        w.rt(1)
        w.fd(siz)
        
    
bnsri(1,0,0)
done()
