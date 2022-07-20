from turtle import Turtle, done, begin_fill, end_fill, color
turtle = Turtle()
turtle.color('red', 'yellow')
turtle.begin_fill()
turtle.speed(10)
while True:
    turtle.forward(200)
    turtle.left(150)
    turtle.circle(30)
    if abs(turtle.pos()) < 1:
        break
turtle.end_fill()
done()