import pyshorteners

from tkinter import *
#Creating the window
wn = Tk()
wn.title("URL_short")
wn.geometry('500x250')
wn.config(bg='darkgray')
def url_shortner():
 long_url = text.get()
 type_tiny = pyshorteners.Shortener()
 short_url = type_tiny.tinyurl.short(long_url)
 correctedText.set("The Shortened URL is: "+ short_url) #Showing the corrected word

text=StringVar(wn)
correctedText =StringVar(wn)

#The main label
Label(wn, text='URL_Shortner',bg='darkgray',
fg='black', font=('Times', 20,'bold')).place(x=100, y=10)

#Getting the input of word from the user
Label(wn, text='Enter long url:',bg='darkgray',font=('calibre',13,'normal'), anchor="e", justify=LEFT).place(x=20, y=70)

Entry(wn,textvariable=text, width=35,font=('calibre',13,'normal')).place(x=20,y=110)

#Label to show the correct word
opLabel = Label(wn, textvariable=correctedText, bg='gray',anchor="e",font=('calibre',13,'normal'), justify=LEFT).place(x=20, y=130)

#Button to do the spell check
Button(wn, text="ShortMe", bg='gray',font=('calibre', 13),
command=url_shortner).place(x=230, y=190)

#Runs the window till it is closed by the user
wn.mainloop()
#Function to check the spelling and show the corrected spelling
