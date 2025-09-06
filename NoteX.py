from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog

def save():
    file_stuff = text.get(1.0, END)
    file = filedialog.asksaveasfile(defaultextension=".txt",
                                        filetypes=[
                                            ("Text File", ".txt"),
                                            ("HTML File", ".html"),
                                            ("Python File", ".py"),
                                            ("All Files", ".*"),
                                        ])
    if file:
        file.write(file_stuff)
        file.close()


def changebg():
    color = colorchooser.askcolor()
    hexcolor = color[1]
    text.config(bg=hexcolor)

def changefg():
    color = colorchooser.askcolor()
    hexcolor = color[1]
    text.config(foreground=hexcolor)

root = Tk()
root.attributes("-fullscreen", True)

menubar = Menu(root)
root.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Save", command=save)
fileMenu.add_command(label="Exit", command=lambda: root.destroy())

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Change Background", command=changebg)
editMenu.add_command(label="Change Foreground", command=changefg)

text = Text(root, font=("OCR A EXTENDED", 11), width=1920, height=2000)
text.pack(expand=True)

root.mainloop()
