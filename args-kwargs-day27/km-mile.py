from tkinter import *

def button_clicked():
    miles=input.get()
    km=float(miles)*1.60934
    mile_km_label.config(text=f"{km:.2f}")

window = Tk()
window.minsize(400,400)
window.title("Mile to Km Converter")
window.config(padx=30, pady=30)

my_label = Label(text="Miles")
my_label.grid(column=2, row=0)

new_label = Label(text="is equal to")
new_label.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

input=Entry()
input.grid(column=1, row=0)
input.config(width=14)

mile_km_label = Label(text="")
mile_km_label.grid(column=1, row=1)

button=Button(text="Calculate",command=button_clicked,width=7,height=1)
button.grid(column=1, row=2)


window.mainloop()