import turtle

turtle.Screen().bgcolor("Purple")
board = turtle.Turtle()

# triangle
board.forward(100)

board.left(120)
board.forward(100)
board.left(120)
board.forward(100)
board.penup()
board.right(150)
board.forward(50)

# rectangle
board.forward(100)
board.right(90)
board.forward(50)
board.right(90)
board.forward(100)
board.right(90)
board.forward(50)

turtle.done()