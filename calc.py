import tkinter as tk

# Pastel color palette
PASTEL_PINK = "#f2abaf"
PEACH_PINK = "#f5ccc6"
CREAM = "#fbf2e9"
SOFT_BLUE = "#b8c9e7"

# Main window setup
root = tk.Tk()
root.title("Calc 💖")
root.geometry("360x520")
root.configure(bg=CREAM)
root.resizable(False, False)

# Entry display
entry = tk.Entry(root, font=("Comic Sans MS", 22, "bold"), bd=4,
                 bg="white", fg=PASTEL_PINK, justify='right')
entry.pack(pady=20, padx=20, ipady=15, fill='x')

# Button press logic
def press(value):
    current = entry.get()
    if value == "C":
        entry.delete(0, tk.END)
    elif value == "=":
        try:
            result = eval(current.replace("×", "*").replace("÷", "/"))
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error 🤕")
    else:
        entry.insert(tk.END, value)

# Button layout
buttons = [
    ['7', '8', '9', '÷'],
    ['4', '5', '6', '×'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C']
]

# Cute annrehs title
title_label = tk.Label(root, text="✨ annrehs calculator ✨ ", font=("Comic Sans MS", 9, "italic"),
                       bg=CREAM, fg=PASTEL_PINK)
title_label.pack(pady=(1, 1))

# Pastel button colors
def get_color(val):
    if val in ['C', '=']:
        return SOFT_BLUE
    elif val in ['+', '-', '×', '÷']:
        return PASTEL_PINK
    else:
        return PEACH_PINK

# Button frame
btn_frame = tk.Frame(root, bg=CREAM)
btn_frame.pack(pady=10)

# Create each button
for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        btn = tk.Button(
            btn_frame, text=char, width=4, height=1,
            bg=get_color(char), fg="white", font=("Comic Sans MS", 18),
            bd=0, relief='ridge',
            command=lambda ch=char: press(ch)
        )
        btn.grid(row=r, column=c, padx=10, pady=10)

# Launch app
root.mainloop()