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


# Main game loop
while True:
    window.update()