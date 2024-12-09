# GUI Tkinter
# Positional Arguments(requaired and optional) in the example of tutrle.write() function
# Unlimited Positional Arguments function(*args) 
    # *agr is tuple data type
    # *arg[0] items in the tuple args can be accessed with index number 
# Unlimited Keyword Arguments function(**kwargs)
    # **kwargs data type is dictionary, you can have all the methods of dictionary with kwargs
    # **kwargs[key_name] including accessing the items
    # get() method is used in creating a class with kwargs so that when the key is not spacified it returns "None"
    # and doesn't crash    
import tkinter

#main class -> object asignment
window = tkinter.Tk()
window.title("My Very First GUI Program")
window.minsize(width=500, height=300)
#you can give padding
window.config(padx=100, pady=250)


#Label
#create an object with Label info
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
#Display the label with pack() function
# documentation - https://www.tcl.tk/man/tcl8.6/TkCmd/contents.htm
#my_label.pack()
my_label.grid(column=0, row=0)

#Function for clicked button
def clicked_button():
    user_input=input.get()
    my_label["text"] = user_input

#Button

button = tkinter.Button(text="Click me", command=clicked_button, background="light green")
# To show anyting on the screen, it should be packe dor parced
#button.pack()
button.grid(column=1, row=1)


new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)
#Entery - Input from the user

input = tkinter.Entry(width=25) #modifying input area
#input.pack()
input.grid(column=3, row=2)





































#always keep it down
#main window keeps the window open and keeps listening to the instruction
window.mainloop()



