import customtkinter as ctk

# Function to handle button clicks
def button_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Function to clear the display
def clear():
    global expression
    expression = ""
    input_text.set(expression)

# Function to calculate the result
def equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        history.append(expression + " = " + result)
        expression = ""
    except:
        input_text.set("Error")
        expression = ""

# Function to show history
def show_history():
    history_window = ctk.CTkToplevel()
    history_window.title("History")
    history_window.geometry("300x400")
    history_label = ctk.CTkLabel(history_window, text="\n".join(history), justify="left", font=app_font)
    history_label.pack(pady=10, padx=10)

# Initialize the application
app = ctk.CTk()
app.title("Calculator")
app.geometry("400x200")
app.configure(fg_color="black")  # Set the background color

expression = ""
history = []
input_text = ctk.StringVar()

# Define the Gwendolyn font using CTkFont
app_font = ctk.CTkFont(family="Gwendolyn", size=20)

# Display frame
input_frame = ctk.CTkFrame(app, width=400, height=50, fg_color="black")
input_frame.pack(side=ctk.TOP, pady=20)
input_field = ctk.CTkEntry(input_frame, textvariable=input_text, font=app_font, width=200, justify=ctk.RIGHT, fg_color="black", text_color="white")
input_field.grid(row=0, column=0)

# Buttons frame
buttons_frame = ctk.CTkFrame(app, width=400, height=450, fg_color="black")
buttons_frame.pack()

# Button layout
button_texts = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('History', 5, 0, 4)
]

for (text, row, col, *span) in button_texts:
    action = lambda x=text: button_click(x) if x not in {'C', '=', 'History'} else clear() if x == 'C' else equal() if x == '=' else show_history()
    ctk.CTkButton(buttons_frame, text=text, command=action, font=app_font, text_color="white", fg_color="black").grid(row=row, column=col, columnspan=span[0] if span else 1, sticky="nsew")

for i in range(5):
    buttons_frame.grid_rowconfigure(i, weight=1)
    buttons_frame.grid_columnconfigure(i, weight=1)

# Run the application
app.mainloop()
