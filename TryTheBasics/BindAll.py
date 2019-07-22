try:
    import Tkinter as tk     ## Python 2.x
except ImportError:   
    import tkinter as tk     ## Python 3.x

def key_in(event):
    ##shows key or tk code for the key
    if event.keysym == 'Escape':
        root.quit()
    if event.char == event.keysym:
        # normal number and letter characters
        print('Normal Key', event.char)
    elif len(event.char) == 1:
        # charcters like []/.,><#$ also Return and ctrl/key
        print( 'Punctuation Key %r (%r)' % (event.keysym, event.char) )
    else:
        # f1 to f12, shift keys, caps lock, Home, End, Delete ...
        print( 'Special Key %r' % event.keysym )

root = tk.Tk()
tk.Label(root, text="Press a key (Escape key to exit):" ).grid()

ent=tk.Entry(root)
ent.bind_all('<Key>', key_in)  # <==================
ent.focus_set()

root.mainloop()

