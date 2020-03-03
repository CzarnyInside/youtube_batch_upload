from tkinter import Tk
from tkinter import OptionMenu, Label, Button, GROOVE, Entry
from tkinter import StringVar
import sys
from tkinter import filedialog
from tkinter.ttk import *
from tkinter import *

    
#below is the code for "static" part of GUI
main_window_of_gui = Tk()
main_window_of_gui.title("YouTube Batch Upload")

#folder selection window

text_in_gui = Label(main_window_of_gui, text = "Please select the folder:")
text_in_gui.grid(row = 0, column = 0)

def browse_button():
    filename = filedialog.askdirectory()
    print(filename)
    return filename

button2 = Button(text="Browse...", command=browse_button).grid(row=0, column=1)

#youtube channel selection:

text_in_gui = Label(main_window_of_gui, text = "YouTube channel:")
text_in_gui.grid(row = 1, column = 0)

ip_selector_variable = StringVar()
ip_list = ["Hearthstone", "Heroes", "Overwatch", "Diablo", "StarCraft", "WoW", "Blizzard"]
ip_selector = OptionMenu(main_window_of_gui, ip_selector_variable, *ip_list)
ip_selector_variable.set(ip_list[0])
ip_selector.config(width=17)
ip_selector.grid(row = 1, column = 1)

#privacy selection:

text_in_gui = Label(main_window_of_gui, text = "Privacy:")
text_in_gui.grid(row = 2, column = 0)

privacy_variable = StringVar()
privacy_list = ["Private", "Unlisted", "Public"]
privacy = OptionMenu(main_window_of_gui, privacy_variable, *privacy_list)
privacy_variable.set(privacy_list[0])
privacy.config(width=17)
privacy.grid(row = 2, column = 1)

#usage policy selection:

text_in_gui = Label(main_window_of_gui, text = "Usage policy:")
text_in_gui.grid(row = 3, column = 0)

usage_policy_variable = StringVar()
usage_policy_list = ["Track Worldwide", "BlizzCon VT Policy", "Standard Track", "Block Worldwide", "BlizzCon 2018"]
usage_policy = OptionMenu(main_window_of_gui, usage_policy_variable, *usage_policy_list)
usage_policy_variable.set(usage_policy_list[0])
usage_policy.config(width=17)
usage_policy.grid(row = 3, column = 1)

#enable content ID:

text_in_gui = Label(main_window_of_gui, text = "Enable content ID:")
text_in_gui.grid(row = 4, column = 0)

enable_content_id_variable = StringVar()
enable_content_id_list = ["Yes", "No"]
enable_content_id = OptionMenu(main_window_of_gui, enable_content_id_variable, *enable_content_id_list)
enable_content_id_variable.set(enable_content_id_list[0])
enable_content_id.config(width=17)
enable_content_id.grid(row = 4, column = 1)

#match policy:

text_in_gui = Label(main_window_of_gui, text = "Match policy:")
text_in_gui.grid(row = 5, column = 0)

match_policy_id_variable = StringVar()
match_policy_id_list = ["Track Worldwide", "BlizzCon VT Policy", "Standard Track", "Block Worldwide", "BlizzCon 2018"]
match_policy_id = OptionMenu(main_window_of_gui, match_policy_id_variable, *match_policy_id_list)
match_policy_id_variable.set(match_policy_id_list[0])
match_policy_id.config(width=17)
match_policy_id.grid(row = 5, column = 1)

#notify subscribers:

text_in_gui = Label(main_window_of_gui, text = "Notify subscribers:")
text_in_gui.grid(row = 6, column = 0)

notify_subscribers_id_variable = StringVar()
notify_subscribers_id_list = ["Yes", "No"]
notify_subscribers_id = OptionMenu(main_window_of_gui, notify_subscribers_id_variable, *notify_subscribers_id_list)
notify_subscribers_id_variable.set(notify_subscribers_id_list[0])
notify_subscribers_id.config(width=17)
notify_subscribers_id.grid(row = 6, column = 1)

#text box
text_box = Listbox(main_window_of_gui, height=5)
text_box.grid(column=0, row=9, columnspan=2, sticky=(N,W,E,S))  # columnspan − How many columns widgetoccupies; default 1.
main_window_of_gui.grid_columnconfigure(0, weight=1)
main_window_of_gui.grid_rowconfigure(9, weight=1)

#scroll bar
my_scrollbar = ttk.Scrollbar(main_window_of_gui, orient=VERTICAL, command=text_box.yview)
my_scrollbar.grid(column=2, row=9, sticky=(N,S))
#attaching scroll bar to text box
text_box['yscrollcommand'] = my_scrollbar.set

#inserting the text
def insert_log(text):
    text_box.insert('end', text)


progress=Progressbar(main_window_of_gui,orient=HORIZONTAL, mode='determinate')
progress.grid(row=10, column=0, columnspan=3, sticky=(W,E))

videos = ["a","b","c","d","e","f","g"]

def bar():
    import time

    for i, value in enumerate(videos):
        insert_log("working on "+ str(value))
        time.sleep(2) # simulate work done
        update_progressbar(progress, i+1, len(videos))

def update_progressbar(progressbar, current_value, total_values):
    progress['value']= current_value / total_values * 100
    main_window_of_gui.update_idletasks()
    
#generate button:

def placeholder_function():
    print("File generated!")

text_in_gui = Label(main_window_of_gui, text="")
text_in_gui.grid(row=8, column=0)

button3 = Button(text="Generate the file!", command=bar).grid(row=8, column=1)

empty_line = Label(main_window_of_gui, text="")
text_in_gui.grid(row=7, column=1)

mainloop()

#start the main window of GUI
main_window_of_gui.mainloop()