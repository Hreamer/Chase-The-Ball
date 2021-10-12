import turtle
import time


play=True

score1=0
score2=0

wn=turtle.Screen() #Get a reference to the windoq
wn.title("Chase the Ball 6900!") #Change the window name
wn.bgcolor("darkblue") #Change the color of the background
wn.setup(600,600) #Determine the window size

x=0
y=0

x_direction="right"
y_direction="up"

#--------------------------------------------------------------------
#Seting up the Turtles
t1=turtle.Turtle()#Player 1
t1.penup()
t1.speed(2)
t1.color("green")#changing the color
t1.shape("turtle")#changing the shape
t1.goto(0,-200)
t1.left(90)

t2=turtle.Turtle()#Player 2
t2.penup()
t2.speed(2)
t2.color("orange")
t2.shape("turtle")
t2.goto(0,200)
t2.right(90)

wiper=turtle.Turtle()
wiper.hideturtle()
wiper.penup()
wiper.fillcolor("darkblue")
wiper.pensize(2)
wiper.speed(0)
#wiper.goto(100,270) 
wiper.color("darkblue")



ball=turtle.Turtle()#The Ball
ball.speed(5)
ball.penup()
ball.right(45)
ball.color("yellow")
ball.shape("circle")

edge=turtle.Turtle()#Making the Edge of the gameboard
edge.hideturtle()
edge.speed(0)
edge.penup()
edge.pensize(4)
edge.goto(-265,-270)
edge.left(90)
edge.pencolor("white")
edge.pendown()
for i in range(4): #Top Left Corner is -265,250 Top corner is 255,250 Right Bottom is 255,-270  
    edge.forward(520)
    edge.right(90)

player1=turtle.Turtle()#Making the player's turtles
player1.hideturtle()
player1.speed(0)
player1.penup()
player1.goto(-255,260)
player1.pencolor("green")
player1.pendown()
player1.write("player 1: " + str(score1),font=("Arial",32,"normal"))

player2=turtle.Turtle()
player2.hideturtle()
player2.speed(0)
player2.penup()
player2.goto(90,260)
player2.pencolor("orange")
player2.pendown()
player2.write("player 2: " + str(score2),font=("Arial",32,"normal"))
#-------------------------------------------------------------------------
#Setting up the Key commands and Logic

def start():
    global x,y,x_direction,y_direction,score1,score2
    
    ballx=int(ball.xcor())
    bally=int(ball.ycor())
    
    ball_vx=4
    ball_vy=2
    
    while play==True:

        ball.goto(ballx,bally)

        if ballx>=250:
            ball_vx=-ball_vx

        elif ballx<=-260:
            ball_vx=-ball_vx

        if bally>=245:
            ball_vy=-ball_vy

        elif bally<=-265:
            ball_vy=-ball_vy
        
        ballx+=ball_vx
        bally+=ball_vy
        
        t1.forward(2)
        t2.forward(3)

        t1xcor=t1.xcor()
        t2xcor=t2.xcor()

        t1ycor=t1.ycor()
        t2ycor=t2.ycor()

        if ballx+10 >= t1xcor >= ballx-10 and bally+10 >= t1ycor >= bally-10:
            wiper.goto(-100,265)
            wiper.setheading(180)
            wiper.pendown()
                
            wiper.begin_fill()
            for i in range(2):
                wiper.forward(175)
                wiper.right(90)
                wiper.forward(35)
                wiper.right(90)
                
            wiper.end_fill()
            wiper.penup()
            score1+=1
            player1.write("player 1: " + str(score1),font=("Arial",32,"normal"))
            t1.goto(0,0)
            
                
        if ballx+10 >= t2xcor >= ballx-10 and bally+10 >= t2ycor >= bally-10:
            wiper.goto(100,260)
            wiper.setheading(0)
            wiper.pendown()
            
            wiper.begin_fill()
            for i in range(2):
                wiper.forward(175)
                wiper.left(90)
                wiper.forward(35)
                wiper.left(90)

            wiper.end_fill()
            wiper.penup()
            score2+=1
            player2.write("player 2: " + str(score2),font=("Arial",32,"normal"))
            t2.goto(0,0)
           
        if t1xcor+8 >= 252 >= t1xcor-8 or t1xcor+8 >= -257 >= t1xcor-8:
            wiper.goto(-100,260)
            wiper.setheading(180)
            wiper.pendown()
            
            wiper.begin_fill()
            for i in range(2):
                wiper.forward(175)
                wiper.right(90)
                wiper.forward(35)
                wiper.right(90)
                
            wiper.end_fill()
            wiper.penup()
            score1-=1
            player1.write("player 1: " + str(score1),font=("Arial",32,"normal"))
            t1.goto(0,0)

        if t2xcor+8 >= 252 >= t2xcor-8 or t2xcor+8 >= -257 > t2xcor-8:
            wiper.goto(100,260)
            wiper.setheading(0)
            wiper.pendown()
            
            wiper.begin_fill()
            for i in range(2):
                wiper.forward(175)
                wiper.left(90)
                wiper.forward(35)
                wiper.left(90)

            wiper.end_fill()
            wiper.penup()
            score2-=1
            player2.write("player 2: " + str(score2),font=("Arial",32,"normal"))
            t2.goto(0,0)

        if t1ycor+8 >= 247 >= t1ycor-8 or t1ycor+8 >= -262 >= t1ycor-8:
            wiper.goto(-100,260)
            wiper.setheading(180)
            wiper.pendown()
            
            wiper.begin_fill()
            for i in range(2):
                wiper.forward(175)
                wiper.right(90)
                wiper.forward(35)
                wiper.right(90)
                
            wiper.end_fill()
            wiper.penup()
            score1-=1
            player1.write("player 1: " + str(score1),font=("Arial",32,"normal"))
            t1.goto(0,0)

        if t2ycor+8 >= 247 >= t2ycor-8 or t2ycor+8 >= -262 >= t2ycor-8:
            wiper.goto(100,260)
            wiper.setheading(180)
            wiper.pendown()
            
            wiper.begin_fill()
            for i in range(2):
                wiper.forward(175)
                wiper.right(90)
                wiper.forward(35)
                wiper.right(90)
                
            wiper.end_fill()
            wiper.penup()
            score2-=1
            player2.write("player 2: " + str(score1),font=("Arial",32,"normal"))
            t2.goto(0,0)
            
            
            
                               
        
def t1w():
    t1.speed(5)
    t1.forward(10)

def t2forward():
    t2.speed(5)
    t2.forward(10)

def t1a():
    t1.speed(5)
    t1.left(25)

def t2left():
    t2.speed(5)
    t2.left(25)

def t1d():
    t1.speed(5)
    t1.right(25)

def t2right():
    t2.speed(5)
    t2.right(25)

#--------------------------------------------------------------------------
#Setting up the Keys and Stuff
wn.onkey(t1w, "w")

wn.onkey(t2forward, "Up")

wn.onkey(t1a, "a")

wn.onkey(t2left, "Left")

wn.onkey(t1d, "d")

wn.onkey(t2right, "Right")

wn.onkey(start, "s")
#--------------------------------------------------------------------------
#Making the hit detection



wn.listen()
wn.mainloop()
