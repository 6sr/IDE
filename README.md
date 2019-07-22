# IDE  
Notepad(width = 1000,height = 500) - Calls the \_\_init\_\_ function  
run(self) - Calls the mainloop() function to run infinite loop to accept tkinter window events

#### CONSTRUCTOR FUNCTIONS
- set_dimensions(self,master,**kwargs)
- addMenuToMenuBar(self,name,optionList)
- AddIndentation(self,event)
  
#### FILE FUNCTIONS
```./MenuBar/FileMenu/FileMenuClass```
- newFile(self) - creating new file
- openFile(self) - open saved file
- saveFile(self) - saving file
- quitApplication(self) - exit notepad
  
#### EDIT FUNCTIONS
```./MenuBar/EditMenu/EditMenuClass```
- undo(self)
- redo(self)
- cut(self)
- copy(self)
- paste(self)
- selectAll(self)
  
#### SEARCH FUNCTIONS
```./MenuBar/SearchMenu/SearchMenuClass```
- findText(self)
- replaceText(self)
  
#### TOOLS FUNCTIONS
```./MenuBar/ToolsMenu/ToolsMenuClass```
- md5Text(self)
- sha256Text(self)
  
#### HELP FUNCTIONS
```./MenuBar/HelpMenu/HelpMenuClass```
- showAbout(self) - showing description
  
#### RUN BUTTON
```./MenuBar/RunCode/RunCodeClass```
- RunFile(self) - Runs the entered code



