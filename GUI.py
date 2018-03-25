# from tkinter import * 

# class Window(Frame):

#     def __init__(self, master=None):
#         Frame.__init__(self,master)
#         self.master = master
        
# root = Tk()
# root.geometry("400x300")
# app = Window(root)
# root.mainloop()

from tkinter import Tk, Label, Button, scrolledtext

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):

root = Tk()
root.geometry("700x300")
my_gui = MyFirstGUI(root)
root.mainloop()