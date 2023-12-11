# from turtle import Turtle, Screen



# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(300)
#
#
# print(timmy)
#
# my_screen = Screen()
#
# my_screen.exitonclick()


from prettytable import PrettyTable


table = PrettyTable()
table.header = True

table.add_column("Pokemo Name", ["Picachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Picachu", "Squirtle", "Charmander"])
table.add_column("Rating", ["Picachu", "Squirtle", "Charmander"])


print(table)
