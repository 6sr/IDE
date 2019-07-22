import os
import hashlib
import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import ttk

    ################################   FILE FUNCTIONS   ##########################################################
class FileMenuClass:
    NotepadReference = None
    def __init__(self,**kwargs):
        try:
            self.NotepadReference = kwargs['NotepadObject']
        except KeyError:
            pass

    def newFile(self):
        self.NotepadReference.master.title("Untitled - Notepad")
        self.NotepadReference.file = None
        self.NotepadReference.NotepadTextArea.delete(1.0,END)

    def openFile(self):
        self.NotepadReference.file = askopenfilename(defaultextension = ".txt", filetypes = [("All Files","*.*"), ("Text Documents","*.txt")])
        if self.NotepadReference.file == "":
            # no file to open
            self.NotepadReference.file = None
        else:
            # Try to open the file
            # set the window title
            self.NotepadReference.master.title(os.path.basename(self.NotepadReference.file) + " - Notepad")
            self.NotepadReference.NotepadTextArea.delete(1.0,END)
            file = open(self.NotepadReference.file,"r")
            data = file.read()
            self.NotepadReference.NotepadTextArea.insert(1.0,data)
            file.close()

    def saveFile(self):
        print("Saving 1")
        #If we want to save the new file
        if self.NotepadReference.file == None:
            print("Saving 2")
            self.NotepadReference.file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension = ".txt", filetypes = [("All Files","*.*"), ("Text Documents","*.txt")])

            if self.NotepadReference.file == "":
                print("Saving 3")
                self.NotepadReference.file = None
            else:
                print("Saving 4")
                # Try to save the file
                file = open(self.NotepadReference.file,"w")
                file.write(self.NotepadReference.NotepadTextArea.get(1.0,END))
                file.close()

                # Change the window title
                self.NotepadReference.master.title(os.path.basename(self.NotepadReference.file) + " - Notepad")
                print("Saving 5")
        else:
            print("Saving 6")
            file = open(self.NotepadReference.file,"w")
            file.write(self.NotepadReference.NotepadTextArea.get(1.0,END))
            file.close()
            print("Saving 7")
        print("Saving 8")

    def quitApplication(self):
        popup_master = Toplevel()
        self.NotepadReference.set_dimensions(popup_master,width = 160, height = 100)
        popup_master.title("Want To Save")
        labelBonus = Label(popup_master,text = "Want To Save?")
        OptionMenu = Label(popup_master)
        labelBonus.grid(row = 0, column = 0)
        OptionMenu.grid(row=1,column = 0)

        def yes_function():
            self.saveFile()
            popup_master.destroy()


        def no_function():
            popup_master.destroy()
            self.NotepadReference.master.destroy()

        yes_button = ttk.Button(OptionMenu,text = 'Yes',command = yes_function )
        no_button = ttk.Button(OptionMenu,text = 'No', command = no_function)
        yes_button.pack(fill = X,side = LEFT)
        no_button.pack(fill = X,side = LEFT)
        popup_master.mainloop()
