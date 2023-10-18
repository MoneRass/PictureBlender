import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import Label
from tkinter.messagebox import showinfo

from PIL import Image
import PIL

from process import blend
from resize import resize_and_save

# create the root window
root = tk.Tk()
root.title('Picture B;ender Application')
root.resizable(False, False)
root.geometry('500x250')

header = Label(root, text='Picture Blending Applicatoin!!!')

base_file = ''
color_file = ''

def save_file():
    im = Image.open(r'img\temp.jpg')
    im = im.save('res.jpg')

def select_base():
    global base_file
    filetypes = (
        ('jpeg files', '*.jpg'),

    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='D:/PictureBlender/img',
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
        initialdir='D:/PictureBlender/img',
        filetypes=filetypes)
    if filename:
        color_text.set(f'Color picture : {filename}')
        color_file = filename

def start():
    global color_file
    global base_file

    inp_size = inputtxt.get(1.0, "end-1c")
    
    if color_file != '':

        blend(base_file, color_file)

        if inp_size != '':
            base_file = base_file.split('/')
            color_file = color_file.split('/')
            blended_file = "blended_img/blended_"+base_file[-1][:-4]+'_'+color_file[-1]
            print(blended_file)
            resize_and_save(blended_file, int(inp_size))

    elif color_file == '' and inp_size!='':
        resize_and_save(base_file, int(inp_size))

    else:
        print('Please select base picture')
    
    


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

blend_btn = ttk.Button(
    root,
    text='blend',
    command=start
    
)

# TextBox Creation 
inputtxt = tk.Text(root, 
                   height = 1, 
                   width = 5) 

base_text = tk.StringVar()
base_text.set('Base picture : ')

base_label = tk.Label(root, textvariable=base_text)

color_text = tk.StringVar()
color_text.set('Color picture : ')

color_label = tk.Label(root, textvariable=color_text)


scale_text = tk.StringVar()
scale_text.set('Set scale (%) : ')

scale_label = tk.Label(root, textvariable=scale_text)



base_label.pack()

base_picture_button.pack()

color_label.pack()

color_picture_button.pack()

scale_label.pack()
inputtxt.pack()

blend_btn.pack()

# run the application
root.mainloop()
