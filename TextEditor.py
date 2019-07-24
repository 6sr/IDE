import os
import hashlib
import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import ttk

# Importing Menu Bar Files
from MenuBar.FileMenu import FileMenuClass
from MenuBar.EditMenu import EditMenuClass
from MenuBar.SearchMenu import SearchMenuClass
from MenuBar.ToolsMenu import ToolsMenuClass
from MenuBar.HelpMenu import HelpMenuClass
from MenuBar.RunCode import RunCodeClass


class Notepad:
    master = Tk()
    
    file = None
    
    # default window width and height
    NotepadWidth = 100
    NotepadHeight = 100
    NotepadTextArea = Text(master,bg = '#00001a', fg = "#ffffff", insertbackground = "#ffffff", undo = True, font=("Consolas", 11))
    NotepadMenuBar = Menu(master)
    NotepadScrollbar = Scrollbar(NotepadTextArea)

    bracketsInText = 0
    
    MenuBarDict = {
        "FileMenu": Menu(NotepadMenuBar, tearoff=0),
        "EditMenu": Menu(NotepadMenuBar, tearoff=0),
        "SearchMenu": Menu(NotepadMenuBar, tearoff=0),
        "ToolsMenu": Menu(NotepadMenuBar, tearoff=0),
        "HelpMenu": Menu(NotepadMenuBar, tearoff=0)
    }
    
    def __init__(self,**kwargs):

        # Set window size
        try:
            self.NotepadWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.NotepadHeight = kwargs['height']
        except KeyError:
            pass

        # Setting icon of master window
        try:
            self.master.iconbitmap("IconIDE.ico")
        except:
            pass

        self.set_dimensions(self.master,height = self.NotepadHeight,width = self.NotepadWidth)

        # Adding the Title
        self.master.title("Untitled - IDE")
        
        # Adding Primary menu to the master window
        self.master.config(menu = self.NotepadMenuBar)
        
        #######################################   KEY BINDINGS   ########################################################
        keyList = ["KeyPress-Return", "Tab", "}", "{"]     # "Enter"
        for buttonPressed in keyList:
            self.NotepadTextArea.bind('<' + buttonPressed + '>',self.handlePressedKey)
            # lambda evt, temp=button_name: self.OnButton(evt, temp)
            # self.NotepadTextArea.bind("<Enter>", self.AddIndentation)
            # self.NotepadTextArea.bind("<KeyRelease-Return>", self.AddIndentation)
            # self.NotepadTextArea.bind("<}>", closeBracketPressed)
            # self.NotepadTextArea.bind("<Tab>", tabPressed)
        
        #######################################   MENU BAR   ########################################################
        ##### Adding secondary menus to the primary menu bar #####
        # ["",None] adds line in the dropdown
        FileMenuObj = FileMenuClass(NotepadObject = self)
        fileOptions = [
            ["New",FileMenuObj.newFile],
            ["Open",FileMenuObj.openFile],
            ["Save",FileMenuObj.saveFile],
            ["",None],
            ["Exit",FileMenuObj.quitApplication]
        ]
        self.addMenuToMenuBar("File",fileOptions)
        
        EditMenuObj = EditMenuClass(NotepadObject = self)
        editOptions = [
            ["Undo",EditMenuObj.undo],
            ["Redo",EditMenuObj.redo],
            ["",None],
            ["Cut",EditMenuObj.cut],
            ["Copy",EditMenuObj.copy],
            ["Paste",EditMenuObj.paste],
            ["Select All",EditMenuObj.selectAll]
        ]
        self.addMenuToMenuBar("Edit",editOptions)

        SearchMenuObj = SearchMenuClass(NotepadObject = self)
        searchOptions = [
            ["Find",SearchMenuObj.findText],
            ["Replace",SearchMenuObj.replaceText]
        ]
        self.addMenuToMenuBar("Search",searchOptions)

        ToolsMenuObj = ToolsMenuClass(NotepadObject = self)
        toolOptions = [
            ["Convert file to MD5",ToolsMenuObj.md5Text],
            ["Convert file to SHA-256",ToolsMenuObj.sha256Text]
        ]
        self.addMenuToMenuBar("Tools",toolOptions)

        HelpMenuObj = HelpMenuClass(NotepadObject = self)
        helpOptions = [
            ["About Notepad",HelpMenuObj.showAbout]
        ]
        self.addMenuToMenuBar("Help",helpOptions)

        ###########################   RUN BUTTON   ######################################
        run_button = Button(self.master,bg = 'red',text = "RUN",command = RunCodeClass.RunFile)
        run_button.place(x = 400,y = 0)

        # To make the textarea auto resizable
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        #######################################   SCROLLBAR   ####################################################

        self.NotepadScrollbar.pack(side=RIGHT, fill=Y)

        # To adjust Scrollbar according to content automatically
        self.NotepadScrollbar.config(command=self.NotepadTextArea.yview)
        self.NotepadTextArea.config(yscrollcommand=self.NotepadScrollbar.set)

        ####################################      ADDING TEXT AREA   ######################################
        self.NotepadTextArea.pack(fill=BOTH,expand = 1)


