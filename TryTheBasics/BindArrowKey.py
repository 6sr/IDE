def arrow_down(event):
    print "arrow down"

def arrow_up(event):
    print "arrow up"

root = tk.Tk()
tk.Label(root, text="Press a key (Escape key to exit):" ).grid()

root.bind('<Down>', arrow_down)
root.bind('<Up>', arrow_up)

root.mainloop()