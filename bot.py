from tkinter import *
from tkinter import ttk, messagebox, filedialog, simpledialog, scrolledtext
from plyer import notification

# speech transaltor
import speech_recognition as sr

import tkinter.font as tkFont

# speak out text
import pyttsx3, time, random

# get datetime
from datetime import datetime

import vlc, os, random, wikipedia, webbrowser

# starting to create window header
bot = Tk()
bot.title("Personal Assistant")
bot.resizable(False, False)
bot.iconbitmap("images/robot.ico")


# load bot pic
pic1 = PhotoImage(file='images/bot-pic.png')

# create data containers
mainF = Frame(bot, relief=SOLID, bd=1)
mainF.pack(fill=BOTH)

# left Container
leftF = Frame(mainF, bg="grey")
leftF.grid(row=0, column=0, sticky=N+S)

# ----------------left container code begins here---------------------------
botImage = Label(leftF, image=pic1, text="Hi, click me!", compound=TOP)
botImage.pack(pady=5, padx=5)
botImage.config(fg="white", bg="black", font=("tahoma",20, "bold"))


# right Container
rightF = Frame(mainF, bg="grey")
rightF.grid(row=0, column=1, sticky=N+S)

F1 = Frame(rightF, bg="grey")
F1.grid(sticky=W+E+S+N)

# ----------------right container code begins here-------------------------
ask1 = Label(F1, text="Tell Me About You", bg="black", fg="white", font=("tahoma",20, "bold"))
ask1.pack(pady=5, padx=5, fill=X)

name = ttk.Entry(F1, font=("tahoma",15, "bold"), justify=CENTER)
name.pack(pady=5, padx=5, fill=X)



# --------------------AI commands begin here-------------------

# start the speak functionality of the bot
engine = pyttsx3.init()
rate = engine.getProperty('rate')  #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate

volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)                        #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male


instance = vlc.Instance()
player = instance.media_player_new()


# speak out any text assigned
def speak(text):
	engine.say(text)
	engine.runAndWait()
	engine.stop()

# greeting list to append a greeting
greet = ['hey there', 'hello', 'hi', 'Hai', 'hey!', 'hey','how are you doing']
question = ['how are you', 'how are you doing']
responses = ['I am Okay', "I'm fine thank you",'I am cool, how are you?']
var1 = ['who made you', 'who created you','your creator','created you']
var2 = ['I was created by Barnabas Muzoora right in his computer.', 'I was created by Barnabas.', 'Some guy whom i never got to know.']
var3 = ['what time is it', 'what is the time', 'time']
var4 = ['who are you', 'what is you name']
cmd1 = ['open browser', 'open google']
cmd2 = ['play music', 'next song','next hit', 'play songs', 'play a song', 'open music player','music','song']
cmd3 = ['tell a joke','something funny', 'tell me a joke', 'say something funny', 'tell something funny']
jokes = ['Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all.', 'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.', 'Doctor said. Im sorry but you suffer from a terminal illness and have only 10 to live. Patient said. What do you mean, 10? 10 what? Months? Weeks?!"Doctor replied. Nine.']
cmd4 = ['open youtube', 'i want to watch a video']
cmd5 = ['tell me the weather', 'weather', 'what about the weather']
cmd6 = ['exit', 'close', 'goodbye', 'nothing']
cmd7 = ['what is your color', 'what is your colour', 'your color', 'your color?']
colrep = ['Right now its rainbow', 'Right now its transparent', 'Right now its non chromatic']
cmd8 = ['what is you favourite colour', 'what is your favourite color']
cmd9 = ['thank you']
cmd10 = ['lock my computer', 'lock screen','shut down','hibernate','sleep']

repfr9 = ['youre welcome', 'glad i could help you']

cmd11 = ['open students portal','BSU portal','open bsu portal','open portal','bsu students portal','students portal','student portal','bsu portal','portal']

cmd12 = ['bsu website', 'BSU website','open BSU website','open bsu website']

cmd13 = ('Faith in Jesus Christ as Lord and Saviour. Pursuit of Knowledge and Ingenuity. Academic Independence and Excellence. Compassion. Relentless Service to Society. Moral Integrity. Accountability. Transparency.')

cmd14 = ['BSU core values', 'core values for BSU','do you know BSU core values']

cmdVid = ['video','play video','i want to watch','movie','play a video']

cmdbsu = ['about BSU', 'what do you know about BSU', 'search about BSU','BSU','bsu','about bsu']


