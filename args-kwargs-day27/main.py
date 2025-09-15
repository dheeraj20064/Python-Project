from tkinter import *
window = Tk()
window.title("My first GUI program")
window.minsize(500, 300)
window.config(padx=20, pady=20)

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

my_label = Label(text="Hello World",font=("Arial",20,"bold"))
my_label["text"] = "Hello World"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

button=Button(text="Click me",command=button_clicked)
button.grid(row=1,column=1 )

new_button=Button(text="New Button",command=button_clicked)
new_button.grid(row=2,column=0 )

input=Entry(width=10)
input.grid(row=3 ,column=2 )



window.mainloop()
