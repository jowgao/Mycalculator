import tkinter as tk

class mycalculator:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("300x300")
        self.root.title("My Calulator")

        self.label = tk.Label(self.root, text="Hello DIP01", font=('Arial', 18)).pack()

        self.buttom = tk.Button(self.root, text="Click here", height=4)
        self.buttom.place(x=20, y=50)

        self.root.mainloop()

mycalculator()        