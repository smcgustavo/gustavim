from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import file
import json

def readJson():
    with open("config.json", "r") as j:
        return json.load(j)
        
def makeWindow(config):
    window = Tk()
    window.geometry(config['windowGeometry'])
    window.title('Gustavim')
    window.minsize(1280,720)
    return window

def makeFrame(window):
    frm = ttk.Frame(window, padding=0)
    frm.pack()
    return frm

def makeButtonsAndLabels(window, frm):
    print()
    #ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    #ttk.Button(frm, text="Quit", command=window.destroy).grid(column=1, row=0)
    
def makeMenu(window, frm, config, text):
    menubar = Menu(frm, font=(config['font'], config['fontSize']))
    fileMenu = Menu(menubar, font=(config['font'], config['fontSize'])) 
    fileMenu.add_command(label="New", command= lambda: file.newFile(text))
    fileMenu.add_command(label="Open", command= lambda: file.openFile(text))
    fileMenu.add_command(label="Save", command= lambda: file.saveFile(text))
    fileMenu.add_command(label="Quit", command= window.destroy)
    window.config(menu= menubar)
    menubar.add_cascade(label="Files",menu=fileMenu)
    
def makeText(window, config):
    text = scrolledtext.ScrolledText(
        window,                       
        wrap= None,
        font= (config['font'], config['editor']['fontSize']),
        foreground=(config['editor']['foreground']),
        background=(config['editor']['background']),
    )
    text.pack(expand= True, fill = 'both')
    return text
    
def initEditor():
    config = readJson()
    window = makeWindow(config)
    frm = makeFrame(window)
    makeButtonsAndLabels(window, frm)
    text = makeText(window,config)
    makeMenu(window, frm, config, text)
    window.mainloop()

initEditor()