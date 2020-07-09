# Word Jumble


###########################  GUI Graphics ######################################################################


from tkinter import * 
import tkinter.messagebox as msg
import time
import random
##################################   SOUND PLAY  ##############################
from winsound import *

def play():
  PlaySound("sound1.wav",SND_ASYNC|SND_FILENAME|SND_LOOP)

def stop_play():
  PlaySound(None,SND_FILENAME)

###############################################################
with open('dict_word.txt') as word_file:
 valid_words =list(word_file.read().split('\n'))

with open('dict_meaning.txt') as meaning_file:
 valid_meaning =list(meaning_file.read().split('\n'))

diction = {}
y = 0
for i in valid_words:
  diction[i] = valid_meaning[y]
  y = y+1



def create_window(event):
    window = Toplevel(master)
    window.config(bg="black")
    window.title("Game Start...")
    canvas = Canvas(window, width=600, height=540)
    canvas.config(bg="black")
    canvas.pack()

    
    title = canvas.create_text(300, 20, anchor="n") 
    canvas.itemconfig(title, text="Lets Start The Game!!", width=780,font=("Times", 30,"italic"),fill="#FF4500")
    title1 = canvas.create_text(300, 80, anchor="n") 
    canvas.itemconfig(title1, text="[[[[[[[[[   Welcome to Word Jumble!   ]]]]]]]]]", width=780,font=("Times", 15,"italic"),fill="#FFFF00")
    title2 = canvas.create_text(300, 110, anchor="n") 
    canvas.itemconfig(title2, text="Unscramble the letters to make a word.", width=780,font=("Times", 15,"italic"),fill="#FFFF00")
    title3 = canvas.create_text(300, 130, anchor="n") 
    canvas.itemconfig(title3, text="Enter a 'guess' or type '?' and press submit for a hint", width=780,font=("Times",15,"italic"),fill="#FFFF00")
    title4 = canvas.create_text(300, 160, anchor="n") 
    canvas.itemconfig(title4, text=" For each Win,you get points and for wrong answer,points become 0", width=780,font=("Times", 15,"italic"),fill="#FFFF00")
    title5 = canvas.create_text(300, 190, anchor="n") 
    canvas.itemconfig(title5, text=" See if you can win ", width=780,font=("Times", 15,"italic"),fill="#FFFF00")

    

    def cool(event):
    
      def randchoise():
        word = random.choice(valid_words)
        global correct
        correct = word
        jumble =""
        while word:
          position = random.randrange(len(word))
          jumble += word[position]
          word = word[:position] + word[(position + 1):]
        return jumble

      
      take_rand = randchoise()

      # print( "     The jumble is:  ",randchoise())
      global lst
      lst = range(len(take_rand))
      hint_str = '_'*len(take_rand)

      word_button  = Button(window, text = take_rand , anchor = N)
      word_button.configure(width = 20, activebackground = "#EE82EE", relief = SUNKEN)
      word_button_window = canvas.create_window(230, 280, anchor=NW, window=word_button)


    def delete_arg(event):
      print("function is working")
      canvas.delete("wrong")
      canvas.delete("hint")
      canvas.delete("hint_window")
      canvas.delete("meaning_window")
      canvas.delete("win_score")
      take_guess.delete(0,END)



    start_button = canvas.create_text(290, 230, anchor="n") 
    canvas.itemconfig(start_button, text="**click me**", width=780,font=("Britannic Bold", 20),fill="#FF4500")
    canvas.tag_bind(start_button ,'<Button-1>',cool)


    jumble = canvas.create_text(160, 280, anchor="n")
    canvas.itemconfig(jumble, text=" The Jumble is : ", width=780,font=("Times", 15,"italic"),fill="#FFFF00")

    guess_text = canvas.create_text(160, 350, anchor="n")
    canvas.itemconfig(guess_text, text=" Your Guess : ", width=780,font=("Times", 15,"italic"),fill="#FFFF00")

    take_guess = Entry(canvas,width= 30,bd=5,justify='center')
    canvas.create_window(230, 350, anchor=NW, window=take_guess)

    score = 0
        
    def showme(event):
      
      guess_it = take_guess.get()
      guess = guess_it.lower()

      next_button = canvas.create_text(520, 480, anchor="e") 
      canvas.itemconfig(next_button, text=" Next ->>", width=780,font=("Britannic Bold", 15),fill="#FF4500")
      canvas.tag_bind(next_button ,'<Button-1>',delete_arg)
      canvas.tag_bind(next_button ,'<Button-1>',cool,add="+")
     

      text_score = canvas.create_text(310,380, anchor="n")
      wrong_score = canvas.create_text(310,380, anchor="n")

      if guess == correct:
        global score 
        score = score + 5
        text2 = "Correct Guess , Your Score is "+str(score)
        canvas.itemconfig(wrong_score, text= text2 , width=780,font=("Times",10,"italic"),fill="green",tag="win_score")
        
        for i in diction:
          if guess == i:
            canvas.delete("wrong")
            canvas.delete("hint")
            meaning_button  = Button(window, text = diction[i] , anchor = N)
            meaning_button.configure(width = 60, activebackground = "#EE82EE", relief = SUNKEN)
            meaning_button_window = canvas.create_window(300, 400, anchor=N, window=meaning_button,height=70,tags="meaning_window")
      

      else:
        score = 0
        
        text1 = "WRONG!!!"
        canvas.itemconfig(wrong_score, text= text1 , width=780,font=("Times",10,"italic"),fill="red",tag="wrong")


      if guess == '?':
        canvas.delete("wrong")
        global lst
        i = random.choice(lst)
        hint = canvas.create_text(15, 415, anchor="w")
        canvas.itemconfig(hint, text=" HINT : ", width=780,font=("Times", 15,"italic"),fill="#FFFF00",tag="hint")
        hint_button = Button(window, text = "Alphabet  "+correct[i]+"  is at "+str(i+1)+" postion in the word", anchor = N)
        hint_button.configure(width = 60, activebackground = "#EE82EE", relief = FLAT)
        hint_button_window = canvas.create_window(300, 400, anchor=N, window=hint_button,height=30,tags="hint_window")
        
        score = score+2

    submit = canvas.create_text(480, 350, anchor="n") 
    canvas.itemconfig(submit, text="SUBMIT", width=780,font=("Britannic Bold", 15),fill="#FF4500")
    canvas.tag_bind(submit,'<Button-1>',showme)
    
    



