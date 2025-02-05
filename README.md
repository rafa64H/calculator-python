# Calculator

This calculator program was made with python and tkinter.

## Brief explanation

Apart from the buttons and the tk.Entry to input the value, the code has

```
        self.root.bind("<KeyPress>", self.input_root_binded)
```

To receive inputs from the keyboards without needing to focus the tk.Entry

```
if not self.root.focus_get() == self.entry:
```

It's there because if the conditional wasn't there it would input two characters instead of one
