import os
import hashlib
import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import ttk


##############################################  RUN BUTTON  #########################################################
class RunCodeClass:
    NotepadReference = None
    def __init__(self,**kwargs):
        try:
            self.NotepadReference = kwargs['NotepadObject']
        except KeyError:
            pass

    def RunFile(self):
        exec(self.NotepadReference.NotepadTextArea.get(1.0, END))

