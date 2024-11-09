import pgzrun

HEIGHT = 700
WIDTH = 900
TITLE = "Quiz Master By Sarang"

# Define rectangles for UI elements
marquee = Rect(0, 0, 910, 80)
questionbox = Rect(0, 0, 650, 150)
timerbox = Rect(0, 0, 150, 150)
skipbox = Rect(0, 0, 150, 300)
option1 = Rect(0, 0, 300, 150)
option2 = Rect(0, 0, 300, 150)
option3 = Rect(0, 0, 300, 150)
option4 = Rect(0, 0, 300, 150)
score = 0
timeleft = 10
isgameover = False

questionfile = "Quiz Master/questions.txt"
marqueemessage = ""
optionboxes = [option1, option2, option3, option4]
questions = []
questioncount = 0
questionindex = -1 # Start at -1 so we can increment before accessing

# Set Position For Boxes
marquee.move_ip(0, 0)
questionbox.move_ip(20, 100)
timerbox.move_ip(700, 100)
option1.move_ip(20, 270)   
option2.move_ip(370, 270)   
option3.move_ip(20, 450)   
option4.move_ip(370, 450)   
skipbox.move_ip(700, 270)

def draw():
    global marqueemessage
    screen.clear()
    screen.fill(color="black")
    screen.draw.filled_rect(marquee, "black")
    screen.draw.filled_rect(questionbox, "blue")
    screen.draw.filled_rect(timerbox, "orange")
    screen.draw.filled_rect(skipbox, "green")
    for i in optionboxes:
        screen.draw.filled_rect(i, "yellow")
    
    marqueemessage = "Welcome To Quiz Master by Sarang...."
    marqueemessage += f"Q: {questionindex + 1} of {questioncount}" 
    screen.draw.textbox(marqueemessage, marquee, color="pink")
    screen.draw.textbox("skip", skipbox, color="red", angle=-90)

    if questions and questionindex >= 0: # Ensure there are questions and valid index
        screen.draw.textbox(questions[questionindex][0].strip(), questionbox, color="green") 
        for idx in range(4): # Loop through options safely
            if idx < len(optionboxes):
                screen.draw.textbox(questions[questionindex][idx + 1].strip(), optionboxes[idx], color="brown")

def movemarquee():
    marquee.x -= 2
    if marquee.right < 0:
        marquee.left = WIDTH

def update():
    movemarquee()

def readnextquestion():
    global questionindex
    questionindex += 1
    return questions.pop(0)

def on_mouse_down(pos):
    global questionindex
    if questionindex < len(questions): # Ensure we do not exceed the list length
        correct_answer_index = int(questions[questionindex][5]) # Get correct answer index
        
        for index in range(len(optionboxes)):
            if optionboxes[index].collidepoint(pos):
                if index + 1 == correct_answer_index: # Compare with correct answer index (adjusted for options)
                    correctanswer()
                else:
                    gameover()
        
        if skipbox.collidepoint(pos):
            skipquestion()

def correctanswer():Saragn
    global score
    score += 1
    if questionindex < questioncount - 1: # Check if there are more questions left
        readnextquestion()
        timeleft = 10 
    else:
        gameover()

def gameover():
    global timeleft, isgameover
    message = f"Game Over. You Got {score} Questions Correct." 
    question[:] = [message] + ["----"] + [5] 
    timeleft = 0 
    isgameover = True

def skipquestion():
    global timeleft
    if questionindex < questioncount - 1 and not isgameover:
        readnextquestion()
        timeleft = 10 
    else:
        gameover()

def update_time_left():
    global timeleft
    if timeleft > 0: 
        timeleft -= 1 
    else:
        gameover()

def readquestionfile():
    global questioncount
    with open(questionfile, "r") as q_file: 
        for i in q_file:
            questions.append(i.strip().split(",")) 
            questioncount += 1

readquestionfile()
if questions: # Ensure there are questions before reading the first one.
    readnextquestion()
clock.schedule_interval(update_time_left, 1)
pgzrun.go()
