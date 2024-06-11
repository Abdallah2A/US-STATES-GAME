import turtle
import pandas

screen = turtle.Screen()

screen.title("US STATES GAME")
img = "data/blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

states = pandas.read_csv("data/50_states.csv")
str_states = states.state.to_list()

correct_states = []
states_to_learn = []

while len(correct_states) < 50:
    choice = screen.textinput(title=f"({len(correct_states)} / 50) US States", prompt="Name State of US States: ").title()
    
    if choice.lower() == "exit":
        for state in str_states:
            if state not in correct_states:
                states_to_learn.append(state)
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("data/states_to_learn.csv")
        break
    
    if choice in str_states and choice not in correct_states:
        correct_states.append(choice)
        xcor = int(states[states.state == choice].x)
        ycor = int(states[states.state == choice].y)
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        text.goto(xcor, ycor)
        text.write(choice)