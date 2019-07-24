from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from datetime import datetime
from tkinter.constants import *
import time
import serebo

root = Tk()
scheduledimage=PhotoImage("...")
note = ttk.Notebook(root, width=1000,height=460)


noteStyler = ttk.Style()
noteStyler.configure("TNotebook.Tab", background='green',foreground='red', lightcolor='orange', borderwdith=0)
noteStyler.configure("TFrame", background='cornflowerblue', foreground='green', borderwidth=0)


tab1 = ttk.Frame(note, style='TFrame')
tab2 = ttk.Frame(note, style='TFrame')
tab3 = ttk.Frame(note, style='TFrame')
tab4 = ttk.Frame(note, style='TFrame')

class File_buttons: 
    def __init__(self,master):
        master.geometry("800x500")
        fm = Frame(master, width=300)
        button1 = Button(tab2, text='Log File', command=LogFile).pack(side=LEFT, fill=X, expand=YES, padx=5, pady=5)
        button2 = Button(tab2, text='Generate Hash', command=root.destroy).pack(side=LEFT, fill=X, expand=YES, padx=5, pady=5)
        button3 = Button(tab2, text='Backup Files', command=root.destroy).pack(side=LEFT, fill=X, expand=YES, padx=5, pady=5)
        button4 = Button(tab4, text='Date Time', command=ShowDT).pack(side=LEFT, fill=X, expand=YES, padx=5, pady=5)
              
        fm.pack(fill=BOTH, expand=YES)

class LogFile(Tk):
    def __init__(self):
        super(LogFile, self).__init__()
        self.title("Log File")
        self.minsize(640,400)
        self.labelFrame = ttk.LabelFrame(self, text = "Select A File To Log")
        self.labelFrame.grid(column=4, row=10, padx=2, pady=20)
        self.button()

    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Browse A File", command = self.fileDialog)
        self.button.grid(column=1, row=1)

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir="/", filetypes=(("All Files", "*.*"), ("PDF File", "*.pdf"), ("BMP File", "*.bmp")),title="Choose a file.")
        self.label = ttk.Label(self.labelFrame, text="")
        self.label.grid(column=1, row=2)
        self.label.configure(text=self.filename)
        print(self.filename)    
       
class ShowDT(Tk):
    def __init__(self):
        super(ShowDT, self).__init__()
        self.title("Current date time")
        self.minsize(640,400)
        #self.wm_iconbitmap('icon.ico')
        self.displaytext()
                
    def displaytext(self):
        localDTS = extractDateTime(serebo.localDTS())
        self.label = ttk.Label(self, text = localDTS, font=("", 18), wraplength = 600)
        self.label.grid(column=10, row=10)
        print(localDTS)
        #self.textbox = ttk.Entry(self, width=20)
        #self.textbox.grid(column=0, row=1)


def extractDateTime(self):
    datetimestamp = datetime.strptime(self["Date Time Stamp"], '%Y:%m:%d:%H:%M:%S:%f')
    displaytime = datetimestamp.strftime("%d/%b/%Y, %H:%M:%S")
    return "Date Time: "+ displaytime
    
    

note.add(tab1, text = "Home")
note.add(tab2, text = "File")
note.add(tab3, text = "Help")
note.add(tab4, text = "Settings")
note.pack(fill=BOTH, expand=True)



#Lab = Label(root, text="SEREBO", bg="black", fg="white")
widget = Label(tab1)
widget.config(text="WELCOME TO SEREBO", font=("Stencil", 44), bg='cornflowerblue' )
widget.pack(fill=X, expand=YES)


display = File_buttons(root)
root.mainloop()