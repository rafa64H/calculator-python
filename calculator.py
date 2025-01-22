import tkinter as tk
import re


class Calculator:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("Calculator by rafa64H")

        self.result = tk.Label(self.root, text="0", font={"arial", 18})
        self.result.pack(fill="x")

        self.validation_command = (self.root.register(self.validate_input), "%S", "%d")

        self.entry = tk.Entry(
            self.root, validate="key", validatecommand=self.validation_command
        )
        self.entry.bind("<Control-a>", self.select_all)
        self.entry.bind("<Control-A>", self.select_all)
        self.entry.pack(fill="x", padx=10)

        self.root.bind("<KeyPress>", self.input_entry_not_focused)

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)
        self.buttonframe.columnconfigure(3, weight=1)

        self.btn0 = tk.Button(
            self.buttonframe,
            text="0",
            font={"arial", 16},
            command=lambda: self.button_click("0"),
        )
        self.btn0.grid(row=4, column=0, columnspan=2, sticky=tk.W + tk.E)

        self.btn1 = tk.Button(
            self.buttonframe,
            text="1",
            font={"arial", 16},
            command=lambda: self.button_click("1"),
        )
        self.btn1.grid(row=3, column=0, sticky=tk.W + tk.E)

        self.btn2 = tk.Button(
            self.buttonframe,
            text="2",
            font={"arial", 16},
            command=lambda: self.button_click("2"),
        )
        self.btn2.grid(row=3, column=1, sticky=tk.W + tk.E)

        self.btn3 = tk.Button(
            self.buttonframe,
            text="3",
            font={"arial", 16},
            command=lambda: self.button_click("3"),
        )
        self.btn3.grid(row=3, column=2, sticky=tk.W + tk.E)

        self.btn4 = tk.Button(
            self.buttonframe,
            text="4",
            font={"arial", 16},
            command=lambda: self.button_click("4"),
        )
        self.btn4.grid(row=2, column=0, sticky=tk.W + tk.E)

        self.btn5 = tk.Button(
            self.buttonframe,
            text="5",
            font={"arial", 16},
            command=lambda: self.button_click("5"),
        )
        self.btn5.grid(row=2, column=1, sticky=tk.W + tk.E)

        self.btn6 = tk.Button(
            self.buttonframe,
            text="6",
            font={"arial", 16},
            command=lambda: self.button_click("6"),
        )
        self.btn6.grid(row=2, column=2, sticky=tk.W + tk.E)

        self.btn7 = tk.Button(
            self.buttonframe,
            text="7",
            font={"arial", 16},
            command=lambda: self.button_click("7"),
        )
        self.btn7.grid(row=1, column=0, sticky=tk.W + tk.E)

        self.btn8 = tk.Button(
            self.buttonframe,
            text="8",
            font={"arial", 16},
            command=lambda: self.button_click("8"),
        )
        self.btn8.grid(row=1, column=1, sticky=tk.W + tk.E)

        self.btn9 = tk.Button(
            self.buttonframe,
            text="9",
            font={"arial", 16},
            command=lambda: self.button_click("9"),
        )
        self.btn9.grid(row=1, column=2, sticky=tk.W + tk.E)

        self.btndot = tk.Button(
            self.buttonframe,
            text=".",
            font={"arial", 16},
            command=lambda: self.button_click("."),
        )
        self.btndot.grid(row=4, column=2, sticky=tk.W + tk.E)

        self.btnSubstract = tk.Button(
            self.buttonframe,
            text="-",
            font={"arial", 16},
            command=lambda: self.button_click("-"),
        )
        self.btnSubstract.grid(row=1, column=3, sticky=tk.W + tk.E)

        self.btnPlus = tk.Button(
            self.buttonframe,
            text="+",
            font={"arial", 16},
            command=lambda: self.button_click("+"),
        )
        self.btnPlus.grid(row=0, column=3, sticky=tk.W + tk.E)

        self.btnDivide = tk.Button(
            self.buttonframe,
            text="/",
            font={"arial", 16},
            command=lambda: self.button_click("/"),
        )
        self.btnDivide.grid(row=0, column=2, sticky=tk.W + tk.E)

        self.btnMultiply = tk.Button(
            self.buttonframe,
            text="*",
            font={"arial", 16},
            command=lambda: self.button_click("*"),
        )
        self.btnMultiply.grid(row=0, column=1, sticky=tk.W + tk.E)

        self.equal = tk.Button(
            self.buttonframe,
            text="Backspace",
            font={"arial", 16},
            command=lambda: self.button_click("backspace"),
        )
        self.equal.grid(row=2, column=3, sticky=tk.W + tk.E + tk.N + tk.S)

        self.equal = tk.Button(
            self.buttonframe,
            text="C",
            font={"arial", 16},
            command=lambda: self.button_click("c"),
        )
        self.equal.grid(row=0, column=0, sticky=tk.W + tk.E + tk.N + tk.S)

        self.equal = tk.Button(
            self.buttonframe,
            text="=",
            font={"arial", 16},
            command=lambda: self.button_click("="),
        )
        self.equal.grid(row=3, column=3, rowspan=2, sticky=tk.W + tk.E + tk.N + tk.S)

        self.buttonframe.pack(fill="x")

        self.root.mainloop()

    def select_all(self, event):
        self.entry.select_range(0, tk.END)
        return "break"

    def validate_input(self, char, action_type):
        valid_chars = "0123456789*/-+.\b"
        if action_type == "1":
            return char in valid_chars
        elif action_type == "0":
            return True

    def input_entry_not_focused(self, event):
        if not self.root.focus_get() == self.entry:

            if event.keysym == "BackSpace":
                if self.entry.selection_present():
                    self.entry.delete(tk.SEL_FIRST, tk.SEL_LAST)
                else:
                    current_position = self.entry.index(tk.INSERT)
                    if current_position > 0:
                        self.entry.delete(current_position - 1)
            else:
                if self.validate_input(event.char, "1"):
                    self.entry.insert(tk.END, event.char)

    def button_click(self, text):

        if text != "backspace" and text != "=" and text != "c":
            current_text = self.entry.get()
            new_text = f"{current_text}{text}"
            self.entry.config(validate="none")
            self.entry.delete(0, tk.END)
            self.entry.insert(0, new_text)
            self.entry.config(validate="key")
        elif text == "backspace":
            current_text = self.entry.get()
            new_text = current_text[:-1]
            self.entry.config(validate="none")
            if self.entry.selection_present():
                self.entry.delete(tk.SEL_FIRST, tk.SEL_LAST)
            else:
                current_position = self.entry.index(tk.INSERT)
                if current_position > 0:
                    self.entry.delete(current_position - 1)
            self.entry.config(validate="key")
        elif text == "c":
            self.entry.delete(0, tk.END)
        elif text == "=":
            raw_string = self.entry.get()
            pattern = r"\-|\+|\*|/"
            pattern_add_substract = r"\-|\+"
            pattern_multiply_divide = r"\*|/"

            pattern_invalid_zero = r'\b0\d+|[/*\-+]0\d+'
            pattern_invalid_dots = r'(?<!\d)\.(?!\d)|\.\.|\.\d+\.|[/*\-+]\.[/*\-+]'

            find_invalid_zero = bool(re.search(pattern_invalid_zero, raw_string))
            find_invalid_dots = bool(re.search(pattern_invalid_dots, raw_string))

            if "/0" in raw_string:
                self.result.config(text="Can not divide by 0")
                return
            if(find_invalid_zero):
                self.result.config(text="Invalid expression, invalid zero")
                return None
            if(find_invalid_dots):
                self.result.config(text="Invalid expression, wrong dot location")
                return None

            split_numbers = re.split(pattern, raw_string)
            removed_empty_strings_from_split = []
            for str_number in split_numbers:
                if str_number != "":
                    removed_empty_strings_from_split.append(str_number)

            all_operation_signs = re.findall(pattern, raw_string)

            if len(all_operation_signs) >= len(removed_empty_strings_from_split):
                self.result.config(text="Invalid expression, operation sign isolated")
                return None

            split_entire_multiplications_divisions = re.split(
                pattern_add_substract, raw_string
            )
            findall_last_additions_and_substractions = re.findall(
                pattern_add_substract, raw_string
            )

            # solve:
            first_operations = []

            for i in range(len(split_entire_multiplications_divisions)):
                if (
                    "*" not in split_entire_multiplications_divisions[i]
                    and "/" not in split_entire_multiplications_divisions[i]
                ):
                    first_operations.append(split_entire_multiplications_divisions[i])
                else:
                    numbers_inside = re.split(
                        pattern_multiply_divide,
                        split_entire_multiplications_divisions[i],
                    )
                    operators_inside = re.findall(
                        pattern_multiply_divide,
                        split_entire_multiplications_divisions[i],
                    )
                    result = 0

                    for j in range(len(operators_inside)):
                        if j == 0:
                            if operators_inside[j] == "*":
                                result = float(numbers_inside[j]) * float(
                                    numbers_inside[j + 1]
                                )
                            elif operators_inside[j] == "/":
                                result = float(numbers_inside[j]) / float(
                                    numbers_inside[j + 1]
                                )

                        else:
                            if operators_inside[j] == "*":
                                result *= float(numbers_inside[j + 1])
                            elif operators_inside[j] == "/":
                                result /= float(numbers_inside[j + 1])
                    first_operations.append(str(result))

            print(first_operations)

            total_result = 0
            if len(first_operations) == 1:
                total_result = float(first_operations[0])
                self.result.config(text=str(total_result))
                return None

            for i in range(len(findall_last_additions_and_substractions)):
                if i == 0:
                    if findall_last_additions_and_substractions[i] == "+":
                        total_result = float(first_operations[i]) + float(
                            first_operations[i + 1]
                        )
                    else:
                        total_result = float(first_operations[i]) - float(
                            first_operations[i + 1]
                        )
                else:
                    if findall_last_additions_and_substractions[i] == "+":
                        total_result += float(first_operations[i + 1])
                    else:
                        total_result -= float(first_operations[i + 1])

            print(total_result)

            self.result.config(text=str(total_result))


# 2*2*2+5*5+8-5+8/4+8
Calculator()
