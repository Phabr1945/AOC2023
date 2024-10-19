import turtle

my_turtle = turtle.Turtle()
my_turtle.color("green")

file = open("./day18.txt").read().strip()
array = []
for line in file:

turtle.exitonclick()