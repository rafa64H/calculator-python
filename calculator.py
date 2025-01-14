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

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)
        self.buttonframe.columnconfigure(3, weight=1)

        self.btn0 = tk.Button(self.buttonframe, text="0", font={"arial", 16})
        self.btn0.grid(row=4, column=0, columnspan=2, sticky=tk.W + tk.E)

        self.btn1 = tk.Button(self.buttonframe, text="1", font={"arial", 16})
        self.btn1.grid(row=3, column=0, sticky=tk.W + tk.E)

        self.btn2 = tk.Button(self.buttonframe, text="2", font={"arial", 16})
        self.btn2.grid(row=3, column=1, sticky=tk.W + tk.E)

        self.btn3 = tk.Button(self.buttonframe, text="3", font={"arial", 16})
        self.btn3.grid(row=3, column=2, sticky=tk.W + tk.E)

        self.btn4 = tk.Button(self.buttonframe, text="4", font={"arial", 16})
        self.btn4.grid(row=2, column=0, sticky=tk.W + tk.E)

        self.btn5 = tk.Button(self.buttonframe, text="5", font={"arial", 16})
        self.btn5.grid(row=2, column=1, sticky=tk.W + tk.E)

        self.btn6 = tk.Button(self.buttonframe, text="6", font={"arial", 16})
        self.btn6.grid(row=2, column=2, sticky=tk.W + tk.E)

        self.btn7 = tk.Button(self.buttonframe, text="7", font={"arial", 16})
        self.btn7.grid(row=1, column=0, sticky=tk.W + tk.E)

        self.btn8 = tk.Button(self.buttonframe, text="8", font={"arial", 16})
        self.btn8.grid(row=1, column=1, sticky=tk.W + tk.E)

        self.btn9 = tk.Button(self.buttonframe, text="9", font={"arial", 16})
        self.btn9.grid(row=1, column=2, sticky=tk.W + tk.E)

        self.btndot = tk.Button(self.buttonframe, text=".", font={"arial", 16})
        self.btndot.grid(row=4, column=2, sticky=tk.W + tk.E)

        self.btnSubstract = tk.Button(self.buttonframe, text="-", font={"arial", 16})
        self.btnSubstract.grid(row=1, column=3, sticky=tk.W + tk.E)

        self.btnPlus = tk.Button(self.buttonframe, text="+", font={"arial", 16})
        self.btnPlus.grid(row=0, column=3, sticky=tk.W + tk.E)

        self.btnDivide = tk.Button(self.buttonframe, text="/", font={"arial", 16})
        self.btnDivide.grid(row=0, column=2, sticky=tk.W + tk.E)

        self.btnMultiply = tk.Button(self.buttonframe, text="*", font={"arial", 16})
        self.btnMultiply.grid(row=0, column=1, sticky=tk.W + tk.E)

        self.equal = tk.Button(self.buttonframe, text="=", font={"arial", 16})
        self.equal.grid(row=2, column=3, rowspan=3, sticky=tk.W + tk.E + tk.N + tk.S)

        self.buttonframe.pack(fill="x")

        self.root.mainloop()


Calculator()
