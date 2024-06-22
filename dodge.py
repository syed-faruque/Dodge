import turtle
from random import randint
import time

# Setting up the turtle and the turtle screen
player = turtle.Turtle()
player.color("#00FF00")
player.pensize(2)
player.speed(0)
player.hideturtle()
player.penup()

writer = turtle.Turtle()
writer.hideturtle()
writer.pencolor("#00FF00")

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(700, 670)

end_zone = 250

# Variables for the game
amountspeed = 0
blockades = []
list_locs = []
list_of_list_locs = []
start = time.time()
end = time.time()
time_alive = 0

# Ask the user for input to start the game, 't' button starts the game
def start_up():
    writer.goto(0, 0)
    writer.clear()
    writer.pencolor("#00FF00")
    writer.write("Press the 't' button to start", font=("Arial", 30, "normal"), align="center")
    writer.penup()
    writer.setheading(90)
    writer.forward(200)
    writer.pencolor("#00FF00")
    writer.write("Dodge", font=("Monaco", 75, "normal"), align="center")
    del blockades[:]
    del list_locs[:]
    del list_of_list_locs[:]
    writer.pendown()

start_up()

# Game functions
# Opens up a menu to choose difficulty, 'e' for easy, 'm' for medium, 'h' for hard
def start_game():
    player.goto(0, 0)
    writer.clear()
    screen.bgcolor("black")
    player.showturtle()
    writer.penup()
    writer.setheading(-90)
    writer.forward(300)
    writer.color("#00FF00")
    writer.write("Please press 'e' for easy mode, 'm' for medium mode, 'h' for hard mode", font=("Arial", 14, "normal"), align="center")

# Adds random numbers to the list_locs, and uses list_locs to create coordinate locations in list_of_list_locs
def set_blockade_locs():
    global list_locs
    count = 0
    while count < 16:
        random_loc = randint(-(end_zone + 50), -20)
        list_locs.append(random_loc)
        count += 1
    count = 0
    while count < 16:
        random_loc = randint(20, end_zone + 50)
        list_locs.append(random_loc)
        count += 1
    count = 0
    while count < 16:
        random_loc = randint(-(end_zone + 50), -20)
        list_locs.append(random_loc)
        count += 1
    random_loc = randint(50, end_zone + 50)
    list_locs.append(random_loc)
    count = 0
    while count < 16:
        random_loc = randint(20, end_zone + 50)
        list_locs.append(random_loc)
        count += 1
    random_loc = randint(-(end_zone + 50), -20)
    list_locs.append(random_loc)
    count += 1
    count2 = 0
    while count2 < (len(list_locs)) - 1:
        list_of_list_locs.append((list_locs[count2], list_locs[count2 + 1]))
        count2 += 2

# Creates the obstacles in the locations
def create_blockades(blockade_length):
    set_blockade_locs()
    index = 0
    while index < len(list_of_list_locs):
        blockade = turtle.Turtle()
        blockade.hideturtle()
        blockade.shapesize(blockade_length)
        blockade.shape("square")
        blockade.color("#00FF00")
        blockade.penup()
        blockade.goto(list_of_list_locs[index])
        blockade.showturtle()
        blockades.append(blockade)
        index += 1

# Controls the arrow's motion, and stops the motion, ending the game as soon as the arrow leaves the boundary or collides with an obstacle. While moving, 'w' moves up, 'd' moves right, 's' moves down, and 'a' moves left
def movement(speed, collision):
    global start
    global end
    global time_alive
    writer.goto(0, 0)
    start = time.time()
    lose1 = "false"
    while lose1 != "true":
        player.forward(speed)
        if (player.xcor() > (end_zone + 95)) or (player.xcor() < -(end_zone + 105)) or (player.ycor() > (end_zone + 80)) or (player.ycor() < -(end_zone + 70)):
            lose1 = "true"
            end = time.time()
            time_alive = end - start
        for i in range(len(list_of_list_locs)):
            if abs(player.xcor() - list_of_list_locs[i][0]) < collision and abs(player.ycor() - list_of_list_locs[i][1]) < collision:
                lose1 = "true"
                end = time.time()
                time_alive = end - start
    new_screen(time_alive)

# Sets the speed according to the difficulty chosen
def easy():
    writer.clear()
    global amountspeed
    amountspeed = 3
    create_blockades(2)
    movement(amountspeed, 25)

def medium():
    writer.clear()
    global amountspeed
    amountspeed = 6
    create_blockades(2)
    movement(amountspeed, 25)

def hard():
    writer.clear()
    global amountspeed
    amountspeed = 7
    create_blockades(2)
    movement(amountspeed, 25)

# Adds a restart menu, in which it tells the user that clicking 'r' will restart the game
def new_screen(time_alive):
    writer.clear()
    player.hideturtle()
    count = 0
    while count < len(blockades):
        blockades[count].hideturtle()
        count += 1
    writer.penup()
    writer.goto(0, 100)
    writer.write("Game Over", font=("Arial", 75, "normal"), align="center")
    writer.goto(0, 0)
    writer.write("Press 'r' to restart", font=("Arial", 30, "normal"), align="center")
    writer.goto(0, -100)
    writer.write("You were alive for " + str(time_alive) + " seconds", font=("Arial", 20, "normal"), align="center")
    writer.goto(0, -300)
    if time_alive > 30:
        writer.color("pink")
        writer.write("Mastery", font=("Arial", 60, "normal"), align="center")
    elif time_alive > 15:
        writer.color("blue")
        writer.write("Good job", font=("Arial", 60, "normal"), align="center")
    else:
        writer.color("red")
        writer.write("Try harder", font=("Arial", 60, "normal"), align="center")

# Direction changes in the turtle
def move_right():
    player.setheading(0)

def move_up():
    player.setheading(90)

def move_left():
    player.setheading(180)

def move_down():
    player.setheading(270)

# Onkeypress event handlers
screen.onkey(start_game, "t")
screen.onkey(easy, "e")
screen.onkey(medium, "m")
screen.onkey(hard, "h")
screen.onkey(move_up, "w")
screen.onkey(move_right, "d")
screen.onkey(move_down, "s")
screen.onkey(move_left, "a")
screen.onkey(start_up, "r")

screen.listen()
turtle.mainloop()
