from tkinter import *

window = Tk()
window.geometry('650x550')
window.attributes('-fullscreen', True)

# label Title
label = Label(text="Local Library", font=('Times New Roman bold', 20), background="#34A2FE")
label.pack(padx=10, pady=10)

# Create a Button
btn = Button(window, text='Click me !', bd='5',
             command=window.destroy)
# Set the position of button on the top of window.
btn.pack(side='top')


window.mainloop()
