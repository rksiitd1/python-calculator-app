import tkinter as tk
import ttkbootstrap as ttkb

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Beautiful Calculator")
        master.geometry("300x400")
        master.resizable(False, False)

        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Result display
        result_entry = ttkb.Entry(self.master, textvariable=self.result_var, justify="right", font=("Arial", 24))
        result_entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

        # Button layout
        button_layout = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', 'C', '+'),
            ('=',)
        ]

        # Create buttons
        for i, row in enumerate(button_layout):
            for j, button_text in enumerate(row):
                button = ttkb.Button(self.master, text=button_text, command=lambda x=button_text: self.button_click(x))
                button.grid(row=i+1, column=j, padx=2, pady=2, sticky="nsew")

        # Configure grid weights
        for i in range(5):
            self.master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)

    def button_click(self, key):
        if key == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        elif key == 'C':
            self.result_var.set("")
        else:
            current = self.result_var.get()
            self.result_var.set(current + key)

if __name__ == "__main__":
    root = ttkb.Window(themename="darkly")
    calculator = Calculator(root)
    root.mainloop()