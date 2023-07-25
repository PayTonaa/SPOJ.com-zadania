import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        self.display = tk.Entry(self.master, width=25,
                                justify="right", font=("Arial", 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)

        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)

        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)

        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("C", 4, 2)
        self.create_button("+", 4, 3)

        self.create_button("=", 5, 0, columnspan=4)

        self.expression = ""

    def create_button(self, text, row, col, rowspan=1, columnspan=1):
        button = tk.Button(self.master, text=text, width=5, height=2, font=("Arial", 14),
                           command=lambda: self.button_click(text))
        button.grid(row=row, column=col, rowspan=rowspan,
                    columnspan=columnspan, padx=5, pady=5)

    def button_click(self, text):
        if text == "C":
            self.expression = ""
            self.display.delete(0, tk.END)
        elif text == "=":
            result = str(eval(self.expression))
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
            self.expression = result
        else:
            self.expression += text
            self.display.insert(tk.END, text)


root = tk.Tk()
calc = Calculator(root)
root.mainloop()
