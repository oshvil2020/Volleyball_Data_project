import re
import tkinter as tk
from tkinter import filedialog, messagebox

# Store players globally
players = []

class Attack:
    """Represents an attack action in volleyball."""
    def __init__(self, result: str, block_number: int, attack_type: str):
        self.result = result
        self.block_number = block_number
        self.attack_type = attack_type

    def __str__(self):
        return f"Attack: {self.attack_type} | Result: {self.result} | Blockers: {self.block_number}"

class Service:
    """Represents a service action in volleyball."""
    def __init__(self, result: str, service_type: str):
        self.result = result
        self.service_type = service_type

    def __str__(self):
        return f"Service: {self.service_type} | Result: {self.result}"

class Player:
    """Represents a volleyball player with attack and service stats."""
    def __init__(self, player_number: int):
        self.player_number = player_number
        self.attacks = []
        self.services = []

    def add_attack(self, result: str, block_number: int, attack_type: str):
        self.attacks.append(Attack(result, block_number, attack_type))

    def add_service(self, result: str, service_type: str):
        self.services.append(Service(result, service_type))

    # def __str__(self):
    #     attack_summary = "\n".join(str(a) for a in self.attacks) if self.attacks else "No attacks recorded"
    #     service_summary = "\n".join(str(s) for s in self.services) if self.services else "No services recorded"
    #     return f"Player #{self.player_number}\nAttacks:\n{attack_summary}\n\nServices:\n{service_summary}"

    def __str__(self):
        return self.to_string()  # Update __str__ to use new method name

    def to_string(self):
        """Returns a formatted string of player details."""
        attack_summary = "\n".join(str(a) for a in self.attacks) if self.attacks else "No attacks recorded"
        service_summary = "\n".join(str(s) for s in self.services) if self.services else "No services recorded"
        return f"Player #{self.player_number}\nAttacks:\n{attack_summary}\n\nServices:\n{service_summary}"

def check_action(text):
    """
    Checks each part of the text. If after a player number there is 'a', adds an attack to the corresponding player.
    """
    pattern = r'\b(\d+)\s*a'  # Matches a number followed by 'a' (captures the number)

    match = re.search(pattern, text)
    if not match:  # Check if match is None before accessing it
        return

    player_number = int(match.group(1))  # Extract player number
    print(f"attack detected for Player #{player_number}")

    # Find the player or create a new one
    player = next((p for p in players if p.player_number == player_number), None)

    if player is None:
        print(f"Creating new player: #{player_number}")
        player = Player(player_number)
        players.append(player)

    # Add an attack (default values for now)
    player.add_attack(result="Point", block_number=1, attack_type="Spike")
    print(f"Attack added to Player #{player_number}")

def process_text(event=None):
    """Splits the input text at every '.' and updates the result box"""
    text_content = input_box.get("1.0", tk.END).strip()  # Get input text

    parts = text_content.split('.')  # Split at every '.'

    # Check each part for 'attack' condition
    for part in parts:
        check_action(part.strip())

    # Update result box with all parts separated by newline
    result_box.config(state=tk.NORMAL)  # Enable editing to update content
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, "\n".join(part.strip() for part in parts))
    result_box.config(state=tk.DISABLED) 

def update_result_box(content):
    """Updates the result box with processed text"""
    result_box.config(state=tk.NORMAL)
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, content)
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


def open_file():
    """Opens a text file and loads its content into the input box."""
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if file_path:  # If a file was selected
        with open(file_path, "r") as file:
            content = file.read()

        result_box.config(state=tk.NORMAL)  # Enable editing before updating content
        result_box.delete("1.0", tk.END)  # Clear previous content
        result_box.insert(tk.END, content)  # Load new content
        result_box.config(state=tk.DISABLED)

def enable_edit(event=None):
    """Enables editing when double-clicking the result box"""
    result_box.config(state=tk.NORMAL)

def disable_edit(event=None):
    """Disables editing when pressing Enter inside the result box"""
    result_box.config(state=tk.DISABLED)
    return "break"

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
    """Displays player statistics in a message box."""
    if not players:
        messagebox.showinfo("Statistics", "No player data available.")
        return

    stats_text = "\n\n".join(player.to_string() for player in players)
    messagebox.showinfo("Player Statistics", stats_text)
def exit_app():
    """Closes the application"""
    root.quit()

# Create main window
root = tk.Tk()
root.title("Volleyball Scouting & Analysis")

# Create menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
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
input_box.bind("<Return>", process_text)

# Result text box (Right)
result_frame = tk.Frame(frame)
result_frame.pack(side=tk.RIGHT, padx=10)
tk.Label(result_frame, text="Processed Result (Double-click to Edit, Enter to Lock):").pack()
result_box = tk.Text(result_frame, wrap="word", height=10, width=40)
result_box.pack()
result_box.config(state=tk.DISABLED)
result_box.bind("<Double-Button-1>", enable_edit)
result_box.bind("<Return>", disable_edit)
result_box.bind("<KeyRelease>", check_for_dot)

# Save Button
save_button = tk.Button(root, text="Save to File", command=save_to_file)
save_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()

