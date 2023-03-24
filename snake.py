"""Snake, classic arcade game.
Arturo Ordoñez Jarillo
Danienl de la Peña Rosales 
"""

from random import randrange
from turtle import *

from freegames import square, vector
counter = vector(0, 0)
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def colorBody():
    color = randrange(1,6)
    if color == 1:
        colorString = 'black'
    elif color == 2:
        colorString = 'blue'
    elif color == 3:
        colorString = 'green'
    elif color == 4:
        colorString = 'violet'
    elif color == 5:
        colorString = 'brown'
    return colorString
colorB = colorBody()
colorF = colorBody()
while colorF == colorB:
    colorF = colorBody()

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    if counter.x % 15 == 0:
        
        if -200 < food.x < 190:
            food.x += randrange(-1, 2) * 10
        elif food.x == -200:
            food.x += 10
        elif food.x == 190:
            food.x -= 10

        
        if -200 < food.y < 190:
            food.y += randrange(-1, 2) * 10
        elif food.y == -200:
            food.y += 10
        elif food.y == 190:
            food.y -= 10
            
    for body in snake:
        square(body.x, body.y, 9, colorB)


    square(food.x, food.y, 9, colorF)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
