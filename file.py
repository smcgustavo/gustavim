from tkinter import filedialog
from tkinter import *
import json

def readJson():
    with open("config.json", "r") as j:
        return json.load(j)

def applyColors(textArea):
    config = readJson()
    for tag in textArea.tag_names():
        textArea.tag_remove(tag, "1.0", END)
    keywords = [
        "def ", "class ", "import ", "if ", "else ",
        "as ", "in ", "while ", "for ", "from ", " return "
    ]
    for word in keywords:
        startIDX = "1.0"
        while True:
            startIDX = textArea.search(word, startIDX, nocase=True, stopindex=END)
            if not startIDX:
                break
            endIDX = f"{startIDX}+{len(word)}c"
            textArea.tag_add(word, startIDX, endIDX)
            textArea.tag_config(word, foreground= config['editor']['highlight'])
            startIDX = endIDX

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
            applyColors(textArea)

def newFile(textArea):
    textArea.delete("1.0", END)
    textArea.bind("<KeyRelease>", lambda event: applyColors(textArea))