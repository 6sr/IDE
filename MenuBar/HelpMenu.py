import os
import hashlib
import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import ttk

    #######################################  HELP FUNCTIONS  ###################################################
class HelpMenuClass:
    NotepadReference = None
    def __init__(self,**kwargs):
        try:
            self.NotepadReference = kwargs['NotepadObject']
        except KeyError:
            pass

    def showAbout(self):
        showinfo("IDE", "Made with ❤️ by  AGSR ")
