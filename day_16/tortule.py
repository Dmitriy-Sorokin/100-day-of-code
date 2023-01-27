# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
#
# my_screen = Screen()
#
# print(my_screen.canvwidth)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("City name", ["Adelaide", "Brisbane", "Darwin"])
table.add_column("Pokemon Name", ["Pika", "Sq", "Char"])
table.align = "l"
print(table)
