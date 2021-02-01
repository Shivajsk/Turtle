from turtle import *
import random
import pygame
pygame.mixer.init()
pygame.mixer.music.load("st.mp3")
pygame.mixer.music.play()
w=Turtle()
s=Screen()
#shape("turtle")
w.speed(0)
s.bgcolor("yellow")

l=["red","green","blue","pink","orange"]

w.penup()
w.setpos(-100,320)
w.pendown()
r=1
angle=1
fd=1
for i in range(10):
   
    for i in range(10):
        w.lt(angle)
        w.fd(fd)
        
        w.color(random.choice(l))
        w.begin_fill()
        w.circle(r)
        w.end_fill()
        angle+=3
        fd+=3
        
            

done()