# a function to greet a user according to the time
def greeting(*args):
	now = datetime.now()
	currenttime = now.strftime("%H")
	if(currenttime<str(12)):
		greeting = "Hi there, good morning."
	elif(currenttime>=str(12) and currenttime<=str(15)):
		greeting = "Hi there, good afternoon."
	else:
		greeting = "Hi there, good evening."	
	

	try:
		if "true" in greet:
			pass
		else:
			speak(greeting)
			name.focus()
			speak("Please enter your name in the field and place enter on your keyboard.")
			greet.append("true")
	except Exception as e:
		print(e)

	
		
# get current user information
# --------------------/user audio to speech ends here-----------------

users = []
mic = PhotoImage(file='images/mic.png')
def getname(*args):
	F1.grid_remove()
	user = name.get()
	users.append(user)
	botImage.config(text="Hi, "+users[0])
	Label(rightF, text="Click Mic To Speak!", bg="black", fg="white", font=("tahoma",20, "bold")).grid(row=1, column=0, sticky=W+E, pady=5, padx=5)
	
	# add button to start speaking

	btC = Label(rightF, image=mic, bg="gray", cursor="hand2")
	btC.grid(row=2, column=0)
	btC.bind("<1>",get_audio)	




name.bind("<Return>", getname)

botImage.bind("<Enter>", greeting) 


# -----------------get speech from user-----------------
state = Text(rightF, width=50, wrap=WORD, relief=SOLID, height=10,  bg="grey", fg="black", font=("arial",10, "bold"))
state.grid(row=3, sticky=W+E, pady=5, padx=5)

bF = Frame(rightF, bg="grey")
bF.grid(row=4)

pauseB = Button(bF, bg='skyblue', text="Pause", relief=GROOVE, cursor='hand2', font=('arial',12,'bold'))
nextB = Button(bF, bg='skyblue', text="Next", relief=GROOVE, cursor='hand2', font=('arial',12,'bold'))
prevB = Button(bF, bg='skyblue', text="Prev", relief=GROOVE, cursor='hand2', font=('arial',12,'bold'))



def pauseM():
	state.delete('1.0',END)
	state.insert('1.0',"Music Paused")
	player.pause()

pa = ttk.Button(rightF, text="Pause Music", command=pauseM)

def nextV():
	mfiles = os.listdir("video")
	start_s = mfiles[0]

	curent_s = state.get('1.0','end-1c')

	if curent_s in mfiles:

		next_s = mfiles.index(curent_s)+1

		if next_s>=len(mfiles):
			playing_s = mfiles[0]
		else:
			playing_s = mfiles[next_s]

	else:
		playing_s = mfiles[0]

	state.delete('1.0','end-1c')
	state.insert(END,playing_s)
	media = instance.media_new("video/"+playing_s)
	player.set_media(media)
	player.play()
	time.sleep(1)

def prevV():
	mfiles = os.listdir("video/")

	curent_s = state.get('1.0','end-1c')

	if curent_s in mfiles:
		prev_s = mfiles.index(curent_s)-1

		if prev_s <= 0:
			playing_s = len(mfiles)-1
			playing_s = mfiles[playing_s]
		else:
			playing_s = prev_s
			playing_s = mfiles[playing_s]
	else:
		playing_s = mfiles[0]

	state.delete('1.0','end-1c')
	state.insert(END,playing_s)
	media = instance.media_new("video/"+playing_s)
	player.set_media(media)
	player.play()
	time.sleep(1)

def nextM():
	mfiles = os.listdir("audio")
	start_s = mfiles[0]

	curent_s = state.get('1.0','end-1c')

	if curent_s in mfiles:

		next_s = mfiles.index(curent_s)+1

		if next_s>=len(mfiles):
			playing_s = mfiles[0]
		else:
			playing_s = mfiles[next_s]

	else:
		playing_s = mfiles[0]

	state.delete('1.0','end-1c')
	state.insert(END,playing_s)
	media = instance.media_new("audio/"+playing_s)
	player.set_media(media)
	player.play()
	time.sleep(1)

def prevM():
	mfiles = os.listdir("audio/")

	curent_s = state.get('1.0','end-1c')

	if curent_s in mfiles:
		prev_s = mfiles.index(curent_s)-1

		if prev_s <= 0:
			playing_s = len(mfiles)-1
			playing_s = mfiles[playing_s]
		else:
			playing_s = prev_s
			playing_s = mfiles[playing_s]
	else:
		playing_s = mfiles[0]

	state.delete('1.0','end-1c')
	state.insert(END,playing_s)
	media = instance.media_new("audio/"+playing_s)
	player.set_media(media)
	player.play()
	time.sleep(1)

