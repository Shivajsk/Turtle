from turtle import *
import random
#import pygame

#mp3_path = 'ddd.mp3''

#pygame.init()
#pygame.mixer.init()
#pygame.mixer.music.load(mp3_path)
#pygame.mixer.music.play()
l=[ "red","blue","orange","green","white","pink","yellow","orange", "maroon","violet","magenta", "purple", "navy", "skyblue", "cyan","turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "gray" ]
w=Turtle()
s=Screen()
s.bgcolor("black")
w.speed(-1)

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
    w.setpos(105,510)
    w.pendown()
    w.color("black")
    w.begin_fill()
    w.circle(13)
    w.end_fill()
  #  w.penup()
#    w.setpos(102,512)
#    w.pendown()
#    w.color("black")
#    w.begin_fill()
#    w.circle(5)
#    w.end_fill()
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
w.pensize(1)
w.color("black")
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
w.setpos(00,200)
w.pendown()
u=30
o=1

for i in range(160):
#    w.color(random.choice(l))
    w.speed(0)
    for i in range(1):
        w.fd(o)
       # w.lt(10)
    w.rt(3)
    w.color("white")
    w.fd(u)
    u-=5
    if u==-30:
        u=30
        w.lt(25)
    
    o+=.01
w.color("white")
w.penup()
w.setpos(150,500)
w.pendown()  
w.lt(80)
eye(1,150,500)
w.color("white")
w.penup()
w.setpos(250,400)
w.pendown() 
w.rt(110) 
w.fd(110)
w.rt(110)
w.fd(35)
done()