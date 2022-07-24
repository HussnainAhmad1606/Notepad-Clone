from tkinter import *
import tkinter.simpledialog  as sd
import tkinter.messagebox as tmsg
import webbrowser
import keyboard
from datetime import datetime
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


file = None;


root = Tk()

photo = PhotoImage(file = "logo.png")

root.iconphoto(False, photo)

root.title("Untitled - Psycho Pad")
root.geometry("600x500")


'''
All functions for menu commands
'''
# Function for checking purposes only! 
def check(event):
	print("Your function is working properly!")

# Function to show About details on popup
def about():
	tmsg.showinfo("About", "Psycho Pad\nA Utility for writing your notes and save them for later usage.\nProgrammer: Hussnain Ahmad")

def openWebsite():
	webbrowser.open("www.hussnainahmad.com")

# Function to change the font of the editor
# Asks the user to enter font name and font size
# I wrote one more function that open a seperate window named "fontWindow"
def fontChange():
	fontName = sd.askstring("Font Name", "Enter Font Name: ")
	fontSize = sd.askinteger("Font Size", "Enter Font Size: ")	
	text.config(font=(fontName, fontSize))
	tmsg.showinfo("Font Changed", "Psycho Pad font changed Successfully")

# Function to undo the effect TODO
def undoMenu():
	keyboard.press_and_release("ctrl-z")

# Function to cut the text
def cut():
	keyboard.press_and_release("ctrl+x")

# Function to copy the text
def copy():
	keyboard.press_and_release("ctrl+c")

# Function to paste the copied text
def paste():
	keyboard.press_and_release("ctrl+v")

# TODO:
# Function to delete the text
def delete():
	keyboard.press_and_release("backspace")


# Function to paste the current date and time on editor using shortcut F5
def todayDateTimeFunc(event):
	today = datetime.now()
	todayDateTime = today.strftime("%I:%M %p %d/%m/%Y")
	print(todayDateTime)
	keyboard.write(todayDateTime)


# Function to paste the current date and time on editor using menu
def todayDateTimeMenu():
	today = datetime.now()
	todayDateTime = today.strftime("%I:%M %p %d/%m/%Y")
	print(todayDateTime)
	keyboard.write(todayDateTime)

# Function to find the text entered by the user
def findText():	
	userText = sd.askstring("Text", "Enter Text to Find: ")
	fileText = text.get("1.0", END)
	found = fileText.find(userText)
	replaced = fileText.replace(userText, f"\033[44;33m{userText}\033[m")
	text.insert(replaced)
	print(found)
	if userText in fileText:
		tmsg.showinfo("Found", f"{userText} found in the file")
	else:
		tmsg.showerror("ERROR!", f"{userText} not found in the file")
	print(userText)

# Function to rate the software
# Not done yet user just rate the software. But i can't store value anywhere will do this later #TODO:
def rate():
	def rateDone():
		tmsg.showinfo("Rating Done", f"Thanks for the rating of {rateScore.get()}. We hope you enjoy working with our Software.")
		rate.quit

	def desc_space(text):
		final_text = ""
		for i in range(0, len(text)):
			final_text += text[i]
			if i%35==0 and i != 0:
				final_text += "\n"
		return final_text
	rate = Tk()
	rate.title("Rate This Software")
	rate.geometry("400x300")
	Label(rate, text="Rate The Software", font=("Calibri", 20, "bold")).pack()
	Label(rate, text=desc_space("Thank You for using this Software. We made this software to ensure that you will get benefit from this software. If you enjoy using this software then Rate the software Now. It will take a few minutes."), font=("Calibri", 16)).pack()
	rateScore = Scale(rate, from_=0, to=10, tickinterval=5, orient=HORIZONTAL)
	rateScore.pack()
	Button(rate, text="Rate Now", command=rateDone).pack()
	rate.mainloop()



# New Font Change window
# TODO:
# Have to retrive the value selected by user and set font accordingly
def fontWindow():
	font = Tk()
	font.title("Font Change Window")
	font.geometry("300x300")
	Label(font, text="Change Font", font=("Calibri", 20, "bold")).pack()
	fontLists = Listbox(font)
	fonts = ["Arial", "American Captain", "Berlin Sans FB", "Calibri"]
	for i in range(0, len(fonts)):
		fontLists.insert(END, fonts[i])
	fontLists.pack(side=LEFT, anchor=W, padx=5)


	fontSize = Listbox(font)
	for i in range(10, 51, 2):
		fontSize.insert(END, i)
	fontSize.pack(side=RIGHT, anchor=E, padx=5)

	def changeFontWindow():
		tmsg.showinfo("Change", "Font Changed")

	Button(font, text="Apply Font", command=changeFontWindow, padx=50).pack()
	font.mainloop()

