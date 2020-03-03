from tkinter import *
from tkinter import ttk

root = Tk()

#text box
text_box = Listbox(root, height=5)
text_box.grid(column=0, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
#scroll bar
my_scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=text_box.yview)
my_scrollbar.grid(column=1, row=0, sticky=(N,S))
#attaching scroll bar to text box
text_box['yscrollcommand'] = my_scrollbar.set

#inserting the text
for i in range(1,1001):
    text_box.insert('end', 'Line %d of 1000' % (i))
    # wait half a second

p = ttk.Progressbar(root, orient=HORIZONTAL, length=200, mode='determinate')

root.mainloop()
