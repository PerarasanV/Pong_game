import turtle
import pygame
import time



pygame.init()

def Gamestart_sound():
    pygame.mixer.music.load("game-start-6104.mp3")
    pygame.mixer.music.play()

def Ballhit_sound():
    pygame.mixer.music.load("mixkit-game-ball-tap-2073.wav")
    pygame.mixer.music.play()

def Wallhit_sound():
    pygame.mixer.music.load("mixkit-arcade-video-game-bonus-2044.wav")
    pygame.mixer.music.play()

def End_sound():
    pygame.mixer.music.load("game-start-6104.mp3")
    pygame.mixer.music.play()



#Display

display= turtle.Screen()
display.setup(600,600)
display.bgcolor("white")
display.title("Pong game")
display.tracer(0)
Gamestart_sound()
display.bgpic("pongbackground.png")

#Left_Bar
left_bar= turtle.Turtle()
left_bar.speed(0)
left_bar.shape("square")
left_bar.color("White")
left_bar.shapesize(stretch_len=1,stretch_wid=3)
left_bar.penup()
left_bar.goto(-280,0)


#Right_Bar
right_bar= turtle.Turtle()
right_bar.speed(0)
right_bar.shape("square")
right_bar.color("White")
right_bar.shapesize(stretch_len=1,stretch_wid=3)
right_bar.penup()
right_bar.goto(280,0)

#Ball

ball= turtle.Turtle()
ball.shape("circle")
# ball.shapesize(2)
ball.color("orange")
ball.penup()
ball.dy=0.3
ball.dx=0.3



#moving the bars

#functions for player keys

def left_bar_up():
    left_bar.sety(left_bar.ycor()+40)

def left_bar_down():
    left_bar.sety(left_bar.ycor()-40)

def right_bar_up():
    right_bar.sety(right_bar.ycor()+40)

def right_bar_down():
    right_bar.sety(right_bar.ycor()-40)

#score_board

score_board= turtle.Turtle()
score_board.speed(0)
score_board.color("white")
score_board.penup()
score_board.goto(0,240)
score_board.hideturtle()
score_board.write(" Player 1: 0, Player 2 : 0",align="center",font=("aerial",20,"normal"))



display.listen()

#for player 1
display.onkeypress(right_bar_up,"Up")
display.onkeypress(right_bar_down,"Down")
#for player 2
display.onkeypress(left_bar_up,"w")
display.onkeypress(left_bar_down,"s")

a_points=0
b_points=0





while True:


    display.update()


    # to move the ball
    ball.sety(ball.ycor()+ball.dy)
    ball.setx(ball.xcor()+ball.dx)

    #top wall
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *=-1

    #bottom wall
    if ball.ycor()<-284:
        ball.sety(-284)
        ball.dy *= -1

    #right wall
    if ball.xcor()>280:
        ball.setx(280)
        ball.dx *= -1
        a_points+=1
        score_board.clear()
        score_board.write("Player 1: {}, Player 2 : {}".format(a_points,b_points), align="center", font=("aerial", 20, "normal"))
        Wallhit_sound()

    #left wall
    if ball.xcor()<-290:
        ball.setx(-290)
        ball.dx*=-1
        b_points+=1
        score_board.clear()
        score_board.write("Player 1 : {}, Player 2 : {}".format(a_points,b_points), align="center", font=("aerial", 20, "normal"))
        Wallhit_sound()
    #To strike the right_bar

    if ball.xcor()>260 and ball.ycor()< right_bar.ycor()+30 and ball.ycor()>right_bar.ycor()-30:
        ball.setx(260)
        Ballhit_sound()
        ball.dx *= -1

    #To strike the left_bar
    if ball.xcor()<-260 and ball.ycor() <left_bar.ycor()+30 and ball.ycor()> left_bar.ycor()-30:
        ball.setx(-260)
        Ballhit_sound()
        ball.dx*= -1

    if a_points > 10:
        score_board.clear()
        score_board.write("Player 1 won", align="center", font=("aerial", 20, "normal"))
        End_sound()
        

        



    if b_points > 10:
        score_board.clear()
        score_board.write("Player 2  won", align="center", font=("aerial", 20, "normal"))
        End_sound()
        
        

