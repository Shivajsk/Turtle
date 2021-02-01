from turtle import *
import random
import pygame
pygame.mixer.init()
pygame.mixer.music.load("md.mp3")
pygame.mixer.music.play()
w=Turtle()
s=Screen()
#shape("turtle")
l=[ "red","blue","orange","yellow","green"]
s.bgcolor("black")
w.color("white")
w.speed(-1)

def damru(s,posd,x):
    w.color("white","#8B4513")
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
    w.color("white")
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
    w.color("white")
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
    w.color("white","#8B4513")
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
    
    w.penup()
    w.setpos(x,y)
    w.pendown()
    w.color("white","grey")
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
w.color("white")
trishul(-300,20,490)    
w.penup()
w.setpos(300,20)
w.pendown()
w.rt(45)
w.speed(7)
w.color("white")
trishul(300,20,490)


def eye(siz,x,y):
    w.penup()
    w.setpos(x,y)
    w.pendown()
    w.color("white","grey")
    w.begin_fill()
    for i in range(2):
        for i in range(90):
            w.rt(1)
            w.fd(siz)
        w.rt(90)
    w.end_fill()
    w.penup()
    w.setpos(x-100,y-510)
    w.pendown()
    w.color("black","#3498db")
    w.begin_fill()
    w.circle(140)
    w.end_fill()
    w.penup()
    w.setpos(x-73,y-484)
    w.pendown()
    w.color("black")
    w.begin_fill()
    w.circle(105)
    w.end_fill()


def tika(x,y):
    #tika()
    w.color("white")
    
    for i in range(3):
        w.begin_fill()
        w.penup()
        w.setpos(x,y)
        w.pendown()
        w.fd(800)
        for i in range(90):
            w.rt(2)
            w.fd(1.5)
        w.fd(800)
        for i in range(90):
            w.rt(2)
            w.fd(1.5)
        y-=250
        w.end_fill()
        
        
#w.lt(45)
w.rt(135)
tika(-400,-100)        
    
w.rt(45)

w.color("white","grey")
w.begin_fill()
w.speed(-1)
eye(10,0,0)
w.end_fill()
#w.speed(-1)
#w.pensize(1)
#def t(x):
#    w.rt(60)
#    w.fd(x)
#    w.rt(120)
#    w.fd(x)
#    w.rt(120)
#    w.fd(x)
#    
#def sq(x):
#   
#    for i in range(2):
#        w.fd(x)
#        w.rt(90)
#        w.fd(x)
#        w.rt(90)
#        
#def rect(x,y):
#   
#    for i in range(2):
#        w.fd(x)
#        w.rt(90)
#        w.fd(y)
#        w.rt(90)
#o=.5
#k=10
#for i in range(0):    
#   # w.color(random.choice(l))
# #   w.begin_fill()
#    w.circle(o)
#    w.end_fill()
#    
#    w.lt(10)
#    #w.color("green")
#    t(k)
#  #  w.color(random.choice(l))
#    w.color("yellow")
#    t(k)
#    
#    k-=4
#    
#w.rt(250)
#w.color("brown")
#w.pensize(10)
#w.pensize(.1)
#w.color("yellow")
#w.fd(550)
#w.circle(10)
#done()

#for i in range(36):
#    w.color(random.choice(l))
#    w.circle(100)
#    w.lt(10)
#    w.fd(35)
#w.rt(90)
#w.fd(200)
#w.penup()
#w.setpos(00,00)
#w.pendown()
#u=1
#o=1
#z=10
#for i in range(1000):
#    c=random.choice(l)
#    w.color("black",c)
#    w.speed(0)
#    w.begin_fill()
#    #for i in range(9):
#        w.fd(o)
#        w.lt(160)
#    w.rt(20)
#    w.fd(u)
#    t(z)
#    z-=.02
#    u+=1
#    w.end_fill()
#    o+=.8
#def trishul(x,y):
#    
#    w.speed(0)
#    w.color("black")
#    w.setpos(x,y)
#    w.pensize(15)
#    w.fd(600)
#    w.penup()
#    w.setpos(x,y+600)
#    w.pendown()
#    w.lt(90)
#    for i in range(45):
#        w.lt(2)
#        w.bk(5)
#    w.bk(100)
#    w.rt(60)
#    w.fd(25)
#    w.lt(150)
#    w.fd(40)
#    w.lt(150)
#    w.fd(25)
#    for i in range(5):
#        w.lt(2)
#        w.bk(5)
#    w.penup()
#    w.setpos(x,y+600)
#    w.pendown()
#    w.rt(160)
#    for i in range(45):
#        w.rt(2)
#        w.bk(5)
#    w.bk(100)
#    w.rt(60)
#    w.fd(25)
#    w.lt(150)
#    w.fd(40)
#    w.lt(150)
#    w.fd(25)
#    w.penup()
#    w.setpos(x,y+600)
#    w.pendown()
#    w.rt(60)
#    w.color("black","#8B4513")
#    w.fd(280)
#    w.lt(135)
#    for i in range(4):
#        w.fd(25)
#        w.lt(90)
#    w.penup()
#    w.setpos(x,y+540)
#    w.pendown()
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
#    w.end_fill()
#    w.penup()
#    w.setpos(x,y)
#    w.pendown()
#    w.color("black","grey")
#    w.begin_fill()
#    w.speed(2)
#    w.lt(85)
#    w.fd(50)
#    w.lt(135)
#    w.fd(75)
#    w.lt(135)
#    w.fd(50)
#    w.end_fill()


#w.lt(40)    
#w.color("white")
#trishul(-450,100)
done()