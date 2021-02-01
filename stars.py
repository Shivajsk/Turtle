from turtle import *
import random
import pygame
pygame.mixer.init()
pygame.mixer.music.load("mc.mp3")
pygame.mixer.music.play()
w=Turtle()
s=Screen()
shape("circle")
l=[ "red","blue","orange","yellow","white","green"]
s.bgcolor("black")
w.speed(0)
w.color("black")
def rangoli(x):
    for i in range(45):
        w.fd(x)
        w.bk(2*x)
        w.fd(x)
        w.lt(4)
    
def star(x):
    w.lt(70)
    w.fd(x)
    w.rt(150)
    w.fd(x)
    w.rt(148)
    w.fd(x)
    w.rt(132)
    w.fd(x)
    w.rt(141)
    w.fd(x+15)
    w.lt(141)
def pyramid(fd):
    for i in range(20):
        w.lt(200)
        w.fd(fd)
        fd+=2
        
def xmas():
    w.penup()
    w.setpos(0,900)
    w.pendown()
    w.pensize(6)
    w.color("black","green")
    w.begin_fill()
    w.rt(70)
    w.fd(958)
    w.lt(70)
    w.bk(655)
    w.lt(70)
    w.fd(958)
    w.end_fill()
    w.color("black")
    w.home()
    w.color("black","#8B4513")
    w.begin_fill()
    w.goto(-100,0)
    w.rt(90)
    w.fd(300)
    w.lt(90)
    w.fd(200)
    w.lt(90)
    w.fd(300)
    w.home()
    w.end_fill()
xmas()
w.rt(90)
w.color("green")
w.goto(0,920)
w.color("yellow")
fd1_=90
#headstar
for i in range(20):
        w.lt(200)
        w.fd(fd1_)
        fd1_+=2
w.color("black")

#snowman
w.lt(90)
w.penup()
w.setpos(50,-600)
w.pendown()
w.color("black","white")
w.begin_fill()
w.circle(100)
w.end_fill()
w.penup()
w.setpos(80,-890)
w.pendown()
w.color("black","white")
w.begin_fill()
w.circle(150)
w.end_fill()

#snowmaneyes
w.speed(0)
w.penup()
w.setpos(-60,-480)
w.pensize(4)
w.color("black","black")
w.begin_fill()
fd=2
for i in range(20):
        w.lt(200)
        w.fd(fd)
        fd+=2
w.end_fill()
w.penup()
w.setpos(40,-480)
w.pensize(4)
w.color("black","black")
w.begin_fill()
fd=2
for i in range(20):
        w.lt(200)
        w.fd(fd)
        fd+=2
w.end_fill()


#nose
w.color("black","orange")
w.rt(165)


w.penup()
w.setpos(-10,-520)
w.pendown()
w.begin_fill()
w.fd(40)
w.rt(135)
w.fd(58)
w.rt(135)
w.fd(40)
w.end_fill()

#mouth
w.penup()
w.setpos(-55,-570)
w.pendown()
w.begin_fill()
w.color("black","red")
w.rt(45)
w.fd(92)
w.rt(90)
for i in range(90):
    w.rt(2)
    w.fd(1.6)
w.end_fill()

#for i in range(1):
#    w.pensize(3)
#    w.penup()
#    w.setpos(random.randint(0,0),random.randint(0,900))
#    w.pendown()
#    w.color(random.choice(l))
#    pyramid(random.randint(10,100))
#w.lt(365)
#w.penup()
#w.setpos(-450,-970)
#w.pendown()
#def border():
#        w.fd(50)
#        w.rt(90)
#        w.fd(50)
#        w.lt(90)
#def borfunc(fl,sl):
#    for i in range(2):
#        for i in range(fl):
#            border()
#        w.rt(90)    
#        for i in range(sl):
#            border()
#        w.rt(90)

#w.pensize(5)
#w.color("red")
#w.speed(0)
#borfunc(28,13)    
#w.speed(8)
#for i in range(15):
#    w.pensize(3)
#    w.penup()
#    w.setpos(random.randint(0,10),random.randint(0,800))
#    w.pendown()
#    w.color(random.choice(l))
#    pyramid(random.randint(10,100))
w.color("white")
w.penup()
w.setpos(0,0)
w.pendown()
w.rt(90)
#w.home()
w.speed(0)
fd=50
w.penup()
w.setpos(0,900)
w.pendown()
w.rt(70)

