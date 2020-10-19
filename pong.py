import turtle

window = turtle.Screen()
window.title("Pong by @chairielazizi")
window.bgcolor("black")
window.setup(width =800,height =600)
window.tracer(0) #stop windows from updating
    
# Paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0) #speed of animation
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.penup() #to not draw line
paddle_A.goto(-350, 0)

# Paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0) #speed of animation
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.penup() #to not draw line
paddle_B.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) #speed of animation
ball.shape("square")
ball.color("white")
# ball.shapesize(stretch_wid=5, stretch_len=1)
ball.penup() #to not draw line
ball.goto(0, 0)

# functions
def paddle_A_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)
def paddle_A_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)

def paddle_B_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)
def paddle_B_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)

# Keyboard binding
window.listen()
window.onkeypress(paddle_A_up, "w")
window.onkeypress(paddle_A_down, "s")
window.onkeypress(paddle_B_up, "Up")
window.onkeypress(paddle_B_down, "Down")

# Main game loop
while True:
    window.update()