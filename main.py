#importing web browser module
import webbrowser
#importing tkinter
from tkinter import *
#creating root
root = Tk()
#setting a GUI title
root.title("webBrowser")
#setting GUI geometry
root.geometry("300*200")
#function to open copyassignmet.com in browser
def copyassignment():
    webbrowser.open("www.copyassignment.com")
    #function to open google in browser
def google():
    webbrowser.open("www.google.com")
#function to call copyassignment function
copyassignment = Button(root,text="visit copyassignment",command = copyassignment).pack(pady=20)
#button to call google function
mygoogle = Button(root, text="open Google",command=google).pack(pady=20)
root.mainloop()