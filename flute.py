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
s.bgcolor("black")
w.color("white")
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
    for i in range(2):
            for i in range(90):
                w.rt(1)
                w.fd(siz)
            w.rt(90)
    w.lt(40)
    w.fd(10)
    w.rt(40)
    for i in range(90):
        w.rt(1)
        w.fd(siz)
    w.lt(40)
    w.rt(90)
    w.fd(10)
    w.rt(40)
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
    w.lt(40)
    w.fd(400)
    w.penup()
    w.setpos(x+200,y-20)
    w.pendown()
    for i in range(5):
        w.color("white")
       # w.begin_fill()
        w.circle(siz+12)
     #   w.end_fill()
        x+=siz+40
        w.penup()
        w.setpos(x+200,y-24)
        w.pendown()
    x-=200
    w.penup()
    w.setpos(x+300,y)
    w.pendown()
    w.rt(42)
    for i in range(2):
            for i in range(90):
                w.rt(1)
                w.fd(siz+1)
            w.rt(90)
    w.penup()
    w.setpos(x+300,y+25)
    w.pendown()

    for i in range(2):
            for i in range(90):
                w.rt(1)
                w.fd(siz)
            w.rt(90)
            
    w.lt(42)
    
    #dhage
    w.penup()
    w.setpos(x+0,y-78)
    w.pendown()
    w.color("white")
    w.lt(40)
    for i in range(45):
        w.lt(2.5)
        w.fd(siz+2)
    for i in range(35):
        w.rt(2.5)
        w.fd(siz+2)
    w.color("#8B4513")
    w.rt(210)
    w.begin_fill()
    w.circle(5)
    w.end_fill()
    
    w.color("white")
    w.penup()
    w.setpos(x+0,y-78)
    w.pendown()
    w.rt(170)
    for i in range(45):
        w.lt(2.5)
        w.fd(siz+2)
    for i in range(35):
        w.rt(2.5)
        w.fd(siz+2)
    w.color("#8B4513")
    w.rt(210)
    w.begin_fill()
    w.circle(5)
    w.end_fill()
        
    
bnsri(1,0,0)
done()