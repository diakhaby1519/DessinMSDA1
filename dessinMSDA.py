import turtle
import math

def cercle( centre,rayon):

    #fonction qui trace un cercle de rayon rayon et de centre centre

    turtle.up()
    turtle.goto(centre)
    turtle.down()
    turtle.circle(rayon)
def demi_cercle(centre, rayon):
    """
    fonction qui trace un demi cercle de rayon rayon et de centre centre
    """
    turtle.pencolor("red")
    turtle.up()
    turtle.goto(centre)
    turtle.down()
    turtle.circle(rayon, 180)
def carre(position, cote):
    """
    fonction qui trace un carre de côté cote en démarrant par la position position
    """
    turtle.pencolor("green")
    turtle.up()
    turtle.goto(centre)
    turtle.down()
    for i in range(4):
        turtle.forward(cote)  # Côté
        turtle.left(90)
def triangle(position, cote):
    """
    fonction qui trace un triangle à partir de la position position
    """
    turtle.pencolor("red")
    turtle.up()
    turtle.goto(position)
    turtle.down()
    turtle.forward(cote)
    turtle.left(360/3)
    turtle.forward(cote)
    turtle.left(360/3)
    turtle.forward(cote)
def polygone(position, cote, nombre_cote):
    turtle.pencolor("blue")
    turtle.up()
    turtle.goto(position)
    turtle.down()
    for i in range(nombre_cote):
        turtle.forward(cote)
        turtle.left(360/nombre_cote)
def losange(position, cote, angle):
    turtle.pencolor("blue")
    turtle.up()
    turtle.goto(position)
    turtle.down()
    for i in range(4):
        if(i%2==0):
            turtle.right(angle)
            turtle.forward(cote)
        if(i%2==1):
            turtle.right(180-angle)
            turtle.forward(cote)
def trapeze(position, petite_base, grande_base,angle):
    turtle.pencolor("blue")
    turtle.up()
    turtle.goto(position)
    turtle.down()
    turtle.down()
    turtle.forward(grande_base)  # Côté
    turtle.left(50)
    turtle.forward(petite_base)
    turtle.left(90)
    turtle.forward(petite_base)
    turtle.right(90)
    turtle.left(90)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    centre = (15,20)
    position  = (200,200)
    cercle(centre, 100.5)
    carre(position,200)
    position = (0, -200)
    polygone(position, 100,9)
    position = (-50, -100)
    losange(position,150,120)
    position = (-300,50)
    triangle(position, 150)
    position = (-200, 10)
    trapeze(position,  60, 150,45)
    turtle.exitonclick()

