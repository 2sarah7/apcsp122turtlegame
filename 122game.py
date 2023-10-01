# Sarah Hall 

# Import statements
import turtle as trtl
import random
import leaderboard as lb

# Screen setup
wn = trtl.Screen()
wn.bgcolor("salmon")

# Game Configuration/variables
leaderboard_file_name = "122leaderboard.txt"
player_name = input("Please enter your name: ")
shapeSizes = [1,1.5,2,2.5,3,3.5,4]
stampColors = ["white", "bisque", "powderblue", "lavender"]
turtleColor = "teal"
turtleSize = 2
turtleShape = "turtle"
score = 0 
fontSetUp = ("Georgia", 20, "normal")
timer = 10
counterInterval = 1000 #1000 is 1 second
timerUp = False

# Init drawing turtle
t = trtl.Turtle()
t.shape(turtleShape)
t.shapesize(turtleSize)
t.color(turtleColor)
t.up()

#Score writer
sw = trtl.Turtle()
sw.shapesize(0.1)
sw.up()
sw.goto(350, 300)

#Countdown timer
counter = trtl.Turtle()
counter.shapesize(0.1)
counter.up()
counter.goto(-350, 300)

# Game functions
def manage_leaderboard():

  global score
  global t

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, t, score)
  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, t, score)

def turtle_clicked(x,y):
    global timerUp
    t.shapesize(random.choice(shapeSizes))
    if timerUp == False:
        change_position()
        update_score()
    else:
        t.hideturtle()
    
def change_position():
    t.color(random.choice(stampColors))
    t.stamp()
    t.color(turtleColor)
    newX = random.randint(-400, 400)
    newY = random.randint(-300, 300)
    t.goto(newX,newY)
    
def update_score():
    global score
    sw.clear()
    score += 1
    sw.write(score, font=fontSetUp)
    
def countdown():
    global timer, timerUp
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=fontSetUp)
        timerUp = True
        manage_leaderboard()
    else: 
        counter.write("Timer: " + str(timer), font=fontSetUp)
        timer -= 1
        counter.getscreen().ontimer(countdown, counterInterval)

# Event listeners
t.onclick(turtle_clicked)

# Main loop
wn.ontimer(countdown, counterInterval)
wn.mainloop()


































