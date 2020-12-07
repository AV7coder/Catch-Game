import turtle # main module
import random # for random pos. of enemy
import time # for waiting of ball

# screen
wn = turtle.Screen()
wn.title("Catch It!")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)
# player setup
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("brown")
paddle_a.shapesize(stretch_wid=1, stretch_len=5)
paddle_a.penup()
paddle_a.goto(0,-270)
# opponents
c = random.randint(-380, 380)
cc = random.randint(-380, 380)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("circle")
paddle_b.color("red")
paddle_b.penup()
paddle_b.goto(c, 290)

paddle_c = turtle.Turtle()
paddle_c.speed(0)
paddle_c.shape("circle")
paddle_c.color("red")
paddle_c.penup()
paddle_c.goto(cc, 290)


# falling of opponent
def falling():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    y = paddle_c.ycor()
    y -= 20
    paddle_c.sety(y)

# arrow key mov. of player
def r():
    x = paddle_a.xcor()
    x += 20
    paddle_a.setx(x)

def l():
    x = paddle_a.xcor()
    x -= 20
    paddle_a.setx(x)

# score
score = 0 
pen = turtle.Turtle()
pen.color("yellow")
pen.penup()
pen.goto(0, 260)

while True:
    
    wn.update()
    # keyboard bindind
    wn.listen()
    wn.onkeypress(r, "Right")
    wn.onkeypress(l, "Left")
    # to check if the enemy is touching to player
    if paddle_b.distance(paddle_a) < 20:
        c = random.randint(-380, 380)
        paddle_b.goto(c, 290)
        score += 1
        
        pen.clear()
        pen.write("Score:{}".format(score), align= "center", font=("Courier", 24, "normal"))
    if paddle_c.distance(paddle_a) < 20:
        cc = random.randint(-380, 380)
        paddle_c.goto(c, 290)
        score += 1
        
        pen.clear()
        pen.write("Score:{}".format(score), align= "center", font=("Courier", 24, "normal"))     
    elif paddle_b.ycor() < -270:
        c = random.randint(-380, 380)
        paddle_b.goto(c, 290)
    elif paddle_c.ycor() < -270:
        cc = random.randint(-380, 380)
        paddle_c.goto(cc, 290)    
    
    # 0.1 second for enemy fall    
    time.sleep(0.1)
    falling()
