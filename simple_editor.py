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

def check_for_dot(event=None):
    """Checks for a '.' while editing the result box and splits text if found"""
    text_content = result_box.get("1.0", tk.END).strip()
    
    if '.' in text_content:
        first_part, second_part = text_content.split('.', 1)
        update_result_box(first_part, second_part)

def show_about():
    """Displays the 'About' information"""
    messagebox.showinfo("About", "Volleyball Scouting & Analysis\nVersion 1.0\nAn open-source project for volleyball data analysis.")

def show_statistics():
    """Placeholder for statistics display"""
    messagebox.showinfo("Statistics", "Feature under development.\nFuture updates will include player performance analytics.")

def exit_app():
    """Closes the application"""
    root.quit()
    
# Create main window
root = tk.Tk()
root.title("Volleyball Code")

# Create menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open")  # Placeholder for future functionality
file_menu.add_command(label="Save", command=save_to_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

# Statistics Menu
stats_menu = tk.Menu(menu_bar, tearoff=0)
stats_menu.add_command(label="Show Statistics", command=show_statistics)
menu_bar.add_cascade(label="Statistics", menu=stats_menu)

# About Menu
about_menu = tk.Menu(menu_bar, tearoff=0)
about_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="About", menu=about_menu)

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


# Example Usage
if __name__ == "__main__":
    player1 = Player(7)  # Create a player with jersey number 7
    player1.add_attack(result="Point", block_number=2, attack_type="Spike")
    player1.add_attack(result="Out", block_number=1, attack_type="Tip")
    player1.add_service(result="Ace", service_type="Jump Serve")
    player1.add_service(result="Fault", service_type="Float")

    print(player1)  # Display player's attack & service stats
