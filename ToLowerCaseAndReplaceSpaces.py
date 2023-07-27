from tkinter import *
 
root = Tk()
root.title("To lower case and replace whitespaces")
root.resizable(False, False)  # This code helps to disable windows from resizing
 
window_height = 400
window_width = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coordinate = int((screen_width/2) - (window_width/2))
y_coordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

def Take_input():
    INPUT = inputText.get("1.0", "end-1c")

    lowerVal = INPUT.lower()
    noSpacesVal = lowerVal.replace(" ", "-")
    
    outputText.delete('1.0', END)
    outputText.insert(END,noSpacesVal)
     
label = Label(text = "Insert your text")

inputText = Text(
    root, 
    height = 15,
    width = 70,
    bg = "#fff", 
    fg="#000"
    )
 
outputText = Text(
    root, 
    height = 8,
    width = 70,
    bg = "#e0ffff", 
    fg="#000"
    )
 
buttonSubmit = Button(
    root, 
    height = 2,
    width = 20,
    text ="Convert",
    command = Take_input
    )
 
label.pack()
inputText.pack()
buttonSubmit.pack()
outputText.pack()

mainloop()
