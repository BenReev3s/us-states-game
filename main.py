import turtle
from turtle import Turtle

import pandas
FONT = ("Arial", 8, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = pandas.read_csv("50_states.csv")

state_turtle = Turtle()
state_turtle.penup()
state_turtle.hideturtle()

game_is_on = True

states_guessed = []
list_of_states = states["state"].tolist()

while game_is_on:
    answer_state = screen.textinput(title= f"{len(states_guessed)}/{len(list_of_states)} States Correct", prompt="What's another states name").title()

    #creates a csv of states not guessed by the user
    if answer_state == "Exit":
        states_missed = list(filter(lambda  state: state not in states_guessed, list_of_states))
        data_frame = pandas.DataFrame(states_missed, columns=["States Missed"])
        data_frame.to_csv("missed-states")
        game_is_on = False

    #When the state is guessed correct, the name of the state is plotted on the map and user has to guess another
    elif answer_state in states["state"].values:
        states_guessed.append(answer_state)
        state_x = states.loc[states["state"] == answer_state, "x"].iloc[0]
        state_y = states.loc[states["state"] == answer_state, "y"].iloc[0]
        state_turtle.goto(state_x, state_y)
        state_turtle.write(answer_state, font=FONT)
        if len(states_guessed) == 50:
            game_is_on = False


screen.exitonclick()