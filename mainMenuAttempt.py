import turtle

screen = turtle.Screen()
screen.setup(500, 400)

t = turtle.Turtle()

t.up()
t.goto(-50, 15)
t.down()
t.setheading(0)
t.fillcolor('lightblue')
t.begin_fill()
for _ in range(2):
    t.forward(100)
    t.left(90)
    t.forward(40)
    t.left(90)
t.end_fill()
t.up()
t.goto(0, 25)
t.write('Play',
        align='center',
        font=('Arial', 20, 'bold'))

t.up()
t.goto(-50, -15)
t.down()
t.setheading(0)
t.fillcolor('lightcoral')
t.begin_fill()
for _ in range(2):
    t.forward(100)
    t.right(90)
    t.forward(40)
    t.right(90)
t.end_fill()
t.up()
t.goto(0, -45)
t.write('Settings',
        align='center',
        font=('Arial', 20, 'bold'))

playButton = turtle.Turtle()
playButton.speed(1)
playButton.shape('square')
playButton.shapesize(stretch_wid=2, stretch_len=5)
playButton.penup()
playButton.goto(0, 35)

settingsButton = turtle.Turtle()
settingsButton.speed(1)
settingsButton.shape('square')
settingsButton.shapesize(stretch_wid=2, stretch_len=5)
settingsButton.penup()
settingsButton.goto(0, -35)

def playButtonClick(x, y):
    t.clear()
    t.goto(100, 0)
    t.write('what',
            align='center',
            font=('Arial', 20, 'bold'))

def settingsButtonClick(x, y):
    t.clear()
    t.goto(0, 0)
    t.write('settings',
            align='center',
            font=('Arial', 20, 'bold'))

playButton.onrelease(playButtonClick)
settingsButton.onrelease(settingsButtonClick)


screen.mainloop()