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
    	import sys 
    	python_code = """import sys 
#sys.stdin = self.NotepadReference.input_file 
sys.stdout = open('output.txt','w')

"""
    	
    	
    	
		
		
    	my_code = self.NotepadReference.NotepadTextArea.get(1.0, END)
    	final_code = python_code+my_code
    	#print(final_code)
    	exec(final_code)


        
        

        

