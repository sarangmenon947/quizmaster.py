import pgzrun

HEIGHT = 700
WIDTH = 900
TITLE = "Quiz Master By Sarang"

marquee = Rect(0,0,910,80)
questionbox = Rect(0,0,650,150)
timerbox = Rect(0,0,150,150)
skipbox = Rect(0,0,150,300)
option1 = Rect(0,0,300,150)
option2 = Rect(0,0,300,150)
option3 = Rect(0,0,300,200)
option4 = Rect(0,0,300,200)

questionfile = "Quiz Master\questions.txt"
marqueemessage = ""
optionboxes = [option1, option2, option3, option4]
questions = []
questioncount = 0
questionindex = 0

# Set Position For Boxes
marquee.move_ip(0,0)
questionbox.move_ip(20,100)
timerbox.move_ip(700,100)
option1.move_ip(20,270)
option2.move_ip(370,270)
option3.move_ip(20,350)
option4.move_ip(370,350)
skipbox.move_ip(700,270)

def draw():
    global marqueemessage
    screen.clear()
    screen.fill(color = "black")
    screen.draw.filled_rect(marquee, "black")
    screen.draw.filled_rect(questionbox, "blue")
    screen.draw.filled_rect(timerbox, "orange")
    screen.draw.filled_rect(skipbox, "green")
    for i in optionboxes:
        screen.draw.filled_rect(i, "yellow")
    marqueemessage = "Welcome To Quiz Master by Sarang...."
    marqueemessage += f"Q: {questionindex} of {questioncount}"
    screen.draw.textbox(marqueemessage, marquee, color = "pink")
    screen.draw.textbox("skip", skipbox, color = "red", angle = -90)

    if questions:
        screen.draw.textbox(questions[0][0].strip(), questionbox, color = "green")
        index = 1
        for j in optionboxes:
            screen.draw.textbox(questions[0][index].strip(), j, color = "brown")
            index = index + 1

def readquestionfile():
    global questioncount
    global questions
    q_file = open(questionfile, "r")
    for i in q_file:
        questions.append(i.strip().split(","))
        questioncount += 1
    q_file.close()

readquestionfile()
pgzrun.go()