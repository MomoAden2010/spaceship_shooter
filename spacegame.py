import random
import pgzrun

WIDTH = 700
HEIGHT = 650

spaceship = Actor("spaceship.png")
spaceship.pos = 100,350
bug = Actor("bug.png")

enemies = []

def draw():
    screen.clear()
    screen.fill((242, 150, 219))
    bug.draw()
    spaceship.draw()

def update():
    if keyboard.left:
        spaceship.x = spaceship.x-2
    if keyboard.right:
        spaceship.x = spaceship.x+2

#def create_bugs():
for i in range(8):
    for j in range(4):
        enemies.append(Actor("bug"))
        enemies[-1].x = 100 + 50*i
        enemies[-1].y = 80 + 50*j

#create_bugs()




pgzrun.go()