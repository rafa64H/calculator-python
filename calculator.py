import tkinter as tk


class Calculator:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("Calculator by rafa64H")

        self.result = tk.Label(self.root, text="Something", font={"arial", 18})
        self.result.pack(fill="x")

        self.entry = tk.Entry(self.root)
        self.entry.pack(fill="x", padx=10)

        self.root.mainloop()


Calculator()
