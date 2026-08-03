#IMPORTING MODULES
import tkinter as tk

#CREATING GUI 
root = tk.Tk()
root.title("Python Calculator")

#CALCULATOR DISPLAY
display_var = tk.StringVar(value="0")
display = tk.Label(root, textvariable=display_var, anchor="e", font=("Arial", 18, "bold"), bg="#D3D3D3", fg="black", relief="sunken", padx=8)
display.pack(fill="x", pady=(10, 8), padx=8)

#Creating a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(padx=6, pady=(0, 10), fill="x")

#CALCULATOR BUTTONS
buttons = [
    ["C", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", "⌫"],
]

#BUTTON CLICK EVENT HANDLER FUNCTION
def on_button_click(value):
    current = display_var.get()
#FOR CLEAR BUTTON
    if value == "C":
        display_var.set("0")
        return
#FOR BACKSPACE BUTTON
    if value == "⌫":
        if current == "Error" or len(current) <= 1:
            display_var.set("0")
        else:
            display_var.set(current[:-1])
        return
#FOR EQUAL BUTTON
    if value == "=":
        try:
            result = str(eval(current))    #TO EVALUATE THE EXPRESSION
        except Exception:
            result = "Error"
        display_var.set(result)
        return
#FOR HANDLING THE INPUT OF NUMBERS AND OPERATORS
    if current == "Error" and value.isdigit():
        display_var.set(value)
        return
#FOR HANDLING THE INPUT OF OPERATORS
    operators = "+-*/"
    if value in operators:
        if current == "0" or current[-1] in operators:
            return

    if current == "0":
        display_var.set(value)
    else:
        display_var.set(current + value)

#CALCULATOR BUTTONS CREATION
for row_index, row_buttons in enumerate(buttons):     #CALCULATOR BUTTONS ROWS
    for col_index, label in enumerate(row_buttons):   #CALCULATOR BUTTONS COLUMNS
#Setting button background color based on the label
        btn_bg = "#FFFFFF"
        if label == "C":
            btn_bg = "#FF0000"
        elif label == "=":
            btn_bg = "#FFA500"
        btn = tk.Button(button_frame, text=label, width=6, height=2, font=("Arial", 16), bg=btn_bg, command=lambda v=label: on_button_click(v))
        btn.grid(row=row_index, column=col_index, padx=5, pady=5)

#WINDOW SIZE AND POSITIONING
root.update_idletasks()
root.minsize(root.winfo_width(), root.winfo_height())
root.maxsize(root.winfo_width(), root.winfo_height())
root.eval('tk::PlaceWindow . center')

root.mainloop()
