import turtle
t = turtle.Pen()
#设置海龟绘图速度
t.speed(0)
t.penup()
turtle.bgcolor('black')
sides = int(turtle.numinput('Number of sides',
                            'How many sides in your spiral of spirals? (2-6)', 4, 2, 6))
colors = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']

for m in range(100):
    t.forward(m * 4)
    position = t.position()
    heading = t.heading()
    print(position, heading)
    for n in range(int(m / 2)):
        t.pendown()
        t.pencolor(colors[n % sides])
        t.forward(2 * n)
        t.right(360 / sides - 2)
        t.penup()
    t.setx(position[0])
    t.sety(position[1])
    t.setheading(heading)
    t.left(360 / sides + 2)

turtle.done()