def get_audio(*args):
    r = sr.Recognizer()

    with sr.Microphone() as source:
    	state.delete('1.0', END)
    	state.insert('1.0',"Listening...")
    	pauseM()
    	speak("Speak Now!")
    	audio = r.listen(source)
    	state.delete('1.0', END)
    	state.insert('1.0',"Thinking...")
    	said = ""
    	
    	try:
    		said = r.recognize_google(audio)
    		print("You said : "+said)
    		state.delete('1.0', END)
    		state.insert('1.0', "I heard : "+said)
    		pauseB.grid_remove()
	    	nextB.grid_remove()
	    	prevB.grid_remove()

	    	if said in greet:
	    		pa.grid_remove()
	    		random_greeting = random.choice(greet)
	    		state.insert(END,random_greeting)
	    		speak(random_greeting+users[0])
	    		state.delete('1.0', END)
	    	elif said in var1:
	    		pa.grid_remove()
	    		state.delete('1.0', END)
	    		random_response = random.choice(var2)
	    		state.insert('1.0',random_response)
	    		speak(random_response)
	    	elif said in cmdbsu:
	    		result = wikipedia.summary(cmd,sentences=5)
	    		state.delete('1.0','end-1c')
	    		state.insert(END,result)
	    		speak("According to wikipedia")
	    		speak(result)

	    	elif said in cmd11:
	    		speak("Opening B S U students portal")
	    		webbrowser.open_new_tab("https://students.bsu.ac.ug")
	    	elif said in cmd12:
	    		speak("Opening b s u website.")
	    		webbrowser.open_new_tab("https://bsu.ac.ug")
	    	elif said in cmd14:
	    		speak("BSU core values include.")
	    		speak(cmd13)
	    	elif said in cmd6:
	    		pa.grid_remove()
	    		state.delete('1.0', END)
	    		state.insert('1.0',"Exiting...")
	    		speak("goodbye"+users[0])
	    		bot.destroy()
	    	elif said in question:
	    		random_responses = random.choice(responses)
	    		speak(random_responses)
	    		state.delete('1.0', END)
	    	elif said in cmd2:
	    		prevB.grid(row=4, column=0)
	    		pauseB.grid(row=4, column=1)
	    		nextB.grid(row=4, column=2)
	    		pauseB.config(command=pauseM)
	    		prevB.config(command=prevM)
	    		nextB.config(command=nextM)
	    		state.delete('1.0', END)
	    		speak("I am opening a song")
	    		state.insert(END,"Playing Music")
	    		mfiles = os.listdir("C:/Users/Muzoora Barnabas/Desktop/muzk")
	    		song = random.choice(mfiles)
	    		state.delete('1.0',END)
	    		state.insert('1.0',song)
	    		media = instance.media_new("C:/Users/Muzoora Barnabas/Desktop/muzk/"+song)
	    		player.set_media(media)
	    		player.play()
	    		time.sleep(1)
	    	elif said in cmdVid:
	    		prevB.grid(row=4, column=0)
	    		pauseB.grid(row=4, column=1)
	    		nextB.grid(row=4, column=2)
	    		pauseB.config(command=pauseM)
	    		nextB.config(command=nextV)
	    		prevB.config(command=prevV)
	    		speak("I am opening a video")
	    		mfiles = os.listdir("video/")
	    		video = random.choice(mfiles)
	    		media = instance.media_new("video/"+video)
	    		state.delete('1.0',END)
	    		state.insert('1.0',video)
	    		player.set_media(media)
	    		player.play()
	    		time.sleep(1)

	    	elif said in cmd3:
	    		random_joke=random.choice(jokes)
	    		speak(random_joke)
	    	elif said in var4:
	    		speak("My name is Barna. I am your personal assistant. I was created to make your life easy. Thanks for asking.")
	    	elif said in cmd10:
	    		speak('I am locking your computer. goodbye '+users[0])
	    		bot.destroy()
	    		os.system('cmd /k "color a & shutdown/h"')
	    	else:
	    		pa.grid_remove()
	    		state.delete('1.0', END)
	    		# speak("I cannot find the matching answer, try again "+users[0])
	    		notification.notify(
			 		title="Barna The Bot",
			 		message = "I cannot find the matching answer, try again "+users[0],
			 		app_name = "",
			 		app_icon = "images/robot.ico"
			 	)
    	except Exception as e:
	    	pa.grid_remove()
	    	state.delete('1.0', END)
	    	# speak("Sorry"+users[0]+". I couldnot understand what you said. Try again!")
    		notification.notify(
			 		title="Barna The Bot",
			 		message = "Sorry "+users[0]+". I couldnot understand what you said. Try again!",
			 		app_name = "",
			 		app_icon = "images/robot.ico"
			 	)

# close bot application with a message
def close():
	pauseM()
	speak("It was nice serving you!")
	try:
		speak("Good bye "+users[0])
	except Exception as e:
		speak("Good bye.")
	bot.destroy()



bot.protocol("WM_DELETE_WINDOW", close)
bot.mainloop()