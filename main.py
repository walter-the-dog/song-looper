import tkinter
from tkinter import filedialog
from tkinter import messagebox
import os
import time
import tinytag
def doLoop(times,file):
    try:
        OpenedFile = open(file,"rb")
        text = OpenedFile.read()*int(times)
        OpenedFile.close()
        OpenedFile = open(file,"wb+")
        OpenedFile.write(text)
        OpenedFile.close()
    except Exception as e:
        messagebox.showerror("Error","Unexpected error occured\nTraceback \\/\n"+str(e))
        return
    messagebox.showinfo("Success",f"Song successfully looped {times} times!")
root = tkinter.Tk()
tkinter.Label(root,text="MP3 looper").grid(column=1,row=0)
dataFrame = tkinter.Frame(root)
dataFrame.grid(column=1,row=1)
tkinter.Label(dataFrame,text="Choose MP3 file").grid(column=0,row=0)
selectedFile = ""
def ChooseFile():
    global selectedFile
    selectedFile = filedialog.askopenfilename(initialdir="/")
    if selectedFile == "":
        ChooseButton.config(text="Choose..")
    elif selectedFile[-3:] not in ["mp3","MP3"]:
        messagebox.showerror("Error","File type invalid! Must be a MP3. Use y2mate to convert youtube videos to mp3.")
        selectedFile = ""
        ChooseButton.config(text="Choose..")
        LoopEntry['state'] = tkinter.DISABLED
    else:
        ChooseButton.config(text=os.path.basename(selectedFile))
        LoopEntry['state'] = tkinter.NORMAL
ChooseButton = tkinter.Button(dataFrame,text="Choose..",command=ChooseFile)
ChooseButton.grid(column=1,row=0)
tkinter.Label(dataFrame,text="Loop times:").grid(column=0,row=2)
def FileLengthEstimator(a,b,c):
    if selectedFile == "":
        LengthLabel['text'] = "Estimated File Length After Loop:N\\A"
        return
    try:
        loops = int(LoopEntry.get())
    except:
        LengthLabel['text'] = "Estimated File Length After Loop:N\\A"
        return
    length = tinytag.TinyTag.get(selectedFile).duration
    total = length*loops
    try:
        temp = time.gmtime(total)
    except:
        LengthLabel['text'] = "Estimated File Length After Loop:N\\A"
        return
    if total > 86400:
        LengthLabel['text'] = "Estimated File Length After Loop:N\\A"
        return
    LengthLabel['text'] = "Estimated File Length After Loop:"+time.strftime("%H:%M:%S",temp)
textvar = tkinter.StringVar()
LoopEntry = tkinter.Entry(dataFrame,textvariable=textvar,state=tkinter.DISABLED)
textvar.trace('w',FileLengthEstimator)
LoopEntry.grid(column=1,row=2)
def BBI():
    if selectedFile == "":
        messagebox.showerror("Error","No valid file selected")
        return
    try:
        if int(LoopEntry.get())<=1:
            messagebox.showerror("Error","You have to loop it more than once")
            LoopEntry.delete(0,tkinter.END)
            return
        if LengthLabel['text'] == "Estimated File Length After Loop:N\\A":
            messagebox.showerror("Error","Reenter a valid loop value. (It could also be that the estimated file length is larger than 24 hours)")
            return
    except:
        messagebox.showerror("Error","Please provide a number for loop times. ")
        LoopEntry.delete(0,tkinter.END)
        return
    doLoop(int(LoopEntry.get()),selectedFile)
LengthLabel = tkinter.Label(root,text="Estimated File Length After Loop:N\\A")
LengthLabel.grid(column=1,row=4)
tkinter.Button(root,text="Begin..",command=BBI).grid(column=1,row=3)
root.mainloop()