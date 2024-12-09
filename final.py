from tkinter import *

window =Tk()
window.minsize(width=100, height=100)
window.title("Calculator")
window.config(pady=25)

def convert():
    user_input=input1.get()
    km = round(float(user_input) * 1.60934, 2)
    result.config(text=km)
    return 

input1 = StringVar()
entry = Entry(window, textvariable=input1, width=15)
entry.grid(column=1, row=0)

label1 = Label(text="Miles is equal to")
label1.grid(column=2, row=0)
label2 =Label(text="is equal to")
label2.grid(column=0, row=1)

result = Label(text=f"")
result.grid(column=1, row=1)
result_km = Label(text="KM")
result_km.grid(column=2, row=1)
button = Button(text= "Click", command=convert, width=12)
button.grid(column=1, row=2)

















window.mainloop()






