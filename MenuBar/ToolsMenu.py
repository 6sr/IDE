import os
import hashlib
import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import ttk

 ############################################   TOOLS FUNCTIONS  #############################################
class ToolsMenuClass:
    NotepadReference = None
    def __init__(self,**kwargs):
        try:
            self.NotepadReference = kwargs['NotepadObject']
        except KeyError:
            pass

    def md5Text(self):
        print("MD5")
        str = "Text Editor by AGSR"
        result = hashlib.md5(str.encode()) 
        print(result.hexdigest())

    def sha256Text(self):
        print("SHA-256")
