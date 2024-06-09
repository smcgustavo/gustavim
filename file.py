from tkinter import filedialog
from tkinter import *

def saveFile(textArea):
    filePath = filedialog.asksaveasfilename()
    
    if filePath != '':
        string = textArea.get("1.0", END)
        with open(filePath, "w") as f:
            f.write(string)
            f.close()
            
def openFile(textArea):
    filePath = filedialog.askopenfilename()
    
    if filePath != '':
        with open(filePath, "r") as f:
            content = f.read()
            textArea.delete("1.0", END)
            textArea.insert(INSERT, content)
            
def newFile(textArea):
    textArea.delete("1.0", END)