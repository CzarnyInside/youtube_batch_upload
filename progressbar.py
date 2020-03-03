from tkinter import *
from tkinter.ttk import *

tk=Tk()
progress=Progressbar(tk,orient=HORIZONTAL,length=100,mode='determinate')

videos = ["a","b","c","d","e","f","g"]

def bar():
    import time

    for i, value in enumerate(videos):
        print("working on", value)
        time.sleep(2) # simulate work done
        update_progressbar(progress, i+1, len(videos))

    #Finished !!!


def update_progressbar(progressbar, current_value, total_values):
    progress['value']= current_value / total_values * 100
    tk.update_idletasks()
    

progress.pack()
Button(tk,text='foo',command=bar).pack()
mainloop()