import random
import tkinter as tk

#Creating Window Time
wd = tk.Tk()
wd.geometry("400x300")
wd.title(" Rock Paper Scissors Kleva ")

#Global Variables to keep track of Scores
U_SCORE = 0
COM_SCORE = 0
U_Choice = ""
Com_Choice = ""

# Convert Choice to number
def choice_to_num(choice):
    options = {'rock': 0, 'paper': 1, 'scissor': 2}
    return options[choice]

#Convert number to choice
def num_to_choice(num):
    options = {0 : 'rock', 1 : 'paper', 2 : 'scissor'}
    return options[num]

#Generate Random computer Choice
def com_choice():
    return random.choice(['rock', 'paper', 'scissor'])

# Function for determining who the winner is in that instant round of the game
def result(human_choice, com_choice):

    global U_SCORE
    global COM_SCORE
    user = choice_to_num(human_choice)
    com = choice_to_num(com_choice)

    if user == com:
        print("Tie")
    elif (user-com) % 3 == 1:
        print("You Win!!.")
        U_SCORE += 1
    else :
        print("You Lose **.")
        COM_SCORE += 1
    
    text_area = tk.Text(wd, height = 12, width = 20, bg = "#FFFF99")
    text_area.grid(column=0, row=4)
    ans = "Your Choice: {hc}\nComputer's Choice : {cc} \nYour Score : {us} \nComputer Score : {cs} ".format(hc = human_choice,cc = com_choice,us = U_SCORE,cs = COM_SCORE)

    text_area.insert(tk.END, ans)

def rock():
    global U_SCORE
    global COM_SCORE
    Com_Choice = com_choice()
    result("rock", Com_Choice)

def scissor():
    global U_SCORE
    global COM_SCORE
    Com_Choice = com_choice()
    result("scissor", Com_Choice)

def paper():
    global U_SCORE
    global COM_SCORE
    Com_Choice = com_choice()
    result("paper", Com_Choice)

# Let's Make the choice Buttons Brev
rockbutt = tk.Button(wd, text= "Rock", bg="skyblue", command=rock)
rockbutt.grid(column= 0, row =1)
paperbutt = tk.Button(wd, text="Paper" , bg = "pink", command = paper)
paperbutt.grid(column=0, row = 2)
scissorbutt = tk.Button(wd, text="Scissor", bg = "lightgreen", command= scissor)
scissorbutt.grid(column = 0, row= 3)

#Execute it all
wd.mainloop()

