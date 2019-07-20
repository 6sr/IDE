from tkinter import *

root = Tk()

text = Text(root)
text.insert(INSERT, "Hello, world!\n")
text.insert(END, "This is a phrase.\n")
text.insert(END, "Bye bye...")
text.pack(expand=1, fill=BOTH)


while(True):
    toFind = input("Enter : ")
    try:
        text.tag_remove("search", startFind, endFind)
    except:
        print("Error Removing")
    try:
        countVar = StringVar()
        start = "1.0"
        while(True):
            try:
                startFind = text.search(toFind, start, stopindex="end", count=countVar)
                # text.sear

                lineNum = startFind.split('.')[0]
                startIdx = startFind.split('.')[1]
                endFind = startFind.split('.')[0] + '.' + str(int(startFind.split('.')[1]) + len(toFind))

                text.tag_add("search", startFind, endFind)

                print(startFind)
                print(endFind)
                print(countVar)
                start = endFind
            except:
                break

        # adding a tag to a part of text specifying the indices
        # text.tag_add("start", "1.8", "1.13")
        text.tag_config("search", background="black", foreground="yellow")
    except:
        print("Error finding")


root.mainloop()
