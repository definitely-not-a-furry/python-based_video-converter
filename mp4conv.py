title = """
Pyconverter version 0.1
**THIS IS A BETA AND NOT COMPLETELY STABLE, USE AT YOUR OWN RISK
Make sure ffmpeg is installed correctly
Github: https://github.com/definitely-not-a-furry/python_based-mp4-converter"""

from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter.filedialog import askopenfilenames
import os

filenames = None

root = Tk()
root.attributes('-toolwindow',True)
root.resizable(False,False)
root.title('Convert video file to mp4')

filel = Text(root, width=60,height=5, wrap="none", font=("consolas",12), state=DISABLED)
filel.grid(row=1,columnspan=2)

def selectfiles():
    global filenames, filedisplay
    filel["state"] = NORMAL
    filenames = askopenfilenames()
    for x in filenames:
        filedisplay = '\n'.join(filenames)
    filel.delete(1.0, END)
    filel.insert(END, filedisplay)
    filel["state"] = DISABLED

Button(root, text='Select',command=lambda : selectfiles()).grid(column=1,row=3,sticky=N+E+S+W,rowspan=2)
Button(root, text='Done', command=lambda : root.destroy()).grid(column=0,row=3,sticky=N+E+S+W,rowspan=2)
Label(root,text='Select the files you want to convert by pressing "Select". The selected files will appear above.\nThis process can take some time, depending on the duration and resolution of these files. \nFiles will be processed and converted consecutively').grid(column=0,row=2,columnspan=2,sticky=W)
root.mainloop()

print(f'Converting: {filenames}')


if not filenames == None:
    showinfo('Notice','The convertion process will continue in a terminal window')
    try:
        for i in range(len(filenames)):
            print(f'Iteration {i+1}')
            os.system(f'ffmpeg -i "{filenames[i]}" "{filenames[i]}.mp4"')
    except:
        showerror('Error','FFmpeg is not installed correctly')
else:
    showerror('Notice','Please select the files you want to convert by pressing "Select"')