# This file was created by Emilio Perez on 9/25/2023

'''
Goals - create images for paper and scissors
Write program so that user selects rock or paper or scissors when cliking on image...
have t

'''



'''
Goals - create images for paper and scissors
Write program so that user selects rock or paper or scissors when cliking on image...
have t

'''

# import package
import turtle
from turtle import *
# The os module allows us to access the current directory in order to access assets
import os
import winsound
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

from random import randint

# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')
sounds_folder = os.path.join(game_folder, 'sounds')

# Used this resource to include sound
# https://www.youtube.com/watch?v=w6g8PO-Pqp4
def play_rock():
    winsound.PlaySound(os.path.join(sounds_folder, 'rock.wav'), winsound.SND_ASYNC)
def play_paper():
    winsound.PlaySound(os.path.join(sounds_folder, 'paper.wav'), winsound.SND_ASYNC)
def play_scissors():
    winsound.PlaySound(os.path.join(sounds_folder, 'scissors.wav'), winsound.SND_ASYNC)
def play_win():
    winsound.PlaySound(os.path.join(sounds_folder, 'win.wav'), winsound.SND_ASYNC)
def play_lose():
    winsound.PlaySound(os.path.join(sounds_folder, 'lose.wav'), winsound.SND_ASYNC)
def play_tie():
    winsound.PlaySound(os.path.join(sounds_folder, 'tie.wav'), winsound.SND_ASYNC)
# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

rock_w, rock_h = 256, 280

paper_w, paper_h = 256, 204

scissors_w, scissors_h = 256, 170

player_choice = ""

cpu_choice = ""

# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="red")


# canvas object
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)

# setup images for player and for computer
rock_image = os.path.join(images_folder, 'rock.gif')
rock_instance = turtle.Turtle()
cpu_rock_image = os.path.join(images_folder, 'cpu_rock.gif')
cpu_rock_instance = turtle.Turtle()

paper_image = os.path.join(images_folder, 'paper.gif')
paper_instance = turtle.Turtle()
cpu_paper_image = os.path.join(images_folder, 'cpu_paper.gif')
cpu_paper_instance = turtle.Turtle()

scissors_image = os.path.join(images_folder, 'scissors.gif')
scissors_instance = turtle.Turtle()
cpu_scissors_image = os.path.join(images_folder, 'cpu_scissors.gif')
cpu_scissors_instance = turtle.Turtle()




def show_rock(x,y):
    # add the rock image as a shape
    screen.addshape(rock_image)
    # attach the rock_image to the rock_instance
    rock_instance.shape(rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    rock_instance.penup()
    # set the position of the rock_instance
    rock_instance.setpos(x,y)

def cpu_show_rock(x,y):
    screen.addshape(cpu_rock_image)
    cpu_rock_instance.shape(cpu_rock_image)
    cpu_rock_instance.penup()
    cpu_rock_instance.setpos(x,y)

def show_paper(x,y):
    screen.addshape(paper_image)
    paper_instance.shape(paper_image)
    paper_instance.penup()
    paper_instance.setpos(x,y)

def cpu_show_paper(x,y):
    screen.addshape(cpu_paper_image)
    cpu_paper_instance.shape(cpu_paper_image)
    cpu_paper_instance.penup()
    cpu_paper_instance.setpos(x,y)


def show_scissors(x,y):
    screen.addshape(scissors_image)
    scissors_instance.shape(scissors_image)
    scissors_instance.penup()
    scissors_instance.setpos(x,y)


def cpu_show_scissors(x,y):
    screen.addshape(cpu_scissors_image)
    cpu_scissors_instance.shape(scissors_image)
    cpu_scissors_instance.penup()
    cpu_scissors_instance.setpos(x,y)


# Makes text possible 
text = turtle.Turtle()
text.color('black')
text.hideturtle()

# Displayes "Its Rock paper..." 
text.penup()
text.setpos(0,150)
text.write("Its rock, paper, scissors time!", False, "left", ("Arial", 24, "normal"))
text.setpos(72,320)

#makes compter choose between rock paper or scisors
def cpu_select():
    choices = ["rock", "paper", "scissors"]
    return choices[randint(0,2)]

# this function uses and x y value, an obj
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] -  w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False

#shows options to select
show_rock(-300,0)
show_paper(0,0)
show_scissors(300,0)

