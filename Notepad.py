# run() - Calls the mainloop() function to run __init__
# newFile() - creating new file
# openFile() - open saved file
# saveFile() - saving file
# cut(), copy(), paste() - perform same operations
# showAbout() - showing description
# quitApplication() - exit notepad

import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Notepad:
	master = Tk()	# lolololol If you understand

	# default window width and height
	NotepadWidth = 100
	NotepadHeight = 100
	NotepadTextArea = Text(master)
	NotepadMenuBar = Menu(master)
	NotepadFileMenu = Menu(NotepadMenuBar, tearoff=0)
	NotepadEditMenu = Menu(NotepadMenuBar, tearoff=0)
	NotepadHelpMenu = Menu(NotepadMenuBar, tearoff=0)

	# Add Scrollbar
	NotepadScrollbar = Scrollbar(NotepadTextArea)
	file = None

	def __init__(self,**kwargs):

		# Setting icon of master window
		try:
				self.master.iconbitmap("SR.ico")
		except:
				pass

		# Set window size (the default is 300x300)
		try:
			self.NotepadWidth = kwargs['width']
		except KeyError:
			pass

		try:
			self.NotepadHeight = kwargs['height']
		except KeyError:
			pass

		# Set the window text
		self.master.title("Untitled - Notepad")

		# Center the window
		screenWidth = self.master.winfo_screenwidth()
		screenHeight = self.master.winfo_screenheight()

		# For left-align
		left = (screenWidth / 2) - (self.NotepadWidth / 2)

		# For right-align
		top = (screenHeight / 2) - (self.NotepadHeight / 2)

		# For top and bottom
		self.master.geometry('%dx%d+%d+%d' % (self.NotepadWidth, self.NotepadHeight, left, top))

		# To make the textarea auto resizable
		self.master.grid_rowconfigure(0, weight=1)
		self.master.grid_columnconfigure(0, weight=1)

		# Add controls (widget)
		self.NotepadTextArea.grid(sticky = N + E + S + W)

		# Adding New option
		self.NotepadFileMenu.add_command(label="New", command=self.newFile)

		# Adding Open option
		self.NotepadFileMenu.add_command(label="Open", command=self.openFile)

		# Adding Save option
		self.NotepadFileMenu.add_command(label="Save", command=self.saveFile)

		# To create a line in the dialog
		self.NotepadFileMenu.add_separator()

		# Adding Exit option
		self.NotepadFileMenu.add_command(label="Exit", command=self.quitApplication)

		# Adding File menu in menu bar
		self.NotepadMenuBar.add_cascade(label="File", menu=self.NotepadFileMenu)

		# Adding Cut option
		self.NotepadEditMenu.add_command(label="Cut", command=self.cut)

		# Adding Copy option
		self.NotepadEditMenu.add_command(label="Copy", command=self.copy)

		# Adding Paste option
		self.NotepadEditMenu.add_command(label="Paste", command=self.paste)

		# Adding Edit menu in menu bar
		self.NotepadMenuBar.add_cascade(label="Edit", menu=self.NotepadEditMenu)

		# Adding Description option
		self.NotepadHelpMenu.add_command(label="About Notepad", command=self.showAbout)

		# Adding Help menu in menu bar
		self.NotepadMenuBar.add_cascade(label="Help", menu=self.NotepadHelpMenu)

		self.master.config(menu=self.NotepadMenuBar)

		self.NotepadScrollbar.pack(side=RIGHT,fill=Y)

		# To adjust Scrollbar according to content automatically
		self.NotepadScrollbar.config(command=self.NotepadTextArea.yview)
		self.NotepadTextArea.config(yscrollcommand=self.NotepadScrollbar.set)

	def newFile(self):
		self.master.title("Untitled - Notepad")
		self.file = None
		self.NotepadTextArea.delete(1.0,END)

	def openFile(self):
		self.file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
		if self.file == "":
			# no file to open
			self.file = None
		else:
			# Try to open the file
			# set the window title
			self.master.title(os.path.basename(self.file) + " - Notepad")
			self.NotepadTextArea.delete(1.0,END)
			file = open(self.file,"r")
			self.NotepadTextArea.insert(1.0,file.read())
			file.close()

	def saveFile(self):
		if self.file == None:
			# Save as new file
			self.file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])

			if self.file == "":
				self.file = None
			else:
				# Try to save the file
				file = open(self.file,"w")
				file.write(self.NotepadTextArea.get(1.0,END))
				file.close()

				# Change the window title
				self.master.title(os.path.basename(self.file) + " - Notepad")
		else:
			file = open(self.file,"w")
			file.write(self.NotepadTextArea.get(1.0,END))
			file.close()

	def quitApplication(self):
		self.master.destroy()

	def cut(self):
		self.NotepadTextArea.event_generate("<<Cut>>")

	def copy(self):
		self.NotepadTextArea.event_generate("<<Copy>>")

	def paste(self):
		self.NotepadTextArea.event_generate("<<Paste>>")

	def showAbout(self):
		showinfo("Notepad","SR")

	def run(self):
		self.master.mainloop()

# Creating object of Notepad class to run my "Notepad" software
obj = Notepad(width=1000,height=500)
obj.run()