for i in range(19):
    x=random.choice(l)
    w.color("black",x)
    w.begin_fill()
    w.fd(fd)
    
    w.circle(20)
    w.end_fill()
w.fd(8)
w.rt(110)
    
for i in range(13):
    x=random.choice(l)
    w.color("black",x)
    w.begin_fill()
    w.fd(fd)
    
    w.circle(20)
    w.end_fill()
    
w.rt(110)

    
for i in range(18):
    x=random.choice(l)
    w.color("black",x)
    w.begin_fill()
    w.fd(fd)
    
    w.circle(20)
    w.end_fill()
w.penup()
w.setpos(0,900)
w.pendown()
#w.rt(169)    

l=[ "red","blue","orange","yellow","white"]
w.lt(185)
for i in range(16):
    w.color("black",random.choice(l))
    w.begin_fill()
    for i in range(9):
        w.fd(45)
        w.lt(160)
    w.end_fill()
    
    w.fd(60)
w.penup()
w.setpos(-15,900)
w.pendown()
w.lt(34)


for i in range(17):
    w.color("black",random.choice(l))
    w.begin_fill()
    for i in range(9):
        w.fd(55)
        w.lt(160)
    w.end_fill()
    
    w.fd(50)
w.penup()   
w.setpos(-230,200)
w.pendown()
w.color(random.choice(l))
#pyramid(40)
#w.rt(45)
for i in range(1):
    w.color("black",random.choice(l))
    w.begin_fill()
    for i in range(9):
        w.fd(55)
        w.lt(160)
    w.end_fill()
    
    w.fd(50)
    
w.penup()   
w.setpos(-110,195)
w.pendown()
w.rt(45)
for i in range(1):
    w.color("black",random.choice(l))
    w.begin_fill()
    for i in range(9):
        w.fd(55)
        w.lt(160)
    w.end_fill()
    
    w.fd(50)
#pyramid(40)

w.penup()   
w.setpos(90,190)
w.pendown()
w.color(random.choice(l))
w.rt(45)
for i in range(1):
    w.color("black",random.choice(l))
    w.begin_fill()
    for i in range(9):
        w.fd(55)
        w.lt(160)
    w.end_fill()
    
    w.fd(50)
#pyramid(40)

w.penup()   
w.setpos(200,180)
w.pendown()
w.color(random.choice(l))
w.rt(45)
for i in range(1):
    w.color("black",random.choice(l))
    w.begin_fill()
    for i in range(9):
        w.fd(55)
        w.lt(160)
    w.end_fill()
    
    w.fd(50)
#pyramid(40)
w.speed(0)
#for i in range(5):
#    w.pensize(1)
#    w.penup()
#    w.setpos(random.randint(-500,-300),random.randint(-1000,1000))
#    w.pendown()
#    w.color(random.choice(l))
#    rangoli(random.randrange(50,150,25))

#for i in range(5):
#    w.pensize(1)
#    w.penup()
#    w.setpos(random.randint(300,500),random.randint(-1000,1000))
#    w.pendown()
#    w.color(random.choice(l))
#    rangoli(random.randrange(50,150,25))
def nptl(x):
    for i in range(30):
        w.fd(x)
        w.lt(190)

def zigzag(x):
    w.lt(100)
    w.fd(x)
    w.lt(90)
    w.fd(x)
    w.rt(90)
    w.fd(x)
    w.lt(90)
w.speed(-1)
for i in range(30):
    w.pensize(2)
    w.penup()
    w.setpos(random.randint(300,500),random.randint(-1000,1000))
    w.pendown()
    w.color(random.choice(l))
    y=random.randint(10,100)
#    for i in range(38):
   
    nptl(y)


for i in range(35):
    w.pensize(2)
    w.penup()
    w.setpos(random.randint(-500,-300),random.randint(-1000,1000))
    w.pendown()
    w.color(random.choice(l))
    y=random.randint(10,80)
#    for i in range(38):
   
    nptl(y)
w.pensize(5)
w.penup()
w.setpos(50,500)
w.pendown()
o=.5
k=5
for i in range(150):    
    w.color("white",random.choice(l))
#    w.begin_fill()
#    w.circle(o)
#    w.end_fill()
    w.lt(10)
    w.fd(k)
    
    
    k-=.04
done()
    