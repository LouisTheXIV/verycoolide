
import tkinter
import platform
import os    
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

# Reminder that 2.0 is going to be a Alpha Build
NotepadVer = "VeryCoolIDE Alpha 2.0"
WindowsVer = platform.platform()
class Notepad:
    __root = Tk()
    
    def add_terminal(self, terminal):
        self.terminal = terminal
  
    # default window width and height
    __thisWidth = 1200
    __thisHeight = 1200
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisRunMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
      
    # To add scrollbar
    __thisScrollBar = Scrollbar(__thisTextArea)     
    __file = None
  
    def __init__(self,**kwargs):
  
        # Set icon
        try:
            self.__root.wm_iconbitmap("Notepad.ico") 
        except:
            pass
  
        # Set window size (the default is 300x300)
  
        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass
  
        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass
  
        # Set the window text
        self.__root.title("Untitled - VeryCoolIDE")
  
        # Center the window
        screenWidth = 1200 #self.__root.winfo_screenwidth()
        screenHeight = 1200 #self.__root.winfo_screenheight()
      
        # For left-alling
        left = (screenWidth / 2) - (self.__thisWidth / 2) 
          
        # For right-allign
        top = (screenHeight / 2) - (self.__thisHeight /2) 
          
        # For top and bottom
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
                                              self.__thisHeight,
                                              left, top)) 
  
        # To make the textarea auto resizable
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)
  
        # Add controls (widget)
        self.__thisTextArea.grid(sticky = N + E + S + W)
          
        # To open new file
        self.__thisFileMenu.add_command(label="New",
                                        command=self.__newFile)    
          
        # To open a already existing file
        self.__thisFileMenu.add_command(label="Open",
                                        command=self.__openFile)
          
        # To save current file
        self.__thisFileMenu.add_command(label="Save",
                                        command=self.__saveFile)    
  
        # To create a line in the dialog        
        self.__thisFileMenu.add_separator()                                         
        self.__thisFileMenu.add_command(label="Exit",
                                        command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File",
                                       menu=self.__thisFileMenu)     
          
        # To give a feature of cut 
        self.__thisEditMenu.add_command(label="Cut",
                                        command=self.__cut)   
        # Settings main button        
      
        # to give a feature of copy    
        self.__thisEditMenu.add_command(label="Copy",
                                        command=self.__copy)         
          
        # To give a feature of paste
        self.__thisEditMenu.add_command(label="Paste",
                                        command=self.__paste)         
          
        # To give a feature of editing
        self.__thisMenuBar.add_cascade(label="Edit",
                                       menu=self.__thisEditMenu)  

        # To give a feature of running the script
        self.__thisRunMenu.add_command(label="Run",
                                        command=self.__coderun)  
        
        # To give a feature of running & debugging
        self.__thisMenuBar.add_cascade(label="Run",
                                       menu=self.__thisRunMenu)  
          
        # To create a feature of description of the notepad
        self.__thisHelpMenu.add_command(label="About VeryCoolIDE",
                                        command=self.__showAbout) 
        self.__thisMenuBar.add_cascade(label="Help",
                                       menu=self.__thisHelpMenu)
  
        self.__root.config(menu=self.__thisMenuBar)
  
        self.__thisScrollBar.pack(side=RIGHT,fill=Y)                    
          
        # Scrollbar will adjust automatically according to the content        
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)     
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
      
          
    def __quitApplication(self):
        self.__root.destroy()
        # exit()
  
    def __showAbout(self):
        showinfo("VeryCoolIDE - IDE Version",NotepadVer)
        showinfo("VeryCoolIDE - Windows Version",WindowsVer)
  
    def __openFile(self):
          
        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files","*.*"),
                                        ("Text Documents","*.txt")])
  
        if self.__file == "":
              
            # no file to open
            self.__file = None
        else:
              
            # Try to open the file
            # set the window title
            self.__root.title(os.path.basename(self.__file) + " - VeryCoolIDE")
            self.__thisTextArea.delete(1.0,END)
  
            file = open(self.__file,"r")
  
            self.__thisTextArea.insert(1.0,file.read())
  
            file.close()
  
          
    def __newFile(self):
        self.__root.title("Untitled - VeryCoolIDE")
        self.__file = None
        self.__thisTextArea.delete(1.0,END)
  
    def __saveFile(self):
  
        if self.__file == None:
            # Save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files","*.*"),
                                                ("Text Documents","*.txt")])
  
            if self.__file == "":
                self.__file = None
            else:
                  
                # Try to save the file
                file = open(self.__file,"w")
                file.write(self.__thisTextArea.get(1.0,END))
                file.close()
                  
                # Change the window title
                self.__root.title(os.path.basename(self.__file) + " - VeryCoolIDE")
                  
              
        else:
            file = open(self.__file,"w")
            file.write(self.__thisTextArea.get(1.0,END))
            file.close()
  
    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")
  
    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")
  
    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def __coderun(self, *args):
        if self.__file is not None:
            dir_cmd = "cd {0}".format(os.path.dirname(self.__file))
            build_cmd = "python {1}".format(os.getcwd(), self.__file)
            print("{0} && {1}".format(dir_cmd, build_cmd))
            # terminal.automation("{0} && {1}".format(dir_cmd, build_cmd))
            os.system("{0} && {1}".format(dir_cmd, build_cmd))


  
    def run(self):

        # Run main application
        self.__root.mainloop()
        print(NotepadVer)


  
  
  
  
# Run main application
notepad = Notepad(width=2000,height=1000)
notepad.run()