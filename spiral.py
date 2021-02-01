from turtle import *
import random
import pygame

w=Turtle()
s=Screen()
shape("circle")
l=[ "red","blue","orange","yellow","green"]
s.bgcolor("black")
w.speed(-1)
w.pensize(1)
def t(x):
    w.rt(60)
    w.fd(x)
    w.rt(120)
    w.fd(x)
    w.rt(120)
    w.fd(x)
    
def sq(x):
   
    for i in range(2):
        w.fd(x)
        w.rt(90)
        w.fd(x)
        w.rt(90)
        
def rect(x,y):
   
    for i in range(2):
        w.fd(x)
        w.rt(90)
        w.fd(y)
        w.rt(90)
o=.5
k=10
for i in range(0):    
   # w.color(random.choice(l))
 #   w.begin_fill()
#    w.circle(o)
#    w.end_fill()
    
    w.lt(10)
    #w.color("green")
    t(k)
  #  w.color(random.choice(l))
    w.color("yellow")
    t(k)
    
    k-=4
    
w.rt(250)
#w.color("brown")
#w.pensize(10)
w.pensize(.1)
w.color("yellow")
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
w.penup()
w.setpos(-400,0)
w.pendown()
while 1:
    w.color(random.choice(l))
    w.speed(0)
    for i in range(18):
        w.fd(100)
        w.lt(160)
    w.rt(10)
    w.fd(70)
 #   w.lt(10)
w.fd(200)
for i in range(60):
    w.color(random.choice(l))
    w.circle(30)
    w.lt(6)
w.fd(200)
for i in range(60):
    w.color(random.choice(l))
    w.circle(19)
    w.lt(6)
w.fd(200)
for i in range(60):
    w.color(random.choice(l))
    w.circle(10)
    w.lt(6)


def t(x):
    w.rt(60)
    w.fd(x)
    w.rt(120)
    w.fd(x)
    w.rt(120)
    w.fd(x)
#t(60)
done()