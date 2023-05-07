# Kaveh Sabouri

import customtkinter
from textblob import TextBlob

window = customtkinter.CTk()
window.geometry("500x500")
window.title("Spelling cheker")
window.configure(bg="#EDF6F9")
window.resizable(False,False)

def saving():
    enteryget = input1.get()
    correcting = TextBlob(enteryget)
    correcting2 = str(correcting.correct())
    print(correcting2) 

    label_show = customtkinter.CTkLabel(window,text="Correct text:",text_color="#006D77",text_font=("Lalezar",30))
    label_show.place(x=50,y=350)

    label_result = customtkinter.CTkLabel(window,text=correcting2,text_color="black",text_font=("",30))
    label_result.place(x=220,y=350)

# title of app
title_app = customtkinter.CTkLabel(window,text="Welcome to Spelling cheker app",text_color="#006D77",text_font=("Lalezar",30))
title_app.pack()

# inputs of app
input1 = customtkinter.CTkEntry(window,placeholder_text="Enter word",bg_color="#EDF6F9",width=220,height=35)
input1.place(x=50,y=220)

# Save and result button
save_button = customtkinter.CTkButton(window,text="Save",fg_color="#83C5BE",width=170,height=35,hover_color="#6C9D98",command=saving)
save_button.place(x=300,y=220)
window.mainloop()