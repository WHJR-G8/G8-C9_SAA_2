import turtle
import random

list1=[]
for a in range(40, -1, -1):
    list1.append(a)
colors=["red","green","black","blue","yellow","grey","cyan","orange"]

def draw_arrows(l,c):
    for x in l:
        turtle.pencolor(random.choice(c))
        turtle.stamp()
        turtle.left(x)
        turtle.forward(40)
draw_arrows(list1,colors)
