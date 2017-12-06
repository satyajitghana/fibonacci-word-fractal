"""
Author : Satyajit Ghana
A fairly simple Fibonacci Word Fractal Generator, uses Python Turtle to plot the fractal.
"""
import sys
import turtle

sys.setrecursionlimit(100000000)

def fibonacci(first, second, n, i):
    if i < n :
        #print first
        return fibonacci(second, second+first, n, i+1)
    return first

def draw_fractal(word, step):
    for i, c in enumerate(word, 1):
        turtle.forward(step)
        if c == "0":
            if i % 2 == 0:
                turtle.left(90)
            else:
                turtle.right(90)

if __name__ == "__main__":
    N = input('Enter the number of recursion for the sequence > ')
    string = fibonacci('0','01',N, 0)
    #print string
    S = input('Enter the step size > ')
    #turtle.speed(0)
# change this to your screen resolution
    turtle.setup(width=1280, height=720)
    turtle.setheading(90)
    turtle.penup()
    turtle.left(90)
    turtle.forward(1280/2-10)
    turtle.right(90)
    turtle.backward(720/2-10)
    turtle.right(30)
    turtle.pendown()
    turtle.tracer(1000)
    draw_fractal(string, S)

    turtle.exitonclick()

