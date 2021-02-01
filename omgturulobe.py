from turtle import *
import random
#from playsound import playsound
#playsound('omg.mp3')
import pygame

for i in range(2):
    pygame.mixer.init()
    pygame.mixer.music.load("omg.mp3")
    pygame.mixer.music.play()
l=[ "red","blue","orange","green","white","pink"]
w=Turtle()
s=Screen()
s.bgcolor("yellow")
w.speed(-1)
w.pensize(2)
size=15
def circle(r):
     
     for i in range(size):
        r-=int(r/10)
        w.color("black",random.choice(l))
        w.begin_fill()
        w.circle(r)
        w.end_fill()
w.penup()
w.goto(-400,-700)
w.pendown()
circle(80)

w.penup()
w.goto(400,-700)
w.pendown()
circle(80)

w.penup()
w.goto(-400,700)
w.pendown()
circle(80)

w.penup()
w.goto(400,700)
w.pendown()
circle(80)

#O
w.penup()
w.setpos(-400,0)
w.pendown()
w.pensize(9)
w.circle(100)

#M
w.penup()
w.setpos(-150,0)
w.pendown()
w.rt(90)
w.bk(200)
w.lt(45)
w.fd(150)
w.lt(90)
w.fd(150)
w.rt(135)
w.fd(200)

#G
w.penup()
w.setpos(300,200)
w.pendown()
w.lt(90)
for i in range(135):
    w.left(2)
    w.bk(3)
w.lt(90)
w.bk(100)

#T
w.penup()
w.setpos(-400,-200)
w.pendown()
w.fd(150)
w.bk(75)
w.rt(90)
w.fd(150)

#U
w.penup()
w.goto(-220,-200)
w.pendown()
#w.rt(90)
w.fd(100)
for i in range(90):
    w.lt(2)
    w.fd(2)
w.fd(100)

#R
w.penup()
w.goto(-00,-200)
w.pendown()
w.rt(180)
w.fd(150)
w.bk(50)
w.lt(90)
for i in range(90):
    w.lt(2)
    w.fd(2)
w.lt(90)
w.fd(100)
w.lt(45)
w.fd(100)

#U   
w.penup()
w.setpos(130,-200)
w.pendown()
w.rt(45)
w.fd(100)
for i in range(90):
    w.lt(2)
    w.fd(2)
w.fd(100)

#heart
w.penup()
w.setpos(-50,-700)
w.pendown()
w.color("black","red")
w.begin_fill()
w.lt(45)
w.fd(200)
w.rt(45)
for i in range(90):
    w.rt(2)
    w.fd(2.43)
w.lt(180)
for i in range(90):
    w.rt(2)
    w.fd(2.43)
w.rt(45)
w.fd(200)
w.end_fill()

#emoji
w.penup()
w.setpos(-100,550)
w.pendown()
w.circle(150)
w.penup()
w.setpos(-70,480)
w.pendown()
w.color("black","red")
w.begin_fill()
w.lt(270)
w.fd(50)
w.rt(45)
for i in range(90):
    w.rt(2)
    w.fd(.686)
w.lt(180)
for i in range(90):
    w.rt(2)
    w.fd(.686)
w.rt(45)
w.fd(50)
w.end_fill()

#eyesofemoji
w.penup()
w.setpos(70,480)
w.pendown()
w.color("black","red")
w.begin_fill()
w.lt(270)
w.fd(50)
w.rt(45)
for i in range(90):
    w.rt(2)
    w.fd(.686)
w.lt(180)
for i in range(90):
    w.rt(2)
    w.fd(.686)
w.rt(45)
w.fd(50)
w.end_fill()

#mouthofemoji
w.penup()
w.setpos(-95,430)
w.pendown()
w.lt(135)
w.color("black","white")
w.begin_fill()
w.fd(215)
w.rt(90)
for i in range(45):
    w.rt(4)
    w.fd(7.5)
w.end_fill()
done()