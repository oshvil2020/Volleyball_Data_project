import tkinter as tk
from tkinter import filedialog

def process_text(event=None):
    """Splits the input text at the first '.' and updates the result box"""
    text_content = input_box.get("1.0", tk.END).strip()  
    
    if '.' in text_content:
        first_part, second_part = text_content.split('.', 1)
    else:
        first_part = text_content
        second_part = "" 

    # Show result in the second text box
    result_box.config(state=tk.NORMAL)  
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, f"{first_part.strip()}\n{second_part.strip()}")
    result_box.config(state=tk.DISABLED)  

def save_to_file():
    """Saves the processed text to a file"""
    text_content = result_box.get("1.0", tk.END).strip()
    
    if not text_content:
        print("No content to save!")
        return
    
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if file_path:
        with open(file_path, "w") as file:
            file.write(text_content)
        print(f"File saved: {file_path}")
        
def enable_edit(event=None):
    """Enables editing when double-clicking the result box"""
    result_box.config(state=tk.NORMAL)

def disable_edit(event=None):
    """Disables editing when pressing Enter inside the result box"""
    result_box.config(state=tk.DISABLED)

# Create main window
root = tk.Tk()
root.title("Volleyball Code")

# Create a frame for side-by-side layout
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Input text box (Left)
input_frame = tk.Frame(frame)
input_frame.pack(side=tk.LEFT, padx=10)
tk.Label(input_frame, text="Enter Text (Press Enter to Process):").pack()
input_box = tk.Text(input_frame, wrap="word", height=10, width=40)
input_box.pack()
input_box.bind("<Return>", process_text)  # Bind Enter key to process function

# Result text box (Right)
result_frame = tk.Frame(frame)
result_frame.pack(side=tk.RIGHT, padx=10)
tk.Label(result_frame, text="Processed Result (Double-click to Edit):").pack()
result_box = tk.Text(result_frame, wrap="word", height=10, width=40)
result_box.pack()
result_box.config(state=tk.DISABLED)  # Make initially read-only
result_box.bind("<Double-Button-1>", enable_edit)  # Enable editing on double-click
result_box.bind("<Return>", disable_edit)  # Make read-only again on Enter

# Save Button
save_button = tk.Button(root, text="Save to File", command=save_to_file)
save_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()

