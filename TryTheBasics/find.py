from tkinter import *

root = Tk()

text = Text(root)
text.insert(INSERT, "Hello, world!\n")
text.insert(END, "This is a phrase.\n")
text.insert(END, "Bye bye... Hello")
text.pack(expand=1, fill=BOTH)



toFind = input("Enter : ")
countVar = StringVar()
start = "1.0"
flag = 0
while(True):
        try:
            startFind = text.search(toFind, start, stopindex="end", count=countVar)
                

            lineNum = startFind.split('.')[0]
            startIdx = startFind.split('.')[1]
            endFind = startFind.split('.')[0] + '.' + str(int(startFind.split('.')[1]) + len(toFind))

            text.tag_add("search", startFind, endFind)
            text.tag_config("search", background="black", foreground="yellow")

            print(startFind)
            print(endFind)
            print(countVar)
            start = endFind
            flag += 1

        except:
            if flag>0:
                print("Done")
            else:
                print("Your word is not found")
                
            break

       


root.mainloop()
