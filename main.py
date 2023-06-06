import random
from turtle import Turtle, Screen

colors = ["red", "green", "blue", "yellow", "pink", "orange"]
y_positions = [-120, -70, -20, 30, 80, 130]
all_turtle = []
is_game_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)


if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtle:
        if turtle.xcor() > 250:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 20)
        turtle.forward(random_distance)


screen.exitonclick()
