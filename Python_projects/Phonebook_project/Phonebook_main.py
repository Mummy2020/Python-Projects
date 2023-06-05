#Python ver: 3.11.2

#Author:  Sankung Saidyleigh

#Purpose:   Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
#           using Tkinter parent and child relationships.

#Tested os: This code was written and tested to work with windows 10.

from tkinter import *
import tkinter as tk
from tkinter import messagebox

#Besure to import our other modules
#so we can have access to them
import Phonebook_gui 
import Phonebook_func

#Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def _init_(self, master, *args, **kwargs):
        Frame._init_(self, master,*args, **kwargs)

        #define our master frame configuration
        self.master = master
        self.master.minsize(500,300) #(height, width)
        self.master.maxsize(500,300)
        #This CenterWindow method will center our app on the user's screen
        Phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a Tkinter built-in method to cfatch if
        # the user clicks the upper corner, "x" on windows os
        self.master.protocol("WM_DELETE_WINDOW", lambda: Phonebook_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module,
        # keeping your code compartmentalized and clutter free
        Phonebook_gui.load_gui(self)

         
        # Instantiate the Tkinter menu dropdown object
        # This is the menu that will appear at the top of our window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: Phonebook_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0) # defines the particular drop down colum and tearoff=0 means do not separate from menubar
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About This Phonebook Demo") # add_command is a child menubar item of the add_cascde parent item
        menubar.add_cascade(label="Help", menu=helpmenu) # add_cascade is a parent menubar item (visible heading)
        """
            Finally, we apply the config method of the widget to display the menu
            From here we could also pass in additional aprams for additional 
            functionalityor appearances such as a borderwidth.
        """
        self.master.config(menu=menubar, borderwidth='1')

        
"""
    It is from these few lines of code that Python will begin our gui and application
    The (if __name__ == "__main__":) part is basically telling Python that if this script
    is ran, it should start by running the code below this line....in this case we have
    instructed Python to run the following and in this order:

    root = tk.Tk()              #This Instantiates the Tk.() root frame (window) into being
    App = ParentWindow(root)    #This instantiates our own class as an App object
    root.mainloop()             #This ensures the Tkinter class object, our window, to keep looping
                                #meaning, it will stay open until we instruct it to close
"""



if __name__== "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()