def newFile():
	global file
	file = None
	root.title("Untitled - Psycho Pad")
	text.delete(1.0, END)

def openFile():
	global file
	root.title("Untitled - Psycho Pad")
	file = None
	text.delete(1.0, END)
	file = askopenfilename(defaultextension=".txt",
		filetypes=[("All Types", "*.*"),
		("Text Documents", "*.txt")])
	if file == "":
		file == None
	else:
		root.title(os.path.basename(file) + " - Psycho Pad")
		text.delete(1.0, END)
		f = open(file, "r")
		text.insert(1.0, f.read())


def saveFile():
	global file
	if file == None:
		file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
		filetypes=[("All Types", "*.*"),
		("Text Documents", "*.txt")])

		if file == "":
			file = None
		else:
			# save as new file
			f = open(file, "w")
			f.write(text.get(1.0, END))
			f.close()
			root.title(os.path.basename(file) + " - Psycho Pad")
			print("File Saved")
	else:
		# save the file
			f = open(file, "w")
			f.write(text.get(1.0, END))
			f.close()
	print(file)

'''
Menu Functions END
'''


# Main Menu
mainMenu = Menu()

# File Menu
fileMenu = Menu(mainMenu, tearoff=0)
fileMenu.add_command(label="New", command=newFile)
fileMenu.add_command(label="Open..", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
# fileMenu.add_command(label="Save As..", command=check)
fileMenu.add_separator()
fileMenu.add_command(label="Page Setup", command=check)
fileMenu.add_command(label="Print", command=check)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.destroy)
mainMenu.add_cascade(label="File", menu=fileMenu)
root.config(menu=mainMenu)

# Edit Menu
editMenu = Menu(mainMenu, tearoff=0)
editMenu.add_command(label="Undo", command=undoMenu)
editMenu.add_separator()
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)
editMenu.add_command(label="Delete", command=delete)
editMenu.add_separator()
editMenu.add_command(label="Find", command=findText)
editMenu.add_command(label="Replace", command=check)
editMenu.add_separator()
editMenu.add_command(label="Date/Time", command=todayDateTimeMenu)
mainMenu.add_cascade(label="Edit", menu=editMenu)
root.config(menu=mainMenu)


# format Menu
formatMenu = Menu(mainMenu, tearoff=0)
# TODO: write the function for font wrap
formatMenu.add_checkbutton(label="Font Wrap", command=check)
formatMenu.add_command(label="Font", command=fontWindow)
mainMenu.add_cascade(label="Format", menu=formatMenu)
root.config(menu=mainMenu)

# View Menu
viewMenu = Menu(mainMenu, tearoff=0)
viewMenu.add_checkbutton(label="Status Bar",)
mainMenu.add_cascade(label="View", menu=viewMenu)
root.config(menu=mainMenu)

# Help Menu
helpMenu = Menu(mainMenu, tearoff=0)
helpMenu.add_command(label="About", command=about)
helpMenu.add_separator()
helpMenu.add_command(label="Rate This Software", command=rate)
helpMenu.add_command(label="Visit Website", command=openWebsite)
mainMenu.add_cascade(label="Help", menu=helpMenu)
root.config(menu=mainMenu)



# scroll bar X and Y seperately
scrollbarY = Scrollbar(root)
scrollbarX = Scrollbar(root, orient=HORIZONTAL)

scrollbarY.pack(fill=Y, side=RIGHT)
scrollbarX.pack(fill=X, side=BOTTOM)

# Main text area where user can write
editorBackground = "white" #"#0c274a"
editorFontColor = "black"
# Main Notepad Default Font Name and Font Size
defaultFont = ("Calibri", 20)

text = Text(root, wrap="none", bg=editorBackground, fg=editorFontColor, yscrollcommand=scrollbarY.set, xscrollcommand=scrollbarX.set, width=600, height=500, padx=5, pady=5, font=defaultFont, undo=True, maxundo=10)
text.pack()
scrollbarY.config(command=text.yview)
scrollbarX.config(command=text.xview)


# Handling KeyBoard Shortcuts
root.bind("<F5>", todayDateTimeFunc)


root.mainloop()
