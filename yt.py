import turtle

screen = turtle.Screen()
screen.title("YouTube Logo")

t = turtle.Turtle()
t.speed(10)

def draw_rounded_rectangle(width, height, radius):
    for _ in range(2):
        t.forward(width)
        t.circle(radius, 90)
        t.forward(height)
        t.circle(radius, 90)

t.penup()
t.goto(-120, -50)
t.pendown()
t.color("red")
t.begin_fill()
draw_rounded_rectangle(240, 100, 20)
t.end_fill()

t.penup()
t.goto(-30, -30)
t.pendown()
t.color("white")
t.begin_fill()
t.goto(50, 5)
t.goto(-30, 30)
t.goto(-30, -30)
t.end_fill()

t.hideturtle()

turtle.done()