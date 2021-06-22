# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 16:05:15 2021

@author: hp 2
"""
import turtle

def carre():
    """
    fonction qui trace un carre de côté cote en démarrant par la position position
    """
    turtle.pensize(5)
    turtle.pencolor("black")
    turtle.up()
    
    turtle.down()

    for i in range(6):
        
        turtle.forward(200)  
        turtle.right(90) 
    for i in range(1):
         turtle.fd(120)
         turtle.right(90)
         turtle.fd(130)
         turtle.left(90)
         turtle.fd(50)
         turtle.left(90)
         turtle.fd(130)
         turtle.left(270)
         turtle.fd(30)
         turtle.right(90)
         turtle.fd(200)
         turtle.left(270)
   

def triangle():
    '''le triangle permet de dessiner la toiture de la maison'''
    turtle.pensize(5) 
    turtle.forward(250)
    turtle.left(120)
    turtle.forward(100)
    x=0
    while(x<4):
        turtle.fd(50)
        turtle.right(90)
        x=x+1
    for i in range(2):
        
        turtle.forward(200)
        turtle.left(120)
        turtle.forward(100)
    
    turtle.forward(95)
    turtle.right(90)
def polonter():
    '''tracer de la fenetre'''
    x=0
    while(x<3):
        turtle.fd(20)
        turtle.right(90)
        x=x+1

    turtle.fd(40)
    turtle.right(90)
    turtle.fd(40)
    turtle.right(90)
    turtle.fd(40)
    turtle.right(90)
    turtle.fd(20)
    turtle.right(90)
    turtle.fd(40)
    turtle.bk(20)
    turtle.right(90)
    turtle.fd(20)
         
         
def teup(x, y ):
    ''''se déplacer à un point sans tracer'''
    turtle.up()
    turtle.right(90)
    if (isinstance(x, tuple) or isinstance(x, list)) and len(x) ==2: 
        turtle.goto(x)
    else:
        turtle.goto(x, y)
        turtle.down()
    
       
            
    
    
    
carre()
triangle()
teup(170, y =-50)
polonter()

turtle.exitonclick()

