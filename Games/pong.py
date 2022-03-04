#####################################################################################################
#Python Pong game. Tutorial by TokyoEdtech(https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg)#
#####################################################################################################
import turtle

#Window
wn = turtle.Screen()
wn.title('CLASSIC PONG')
wn.bgcolor('black')
wn.setup(width=1000, height=750)
wn.tracer(0)

#Paddle A
a = turtle.Turtle()
a.speed(0)
a.shape('square')
a.shapesize(stretch_wid=5, stretch_len=1)
a.color('white')
a.penup()
a.goto(-450, 0)

#Paddle B
b = turtle.Turtle()
b.speed(0)
b.shape('square')
b.shapesize(stretch_wid=5, stretch_len=1)
b.color('white')
b.penup()
b.goto(450, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = -0.3

#Scoring
score_a = 0
score_b = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 330)
pen.write('Player A: 0  |   Player B: 0', align='center', font=('Courier', 18, 'bold'))

#Paddle Movements
def a_up():
    y = a.ycor()
    y+=20 #goes_up
    a.sety(y)

def a_down():
    y = a.ycor()
    y-=20 #goes_down
    a.sety(y)

def b_up():
    y = b.ycor()
    y+=20 #goes_up
    b.sety(y)

def b_down():
    y = b.ycor()
    y-=20 #goes_down
    b.sety(y)

#Keyboard Bindings
wn.listen() #listens keyboard inputs
wn.onkeypress(a_up, 'w') #when users hits 'w' call function a_up
wn.onkeypress(a_down, 's') #when users hits 's' call function a_down
wn.onkeypress(b_up, 'Up') #when users hits 'w' call function b_up
wn.onkeypress(b_down, 'Down') #when users hits 's' call function b_down

#Main Loop
while True:
    wn.update()

    #Ball Movements
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 350:
        ball.sety(350)
        ball.dy *= -1

    if ball.ycor() < -350:
        ball.sety(-350)
        ball.dy *= -1

    if ball.xcor() > 490:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write('Player A: {}   |   Player B: {}'.format(score_a, score_b), align='center', font=('Courier', 18, 'bold'))

    if ball.xcor() < -490:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('Player A: {}   |   Player B: {}'.format(score_a, score_b), align='center', font=('Courier', 18, 'bold'))


    #Bouncing
    if ball.xcor() >= 440 or ball.xcor() <= -440:
        if (ball.ycor() < a.ycor()+50 and ball.ycor() > a.ycor()-50) or (ball.ycor() < b.ycor()+50 and ball.ycor() > b.ycor()-50):
            ball.dx *= -1
