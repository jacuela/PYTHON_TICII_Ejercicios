

import turtle

miTortuga = turtle.Turtle()


while True:
    miTortuga.forward(200)
    miTortuga.left(170)
    print(miTortuga.pos())
    if abs(miTortuga.pos()) < 1:
        #print("fin")
        break