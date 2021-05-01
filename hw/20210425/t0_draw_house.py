'''
請使用def畫出10個，不同顏色的屋頂，及位置的房子
顏色用list用代入
'''
import turtle

color_list=['green', 'blue', 'pink', 'white', 'gray', 'orange', 'yellow', 'snow', 'tan', 'red']

turtle.speed(0)
def house_roof(x,y, color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.end_fill()

def house_rectangle(x,y):
    turtle.penup()
    turtle.goto(x+10,y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color('green')
    turtle.begin_fill()
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.end_fill()
for i in range(10):
    house_roof(-300+i*40,0,color_list[i])
    house_rectangle(-300+i*40, 0)