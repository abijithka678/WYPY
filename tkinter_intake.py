'''
IT IS WORK ON GUI USING TKINTER AND HAD TAKE AN INPUT FROM USER
CONTAINS
TEXTBOX
LABEL
BUTTON
WHEN WE CLICK THE BUTTON IT GET THE VALUE ENTERED IN THE TEXTBOX
'''
import tkinter as tk
window = tk.Tk()
window.geometry("250x250")
def show():
    print('hello')
    val = text.get()
    print(val)

#Setting Frame inside the window
button_frame = tk.Frame(window)


button_frame.columnconfigure(0,weight =1)
button_frame.columnconfigure(1,weight = 1)

label = tk.Label(button_frame, text='Name')
label.grid(row = 0, column =0)
text = tk.Entry(button_frame)
text.grid(row = 0, column = 1)
button_one = tk.Button(button_frame,text = 'Convert',activebackground = 'grey',command = show)
button_one.grid(row = 1,column = 1,sticky = tk.W+tk.E)

button_frame.pack(fill='x')




window.mainloop()
