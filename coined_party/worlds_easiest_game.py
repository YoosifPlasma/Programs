import turtle
import random
import time
from sys import exc_info

from Projects.coined_party.coined_party.coined_party import games_lounge

# Screen setup
screen = turtle.Screen()
screen.title("World's Easiest Game - Coined Party edition")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Player setup
player = turtle.Turtle()
player.shape('square')
player.color('red')
player.up()
player.goto(-250, -250)
playerSpeed = 20

# Goal setup
goal = turtle.Turtle()
goal.shape('square'),
goal.color('green')
goal.up()
goal.goto(250, 250)

# Enemy setup
enemyCount = 5
enemies = []

for _ in range(enemyCount):
    enemy = turtle.Turtle()
    enemy.shape('circle')
    enemy.color('blue')
    enemy.up()
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    enemy.goto(x, y)
    enemy.speed = random.choice([2, 3, 4])
    enemy.direction = random.choice(['up', 'down', 'left', 'right'])
    enemies.append(enemy)

# Player movement
def goUp():
    y = player.ycor() + playerSpeed
    if y <= 290:
        player.sety(y)

def goDown():
    y = player.ycor() - playerSpeed
    if y >= -290:
        player.sety(y)

def goLeft():
    x = player.xcor() - playerSpeed
    if x >= -290:
        player.setx(x)

def goRight():
    x = player.xcor() + playerSpeed
    if x <= 290:
        player.setx(x)

screen.listen()
screen.onkey(goUp, 'Up')
screen.onkey(goDown, 'Down')
screen.onkey(goLeft, 'Left')
screen.onkey(goRight, 'Right')

# Detecting collision
def isCollision(t1, t2):
    distance = t1.distance(t2)
    return distance < 20

# Main game loop
while True:
    screen.update()
    for enemy in enemies:
        if enemy.direction == "up":
            enemy.sety(enemy.ycor() + enemy.speed)
            if enemy.ycor() > 290:
                enemy.direction = "down"
        elif enemy.direction == "down":
            enemy.sety(enemy.ycor() - enemy.speed)
            if enemy.ycor() < -290:
                enemy.direction = "up"
        elif enemy.direction == "left":
            enemy.setx(enemy.xcor() - enemy.speed)
            if enemy.xcor() < -290:
                enemy.direction = "right"
        elif enemy.direction == "right":
            enemy.setx(enemy.xcor() + enemy.speed)
            if enemy.xcor() > 290:
                enemy.direction = "left"

        if isCollision(player, enemy):
            player.goto(-250, -250)
            print("Ouch. Try Again.")

    if isCollision(player, goal):
        print("You Win!")
        player.goto(-250, -250)
        time.sleep(1)

screen.mainloop()