def show(event):
  print("Game starts....")
def quit(event):
    question = msg.askquestion("Are you sure!!","Do You Want To Quit ?")
    if question == 'yes':
        stop_play()
        master.quit()

def name(event):
    canvas_names = canvas.create_text(500, 445, anchor="n")
    canvas.itemconfig(canvas_names, text="All Rights Reserved @ Aamir", width=780,font=("Algerian", 30,"italic"),fill="#F0FFFF",activefill="#FFD700")

master = Tk()
master.title('WELCOME TO JUMBLE WORLD')
play()
#width, height = Image.open(image.png).size

canvas = Canvas(master, width=1000, height=509)
canvas.pack()
 
image = PhotoImage(file="full.png")
canvas.create_image(0, 0, image=image, anchor=NW)

canvas_play = canvas.create_text(20, 50, anchor="w")
canvas.itemconfig(canvas_play, text="PLAY GAME ", width=780,font=("Castellar", 30),fill="#FFFF00",activefill="red")
# print(canvas_play)
canvas.tag_bind(canvas_play,'<Button-1>',create_window)

canvas_quit = canvas.create_text(20, 100, anchor="w")
canvas.itemconfig(canvas_quit, text="QUIT", width=780,font=("Castellar", 30),fill="#FFFF00",activefill="red")
canvas.tag_bind(canvas_quit, '<Button-1>',quit)

canvas_name = canvas.create_text(20, 150, anchor="w")
canvas.itemconfig(canvas_name, text="CREATORS", width=780,font=("Castellar", 30),fill="#FFFF00",activefill="red")
canvas.tag_bind(canvas_name, '<Button-1>',name)

mainloop()


#####################################################################################################################









