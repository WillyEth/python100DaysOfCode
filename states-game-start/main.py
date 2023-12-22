import turtle
import pandas

screen = turtle.Screen()
screen.title("States Game")

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
guessed_states = []

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

while not len(guessed_states) >= 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="Enter State Name: ").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break;
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        state_data = data[data["state"] == answer_state]
        t.penup()
        # t.goto(int(state_data.x), int(state_data.y))
        # t.goto(int(state_data["x"]), int(state_data["y"]))
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        # t.write(state_data.state.item())
        t.write(answer_state)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()





screen.exitonclick()
