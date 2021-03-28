import turtle as t
t.color('blue')
t.shape('turtle')
t.penup()
for step in range(5,61,2):
    t.stamp()
    t.forward(step)
    t.right(25)
    print(step)