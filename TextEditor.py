import os
import hashlib
import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import ttk

class Notepad:
    master = Tk()
    
    file = None
    
    # default window width and height
    NotepadWidth = 100
    NotepadHeight = 100
    NotepadTextArea = Text(master,bg = '#00001a', fg = "#ffffff", insertbackground = "#ffffff", undo = True, font=("Verdana", 11), tabs = 20)
    NotepadMenuBar = Menu(master)
    NotepadScrollbar = Scrollbar(NotepadTextArea)
    
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
        
        # Binding Enter key press event to AddIndentation function
        self.NotepadTextArea.pack()
        self.NotepadTextArea.bind("<KeyRelease-Return>", self.AddIndentation)

        ##### Adding secondary menus to the primary menu bar #####
        # ["",None] adds line in the dropdown
        fileOptions = [
            ["New",self.newFile],
            ["Open",self.openFile],
            ["Save",self.saveFile],
            ["",None],
            ["Exit",self.quitApplication]
        ]
        self.addMenuToMenuBar("File",fileOptions)
        
        editOptions = [
            ["Undo",self.undo],
            ["Redo",self.redo],
            ["",None],
            ["Cut",self.cut],
            ["Copy",self.copy],
            ["Paste",self.paste],
            ["Select All",self.selectAll]
        ]
        self.addMenuToMenuBar("Edit",editOptions)

        searchOptions = [
            ["Find",self.findText],
            ["Replace",self.replaceText]
        ]
        self.addMenuToMenuBar("Search",searchOptions)

        toolOptions = [
            ["Convert file to MD5",self.md5Text],
            ["Convert file to SHA-256",self.sha256Text]
        ]
        self.addMenuToMenuBar("Tools",toolOptions)

        helpOptions = [
            ["About Notepad",self.showAbout]
        ]
        self.addMenuToMenuBar("Help",helpOptions)

        ###########################   RUN BUTTON   ######################################
        run_button = Button(self.master,bg = 'red',text = "RUN",command = self.RunFile)
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
        for i in optionList:
            if i[0] == "":
                # To create a line in the dialog
                self.MenuBarDict[refName].add_separator()
            else:
                # Adding option
                self.MenuBarDict[refName].add_command(label = i[0], command = i[1])
        
        # Adding menu in menu bar
        self.NotepadMenuBar.add_cascade(label = name, menu = self.MenuBarDict[refName])

    def AddIndentation(self,event):
        currText = str(self.NotepadTextArea.get(1.0,END)).strip()
        def AddSpaces():
            self.NotepadTextArea.insert("end", "    ")

        currLen = len(currText) - 1
        if currText[currLen] == '{' or currText[currLen] == ':':
            print("1" + currText)
            AddSpaces()
        else:
            print("LOL" + currText)


    ################################   FILE FUNCTIONS   ##########################################################

    def newFile(self):
        self.master.title("Untitled - Notepad")
        self.file = None
        self.NotepadTextArea.delete(1.0,END)

    def openFile(self):
        self.file = askopenfilename(defaultextension = ".txt", filetypes = [("All Files","*.*"), ("Text Documents","*.txt")])
        if self.file == "":
            # no file to open
            self.file = None
        else:
            # Try to open the file
            # set the window title
            self.master.title(os.path.basename(self.file) + " - Notepad")
            self.NotepadTextArea.delete(1.0,END)
            file = open(self.file,"r")
            data = file.read()
            self.NotepadTextArea.insert(1.0,data)
            file.close()

    def saveFile(self):
        #If we want to save the new file
        if self.file == None:
            self.file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension = ".txt", filetypes = [("All Files","*.*"), ("Text Documents","*.txt")])

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
        popup_master = Toplevel()
        self.set_dimensions(popup_master,width = 160, height = 100)
        popup_master.title("Want To Save")
        labelBonus = Label(popup_master,text = "Want To Save?")
        OptionMenu = Label(popup_master)
        labelBonus.grid(row = 0, column = 0)
        OptionMenu.grid(row=1,column = 0)

        def yes_function():
            self.SaveFile()
            popup_master.destroy()


        def no_function():
            popup_master.destroy()
            self.master.destroy()

        yes_button = ttk.Button(OptionMenu,text = 'Yes',command = yes_function )
        no_button = ttk.Button(OptionMenu,text = 'No', command = no_function)
        yes_button.pack(fill = X,side = LEFT)
        no_button.pack(fill = X,side = LEFT)
        popup_master.mainloop()

##############################################  RUN BUTTON  #########################################################
    def RunFile(self):
        exec(self.NotepadTextArea.get(1.0, END))

 ############################################   EDIT FUNCTIONS  #############################################

    def undo(self):
        self.NotepadTextArea.event_generate("<<Undo>>")
    
    def redo(self):
        self.NotepadTextArea.event_generate("<<Redo>>")
    
    def cut(self):
        self.NotepadTextArea.event_generate("<<Cut>>")

    def copy(self):
        self.NotepadTextArea.event_generate("<<Copy>>")

    def paste(self):
        self.NotepadTextArea.event_generate("<<Paste>>")
    
    def selectAll(self):
        self.NotepadTextArea.event_generate("<<SelectAll>>")
    
 ############################################   SEARCH FUNCTIONS  #############################################

    def findText(self):
        print("Find")
    
    def replaceText(self):
        print("Replace")
    
 ############################################   TOOLS FUNCTIONS  #############################################

    def md5Text(self):
        print("MD5")
        str = "Text Editor by AGSR"
        result = hashlib.md5(str.encode()) 
        print(result.hexdigest())

    def sha256Text(self):
        print("SHA-256")
    
    #######################################  HELP FUNCTIONS  ###################################################

    def showAbout(self):
        showinfo("IDE", "Made with ❤️ by  AGSR ")

    def run(self):
        self.master.mainloop()

# Creating object of Notepad class to run my "Notepad" software
obj = Notepad(width = 1000,height = 500)
obj.run()