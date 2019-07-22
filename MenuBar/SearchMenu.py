import os
import hashlib
import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import ttk

 ############################################   SEARCH FUNCTIONS  #############################################
class SearchMenuClass:
    NotepadReference = None
    def __init__(self,**kwargs):
        try:
            self.NotepadReference = kwargs['NotepadObject']
        except KeyError:
            pass

    def replaceText(self):
        print("Replace")


    def findText(self):
        popup_master = Toplevel()
        self.NotepadReference.set_dimensions(popup_master,width = 160, height = 100)
        popup_master.title("FIND")

        w = StringVar()
        e = Entry(popup_master,textvariable = w)
        
        e.pack(side=LEFT)
        
        e.focus_set()

        #text = self.NotepadTextArea.get(1.0,END)
        #print(text)

        def find():

            toFind = w.get()
            
            print(toFind)
            countVar = StringVar()
            start = "1.0"
            flag = 0
            while(True):
                try:
                    startFind = self.NotepadReference.NotepadTextArea.search(toFind, start, stopindex="end", count=countVar)
                

                    lineNum = startFind.split('.')[0]
                    startIdx = startFind.split('.')[1]
                    endFind = startFind.split('.')[0] + '.' + str(int(startFind.split('.')[1]) + len(toFind))

                    self.NotepadReference.NotepadTextArea.tag_add("search", startFind, endFind)
                    self.NotepadReference.NotepadTextArea.tag_config("search", background="black", foreground="yellow")

                    print(startFind)
                    print(endFind)
                    print(countVar)
                    start = endFind
                    flag += 1

                except:
                    if flag > 0:
                        print("Done")
                    else:
                        print("Your word is not found")
                
                    break

        b = ttk.Button(popup_master,text = 'Find' , command = find)
        b.pack(side=LEFT)
        popup_master.mainloop()

