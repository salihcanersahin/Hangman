from tkinter import *
import random
from PIL import Image, ImageTk
import requests
import io , os

root=Tk()

root.geometry("400x300")     
root.title("Hangman")

txt_url = "https://raw.githubusercontent.com/salihcanersahin/Hangman/main/countires.txt"
response_countries = requests.get(txt_url).text.split('\n')
countries = []
for line in response_countries:
    countries.append(line)

img_data = requests.get("https://raw.githubusercontent.com/salihcanersahin/Hangman/main/1.jpeg").content
root.one = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)).resize((100, 100), Image.ANTIALIAS))
  
limit = 1
random_county = random.choice(countries).lower()
print(random_county)
user_county = len(random_county)*"-"
userletters = []
def guess():     
    global user_county, limit, label_result
    userletter = user_guess.get().lower()
    if len(userletter) > 1 or userletter.isnumeric() == True or userletter.isalpha() == False:
        messagebox.showinfo(title="Warning", message="Do not enter more than one letter or number.")
    if userletter in random_county:
        index = 0
        for x in random_county:
            index+=1
            if x == userletter:
                user_county = user_county[:index-1] + userletter + user_county[index:]
                label_userguess["text"] = user_county
                user_guess.delete(0, END)
                if user_county == random_county:
                    label_result["text"] = "Congratulations"
                    label_result.place(x=120,y=230)
                    label_result["font"] = "Arial 16"
                    label_result["fg"] = "blue"
    else:
        user_guess.delete(0, END) 
        if len(userletter) <= 1:
            if userletter.isnumeric() == False:
                if userletter.isalpha() == True:   
                    if userletter not in userletters:
                        userletters.append(userletter)  
                        label_letters["text"] = userletters
                        limit = limit + 1                   
                        changeimage(limit)    


def changeimage(limit):
    img_url = "https://raw.githubusercontent.com/salihcanersahin/Hangman/main/" + str(limit) + ".jpeg"
    response = requests.get(img_url)
    img_data = response.content
    root.hangman = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)).resize((100, 100), Image.ANTIALIAS))
    label_picture["image"] = root.hangman
    if limit == 7:
        buton_send["state"] = "disabled"
        label_result["text"] = "Right answer is: " + random_county          
        label_result["fg"] = "red"
        label_result["font"] = "Arial 16"
        label_result.place(x=100,y=230)
        

label_title = Label()
label_title["text"] = "Countries in the world"
label_title.pack()

label_userguess = Label()
label_userguess["font"] = "Arial 28"
label_userguess["text"] = user_county
label_userguess["fg"] = "blue"
label_userguess["padx"] = 5
label_userguess.pack()

label_picture = Label()
label_picture["image"] = root.one
label_picture.pack()

user_guess = Entry()
user_guess["width"] = 12
user_guess ["font"] = "Arial 10"
user_guess.pack()

buton_send = Button(text = "send", font = "Arial 10", command = guess)
buton_send.place(x=150,y=200)  

def restart():
    global user_county,label_result, random_county,userletters,limit
    if label_result["text"] == "Congratulations" or label_result["text"].startswith("Right answer is:"):
        limit = 1
        random_county = random.choice(countries).lower()
        print(random_county)
        user_county = len(random_county)*"-"
        label_userguess["text"] = user_county
        label_result["text"] = " "
        label_letters["text"] = " "
        userletters = []
        user_guess.delete(0, END)
        buton_send["state"] = "active"
        label_picture["image"] = root.one

buton_restart = Button(text = "restart", font = "Arial 10", command = restart)
buton_restart.place(x=200,y=200)  

label_result = Label()
label_result.place(x=100,y=230)

label_letters = Label()
label_letters.place(x=180,y=260)

root.mainloop()

