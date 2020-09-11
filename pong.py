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
paddle_A.penup() #to not draw line
paddle_A.goto(-350, 0)

# Paddle B

# Ball

# Main game loop
while True:
    window.update()