import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("320x420")
        self.root.resizable(False, False)

        self.expression = ""

        # Display
        self.display = tk.Entry(
            root,
            font=("Arial", 20),
            borderwidth=5,
            relief="ridge",
            justify="right"
        )
        self.display.pack(fill="both", padx=10, pady=10, ipady=10)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack()

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]

        for (text, row, col) in buttons:
            tk.Button(
                button_frame,
                text=text,
                width=6,
                height=2,
                font=("Arial", 14),
                command=lambda t=text: self.on_button_click(t)
            ).grid(row=row, column=col, padx=5, pady=5)

        # Clear button
        tk.Button(
            root,
            text="Clear",
            width=28,
            height=2,
            font=("Arial", 14),
            command=self.clear
        ).pack(pady=10)

    def on_button_click(self, char):
        if char == "=":
            try:
                result = eval(self.expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.expression = str(result)
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.expression = ""
        else:
            self.expression += char
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
