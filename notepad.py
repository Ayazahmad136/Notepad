from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def newfile():
    root.title("Untitled - Notepad")
    file = None
    textarea.delete(1.0, END)

def savefile():
    global file
    if file == None:
        # save as new file
        file = asksaveasfilename(initialfile='Untitled.txt',
                                 defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])

        if file == "":
            file = None
        else:

            # try to save the file
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()
            # change the window title
            root.title(os.path.basename(file) + " - Notepad")



    else:
        file = open(file, "w")
        file.write(textarea.get(1.0, END))
        file.close()
def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])

    if file == "":

        # no file to open
        file = None
    else:
        # try to open the file
        # set the window title
        root.title(os.path.basename(file) + " - Notepad")
        textarea.delete(1.0, END)

        file = open(file, "r")

        textarea.insert(1.0, file.read())

        file.close()


def savefile():
    global file
    if file == None:
        # save as new file
        file = asksaveasfilename(initialfile='Untitled.txt',
                                 defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])

        if file == "":
            file = None
        else:

            # try to save the file
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()
            # change the window title
            root.title(os.path.basename(file) + " - Notepad")



    else:
        file = open(file, "w")
        file.write(textarea.get(1.0, END))
        file.close()
def exitfile():
    root.destroy()

def cutfile():
    textarea.event_generate(("<<Cut>>"))
def copyfile():
    textarea.event_generate(("<<Copy>>"))
def pastefile():
    textarea.event_generate(("<<Paste>>"))


def help():
    showinfo("Notepad", "This Notepad Is Made By Ayaz")


root=Tk()
if __name__ =='__main__':
   root.title("Untitled-Notepad")
   root.geometry("734x434")
   textarea= Text(root, font="lucida 13")
   file=None
   textarea.pack(expand=100,fill='both')

   mainmenu=Menu(root)
   submenu= Menu(mainmenu,tearoff=0)
   submenu.add_command(label='New ',command=newfile)
   submenu.add_command(label='Save',command=savefile)
   submenu.add_command(label='Open',command=openfile)
   submenu.add_separator()
   submenu.add_command(label='Exit',command=exitfile)
   mainmenu.add_cascade(label='File',menu=submenu)
   root.config(menu=mainmenu)

   submenu = Menu(mainmenu, tearoff=0)
   submenu.add_command(label='Cut', command=cutfile)
   submenu.add_command(label='Copy', command=copyfile)
   submenu.add_command(label='Paste', command=pastefile)

   mainmenu.add_cascade(label='Edit', menu=submenu)
   root.config(menu=mainmenu)

   submenu = Menu(mainmenu, tearoff=0)
   submenu.add_command(label='help', command=help)
   mainmenu.add_cascade(label='About', menu=submenu)
   root.config(menu=mainmenu)

   scroll=Scrollbar(textarea)
   scroll.pack(side=RIGHT,fill=Y)
   scroll.config(command=textarea.yview)
   textarea.config(yscrollcommand=scroll.set)

   root.mainloop()

