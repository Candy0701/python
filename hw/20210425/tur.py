import turtle
turtle.speed(0)
def tree_leaves(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color('blue')
    turtle.begin_fill()
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.end_fill()


def tree_trunk(x,y):
    turtle.penup()
    turtle.goto(x+8,y-25)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color('brown')
    turtle.begin_fill()
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.end_fill()



tree_leaves(0, 0)
tree_leaves(0, -20)
tree_leaves(0, -50)
tree_trunk(0,-50)
tree_leaves(0, 0)
tree_leaves(-50, -20)
tree_leaves(-50, -50)
tree_leaves(-50, -20)
tree_trunk(-50,-50)
