from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from tkinter import *

bot = ChatBot(
        'Norman',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///database.sqlite3'
    )

bot = ChatBot("AsianPaintsChatbot")
convo=[

   'I want to do color or interior design for my home?',
  'So tell me in which city do you live in?',
    'i live in ahmedabad',
    'I will tell you the address of the ahmedabad shop list . ',
    'Please tell me',
  'In ahmedabad the stores are located at Danilimda,GHatlodiya and in naroda',
   'What is your name ',
    'I Am Asian Pains Chatbot ,Created by Asia Paints',
    'In which city you live ?',
    'I Live in Ahmedabad',

]

trainer=ListTrainer(convo)
#train the bot
#trainer.train("chatterbot.corpus.english")


main=Tk()

main.geometry("500x650")

main.title("Asian Paints Chatbot")
img=PhotoImage(file="logo2.png")

photol=Label(main,image=img)
photol.pack(pady=5)

def ask_from_bot():
    query=textf.get()
    ans_from_bot=bot.get_response(query)
    msgs.insert(END,"You: "+query)
    msgs.insert(END,"Bot: "+str(ans_from_bot))
    textf.delete(0,END)
    msgs.yview(END)

frame=Frame(main)

sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20,yscrollcommand=sc.set)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()

#create text fild
textf=Entry(main,font=("Verdana",20))
textf.pack(fill=X,pady=10)

btn=Button(main,text="Ask from Bot",font=("Verdana",20),command=ask_from_bot)
btn.pack()

def enter_function(event):
    btn.invoke()

#going to bind windw with enter press
main.bind('<Return>',enter_function)
main.mainloop()