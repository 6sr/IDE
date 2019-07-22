import os
import hashlib
import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import ttk

 ############################################   EDIT FUNCTIONS  #############################################
class EditMenuClass:
    NotepadReference = None
    def __init__(self,**kwargs):
        try:
            self.NotepadReference = kwargs['NotepadObject']
        except KeyError:
            pass

    def undo(self):
        print(self)
        self.NotepadReference.NotepadTextArea.event_generate("<<Undo>>")

    def redo(self):
        print(self)
        self.NotepadReference.NotepadTextArea.event_generate("<<Redo>>")

    def cut(self):
        print(self)
        self.NotepadReference.NotepadTextArea.event_generate("<<Cut>>")

    def copy(self):
        print(self)
        self.NotepadReference.NotepadTextArea.event_generate("<<Copy>>")

    def paste(self):
        print(self)
        self.NotepadReference.NotepadTextArea.event_generate("<<Paste>>")

    def selectAll(self):
        print(self)
        self.NotepadReference.NotepadTextArea.event_generate("<<SelectAll>>")
