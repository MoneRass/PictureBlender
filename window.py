import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import Label
from tkinter.messagebox import showinfo

from process import blend

# create the root window
root = tk.Tk()
root.title('Tkinter Open File Dialog')
root.resizable(False, False)
root.geometry('500x250')

header = Label(root, text='Picture Blending Applicatoin!!!')

base_file = ''
color_file = ''


def select_base():
    global base_file
    filetypes = (
        ('jpeg files', '*.jpg'),

    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    if filename:
        base_text.set(f'Base picture : {filename}')
        base_file = filename

   
def select_color():
    global color_file
    filetypes = (
        ('jpeg files', '*.jpg'),

    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    if filename:
        base_text.set(f'Color picture : {filename}')
        color_file = filename

def say_hello():
    header = Label(root, text='Picture Blending Applicatoin!!!')
    header.pack()

def Blend():
    blend(base_file, color_file)

# open button
base_picture_button = ttk.Button(
    root,
    text='Open a File',
    command=select_base
)

color_picture_button = ttk.Button(
    root,
    text='Open a File',
    command=select_color
)

hello_btn = ttk.Button(
    root,
    text='hello',
    command=say_hello
)

pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='indeterminate',
    length=280
)

blend_btn = ttk.Button(
    root,
    text='blend',
    command=Blend
)

base_text = tk.StringVar()
base_text.set('Base picture : ')

base_label = tk.Label(root, textvariable=base_text)

color_text = tk.StringVar()
color_text.set('Color picture : ')

color_label = tk.Label(root, textvariable=color_text)


base_label.pack()

base_picture_button.pack()

color_label.pack()

color_picture_button.pack()

blend_btn.pack()

# run the application
root.mainloop()
