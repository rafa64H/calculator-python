import tkinter as tk
import re
from buttons_config import buttons_array


class Calculator:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x700")
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

        self.root.bind("<KeyPress>", self.input_root_binded)

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)
        self.buttonframe.columnconfigure(3, weight=1)

        for button_item in buttons_array:
            new_btn = tk.Button(
                self.buttonframe,
                text=button_item["text"],
                font={"arial", 16},
                command=lambda text=button_item["text"]: self.button_click(text),
            )
            grid_options = {
                "row": button_item["row"],
                "column": button_item["column"],
            }
            if button_item["sticky"] == "left_right":
                grid_options["sticky"] = tk.W + tk.E
            if button_item["sticky"] == "up_down_left_right":
                grid_options["sticky"] = tk.N + tk.S + tk.W + tk.E
            if button_item["columnspan"] != False:
                grid_options["columnspan"] = button_item["columnspan"]
            if button_item["rowspan"] != False:
                grid_options["rowspan"] = button_item["rowspan"]
            new_btn.grid(**grid_options)

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

    def input_root_binded(self, event):
        if (
            event.keysym == "Return"
            or event.keysym == "KP_Enter"
            or event.keysym == "equal"
        ):
            self.button_click("=")
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

        if text != "Backspace" and text != "=" and text != "c":
            current_text = self.entry.get()
            new_text = f"{current_text}{text}"
            self.entry.config(validate="none")
            self.entry.delete(0, tk.END)
            self.entry.insert(0, new_text)
            self.entry.config(validate="key")
        elif text == "Backspace":
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

            pattern_invalid_zero = r"\b0\d+|[/*\-+]0\d+"
            pattern_invalid_dots = r"(?<!\d)\.(?!\d)|\.\.|\.\d+\.|[/*\-+]\.[/*\-+]"

            find_invalid_zero = bool(re.search(pattern_invalid_zero, raw_string))
            find_invalid_dots = bool(re.search(pattern_invalid_dots, raw_string))

            if "/0" in raw_string:
                self.result.config(text="Can not divide by 0")
                return
            if find_invalid_zero:
                self.result.config(text="Invalid expression, invalid zero")
                return None
            if find_invalid_dots:
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

            result = eval(raw_string)

            self.result.config(text=str(result))


Calculator()
