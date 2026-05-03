import tkinter as tk
def update_display(value):
   current = display_var.get()
   display_var.set(value if current == "0" else current + value)
def clear_display():
   display_var.set("0")
def calculate_result():
   try:
       result = eval(display_var.get())
       display_var.set(str(result))
   except:
       display_var.set("Error")
root = tk.Tk()
root.title("Simple Calculator")
display_var = tk.StringVar(value="0")
tk.Label(root, textvariable=display_var, font=("Arial", 24), bg="lightgray", anchor="e", padx=10).grid(row=0, column=0, columnspan=4)
buttons = [
   ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
   ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
   ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
   ("0",4,0),(".",4,1),("=",4,2),("+",4,3)
]
for (text,r,c) in buttons:
   cmd = lambda t=text: update_display(t) if t != "=" else calculate_result()
   tk.Button(root, text=text, font=("Arial",18), command=cmd).grid(row=r, column=c)
tk.Button(root, text="C", font=("Arial",18), command=clear_display).grid(row=5, column=0, columnspan=4)
root.mainloop()
