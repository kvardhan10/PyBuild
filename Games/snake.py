####################################################################################
# Video Ref: TokyoEdTech (https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg)#
####################################################################################

import turtle
import time
import random

wn = turtle.Screen()
wn.title('Snake-y')
wn.bgcolor('cyan')
wn.setup(width=600, height=600)
wn.tracer(0)

#Snake-head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('black')
head.penup()
head.goto(0,0)
head.direction='stop'

#Snake-food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('yellow')
food.penup()
food.goto(0,100)

segments = []

score = 0
high_score = 0

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Score: 0  High Score: 0', align='center', font=('courier', 24, 'bold'))

def move():
    if head.direction == 'up':
        head.sety(head.ycor() + 20)

    if head.direction == 'down':
        head.sety(head.ycor() - 20)

    if head.direction == 'left':
        head.setx(head.xcor() - 20)

    if head.direction == 'right':
        head.setx(head.xcor() + 20)

def go_up():
    if head.direction != 'down':
        head.direction = 'up'

def go_down():
    if head.direction != 'up':
        head.direction = 'down'

def go_left():
    if head.direction != 'right':
        head.direction = 'left'

def go_right():
    if head.direction != 'left':
        head.direction = 'right'

#Keyboard Bindings
wn.listen()
wn.onkeypress(go_up, 'w')
wn.onkeypress(go_down, 's')
wn.onkeypress(go_left, 'a')
wn.onkeypress(go_right, 'd')

while True:
    wn.update()

    #border collisions
    if head.xcor()>270 or head.xcor()<-280 or head.ycor()>280 or head.ycor()<-270:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'
        for seg in segments:
            seg.goto(10000, 10000)
        segments = []
        pen.clear()
        if score > high_score:
            high_score = score
            pen.write('Score: {}  High Score: {}'.format(0, high_score), align='center', font=('courier', 24, 'bold'))
        else:
            pen.write('Score: {}  High Score: {}'.format(0, high_score), align='center', font=('courier', 24, 'bold'))
        score = 0

    #for non border collisions, reverse x and y cor, so if it crosses top border, it appears from the bottom and no segments clearance

    if head.distance(food) < 20:
        #collided and move food
        food.goto(random.randint(-260, 260), random.randint(-260, 260))

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('grey')
        new_segment.penup()
        segments.append(new_segment)
        score += 10
        pen.clear()
        pen.write('Score: {}  High Score: {}'.format(score, high_score), align='center', font=('courier', 24, 'bold'))

    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    #body-collisions
    for seg in segments:
        if seg.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'
            for seg in segments:
                seg.goto(10000, 10000)
            segments = []
            pen.clear()
            if score > high_score:
                high_score = score
                pen.write('Score: {}  High Score: {}'.format(0, high_score), align='center', font=('courier', 24, 'bold'))
            else:
                pen.write('Score: {}  High Score: {}'.format(0, high_score), align='center', font=('courier', 24, 'bold'))
            score = 0

    time.sleep(0.1)

wn.mainloop()