# function that passes through wn onlick
def mouse_pos(x, y):
    print(cpu_select())
    cpu_picked = cpu_select()
    if collide(x,y,rock_instance,rock_w,rock_h):
        print("I collided with rock...")
        #plays rock sound effect
        play_rock() 
        #shows what cpu and player picked
        if cpu_picked == "rock":
            cpu_show_rock(300,0)
            show_rock(-300,0)
            #hides other options
            scissors_instance.hideturtle()
            paper_instance.hideturtle()
            #clears the text
            text.clear()
            #Writes the outcome of match
            text.penup()
            text.setpos(-100,150)
            text.write("Computer chose rock it is a tie...", False, "left", ("Arial", 24, "normal"))
            #plays sound effect
            play_tie()
        elif cpu_picked == "paper":
            cpu_show_paper(300, 0)
            show_rock(-300,0)
            scissors_instance.hideturtle()
            paper_instance.hideturtle()
            text.clear()
            text.penup()
            text.setpos(-100,150)
            text.write("You Lose...", False, "left", ("Arial", 24, "normal"))
            text.clear()
            text.write("Computer chose paper you lose...", False, "left", ("Arial", 24, "normal"))
            play_lose()
        elif cpu_picked == "scissors":
            cpu_show_scissors(300,0)
            show_rock(-300,0)
            paper_instance.hideturtle()
            text.clear()
            text.penup()
            text.setpos(-100,150)
            text.write("You Win!", False, "left", ("Arial", 24, "normal"))
            text.clear()
            text.write("Computer chose scissors You Win!", False, "left", ("Arial", 24, "normal"))
            play_win()
           

            
    elif collide(x,y,paper_instance,paper_w,paper_h):
        print("I collided with paper")
        play_paper()
        if cpu_picked == "paper":
            show_paper(300,0)
            cpu_show_paper(-300,0)
            scissors_instance.hideturtle()
            rock_instance.hideturtle()
            text.clear()
            text.penup()
            text.setpos(-100,150)
            text.write("Computer chose paper it is a tie...", False, "left", ("Arial", 24, "normal"))
            play_tie()

        elif cpu_picked == "rock":
            show_paper(-300,0)
            cpu_show_rock(300,0)
            scissors_instance.hideturtle()
            rock_instance.hideturtle()
            text.clear()
            text.penup()
            text.setpos(-100,150)
            text.write("Computer chose rock You Win!", False, "left", ("Arial", 24, "normal"))
            play_win()
    
        elif cpu_picked == "scissors":
            show_paper(-300,0)
            cpu_show_scissors(300,0)
            scissors_instance.hideturtle()
            rock_instance.hideturtle()
            text.clear()
            text.penup()
            text.setpos(-100,150)
            text.write("Computer chose scissors you lose...", False, "left", ("Arial", 24, "normal"))
            play_lose()

    elif collide(x,y,scissors_instance,scissors_w,scissors_h):
        print("I collided with scissors")
        play_scissors()
        if cpu_picked == "scissors":
            play_scissors()
            show_scissors(300,0)
            cpu_show_scissors(-300,0)
            paper_instance.hideturtle()
            rock_instance.hideturtle()
            text.clear()
            text.penup()
            text.setpos(-100,150)
            text.write("Computer chose scissors it is a tie...", False, "left", ("Arial", 24, "normal"))
            play_tie()

        elif cpu_picked == "rock":
            play_scissors()
            show_scissors(-300,0)
            cpu_show_rock(300,0)
            paper_instance.hideturtle()
            rock_instance.hideturtle()
            text.clear()
            text.penup()
            text.setpos(-100,150)
            text.write("Computer chose rock you lose...", False, "left", ("Arial", 24, "normal"))
            play_lose()
    
        elif cpu_picked == "paper":
            play_scissors()
            show_scissors(-300,0)
            cpu_show_paper(300,0)
            paper_instance.hideturtle()
            rock_instance.hideturtle()
            text.clear()
            text.penup()
            text.setpos(-100,150)
            text.write("Computer chose paper You Win!", False, "left", ("Arial", 24, "normal"))
            play_win()
       
       
            
      
    else:
        print("pick somethign fool...")

screen.onclick(mouse_pos)
# runs mainloop for Turtle - required to be last  


screen.mainloop()