from turtle import *
import random
import pygame
pygame.mixer.init()
pygame.mixer.music.load("jsr.mp3")
pygame.mixer.music.play()
l=[ "red","blue","orange","green","white","pink"]
w=Turtle()
s=Screen()
s.bgcolor("yellow")
w.speed(0)

w.pensize(5)
w.penup()
w.setpos(-450,-950)
w.pendown()
#w.circle(400)
size=10
w.rt(225)
def border():
        w.fd(50)
        w.rt(90)
        w.fd(50)
        w.lt(90)
def borfunc(fl,sl):
    for i in range(2):
        for i in range(fl):
            border()
        w.rt(90)    
        for i in range(sl):
            border()
        w.rt(90)
w.color("red")
borfunc(28,13)    
w.penup()
w.setpos(-400,-900)
w.pendown()
w.color("green")
borfunc(26,11)
w.penup()
w.setpos(200,800)
w.pendown()
w.color("red")
w.pensize(10)
w.lt(225)
def swastik():
    w.bk(200)
    w.rt(90)
    w.fd(400)
    w.rt(90)
    w.fd(200)
    w.penup()
    w.setpos(-200,800)
    w.pendown()
    w.rt(270)
    w.fd(200)
    w.lt(90)
    w.fd(400)
    w.rt(90)
    w.fd(200)
swastik()
w.penup()
w.setpos(0,-200)
w.pendown()
w.lt(90)

def omkar():
    w.fd(100)
    w.bk(200)
    w.fd(100)
    #firstarc
    for i in range(90):
        w.rt(2)
        w.fd(5)
    w.rt(180)
    #2nd arc"
    for i in range(100):
        w.rt(2)
        w.fd(5)
    w.lt(20)
    w.penup()
    w.setpos(0,-489)
    w.pendown()
    w.rt(180)
    for i in range(40):
        w.rt(2)
        w.fd(5)
    for i in range(60):
        w.lt(2)
        w.fd(5)
    #chandrabindu
    w.penup()
    w.setpos(145,-52)
    w.pendown()
    w.rt(130)
    for i in range(90):
        w.rt(2)
        w.fd(5)
    w.penup()
    w.setpos(0,-110)
    w.pendown()
    w.color("red")
    w.begin_fill()
    w.circle(10)
    w.end_fill()

def siyaram():
    w.fd(420)
    w.bk(475)
    for i in range(100):
        w.rt(2)
        w.fd(3)
    w.rt(210)
    w.fd(180)
    w.penup()
    w.setpos(-50,300)
    w.pendown()
    w.rt(40)
    w.fd(300)
    w.penup()
    w.setpos(50,300)
    w.pendown()
    w.fd(300)
    w.rt(90)
    for i in range(90):
        w.rt(2)
        w.fd(1.2)
    w.fd(140)
    w.rt(90)
    w.fd(67)
    w.bk(300)
    

omkar()
w.penup()
w.setpos(-200,300)
w.pendown()
w.rt(90)
w.speed(9)
siyaram()
done()
	