############################################################  CONSTRUCTOR OVER  ##########################################################################


    ##################################  CONSTRUCTOR FUNCTIONS  ##########################################################
    def handlePressedKey(self, keyPressed):
        #print("Pressed")
        print(keyPressed)
        if keyPressed.char == "\r":
            self.NotepadTextArea.insert("insert", '\n')
            self.AddIndentation()
        elif keyPressed.char == "\t":
            self.NotepadTextArea.insert("insert", ' ' * 4)
        elif keyPressed.char == "{":
            self.NotepadTextArea.insert("insert", '{')
            self.bracketsInText += 1
        elif keyPressed.char == "}":
            self.bracketsInText -= 1
            curr = self.NotepadTextArea.get("end-1c linestart","end")
            #print(':' + curr + ':')
            if curr.strip() == "" or curr == None:
                self.NotepadTextArea.delete("end-5c","end")
                if curr == "    \n":    # Four spaces then \n
                    self.NotepadTextArea.insert("insert", '\n')
            self.NotepadTextArea.insert("insert", '}')
        # print("Pressed")
        return 'break'
    
    def set_dimensions(self,master,**kwargs):
        try:
            self.NotepadWidth = kwargs['width']
        except:
            pass

        try:
            self.NotepadHeight = kwargs['height']
        except:
            pass

        ScreenWidth = self.master.winfo_screenwidth()
        ScreenHeight = self.master.winfo_screenheight()

        left = (ScreenWidth/2) - (self.NotepadWidth/2)
        top = (ScreenHeight/2) - (self.NotepadHeight/2)

        master.geometry('%dx%d+%d+%d' %(self.NotepadWidth,self.NotepadHeight,left,top))


    def addMenuToMenuBar(self,name,optionList):
        refName = name + "Menu"
        for currOption in optionList:
            if currOption[0] == "":
                # To create a line in the dialog
                self.MenuBarDict[refName].add_separator()
            else:
                # Adding option
                self.MenuBarDict[refName].add_command(label = currOption[0], command = currOption[1])
        
        # Adding menu in menu bar
        self.NotepadMenuBar.add_cascade(label = name, menu = self.MenuBarDict[refName])

    def AddIndentation(self):
        currText = str(self.NotepadTextArea.get(1.0,END)).strip()
        def AddSpaces():
            self.NotepadTextArea.insert("insert", ' ' * 4 * self.bracketsInText)

        currLen = len(currText) - 1
        print(":" + currText + ":" + "Len : " + str(currLen))
        #if currText[currLen] == '{' or currText[currLen] == ':':
        #    print(":" + currText + ":")
        #    AddSpaces()
        #else:
        #    print(":" + currText + ":")
        print(":" + currText + ":")
        AddSpaces()

    def run(self):
        self.master.mainloop()

# Creating object of Notepad class to run my "Notepad" software
obj = Notepad(width = 1000,height = 500)
obj.run()
