import re
import tkinter as tk
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Store players globally
players = []

class Receive:
    """Represents a receive action in volleyball."""
    def __init__(self, result: str, receive_type: str):
        self.result = result
        self.receive_type = receive_type

    def __str__(self):
        return f"Receive: {self.receive_type} | Result: {self.result}"


class Block:
    """Represents a block action in volleyball."""
    def __init__(self, result: str, block_number: int):
        self.result = result
        self.block_number = block_number

    def __str__(self):
        return f"Block | Result: {self.result} | Blockers: {self.block_number}"


class Pass:
    """Represents a pass action in volleyball."""
    def __init__(self, result: str, pass_type: str):
        self.result = result
        self.pass_type = pass_type

    def __str__(self):
        return f"Pass: {self.pass_type} | Result: {self.result}"


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
    """Represents a volleyball player with attack, service, block, receive, and pass stats."""
    def __init__(self, player_number: int):
        self.player_number = player_number
        self.attacks = []
        self.services = []
        self.blocks = []
        self.receives = []
        self.passes = []

    def add_attack(self, result: str, block_number: int, attack_type: str):
        self.attacks.append(Attack(result, block_number, attack_type))

    def add_service(self, result: str, service_type: str):
        self.services.append(Service(result, service_type))

    def add_receive(self, result: str, receive_type: str):
        self.receives.append(Receive(result, receive_type))

    def add_block(self, result: str, block_number: int):
        self.blocks.append(Block(result, block_number))

    def add_pass(self, result: str, pass_type: str):
        self.passes.append(Pass(result, pass_type))

    def __str__(self):
        """Returns a formatted string of player details."""
        attack_summary = "\n".join(str(a) for a in self.attacks) if self.attacks else "No attacks recorded"
        service_summary = "\n".join(str(s) for s in self.services) if self.services else "No services recorded"
        block_summary = "\n".join(str(b) for b in self.blocks) if self.blocks else "No blocks recorded"
        receive_summary = "\n".join(str(r) for r in self.receives) if self.receives else "No receives recorded"
        pass_summary = "\n".join(str(p) for p in self.passes) if self.passes else "No passes recorded"

        return (
            f"Player #{self.player_number}\n"
            f"Attacks:\n{attack_summary}\n\n"
            f"Services:\n{service_summary}\n\n"
            f"Blocks:\n{block_summary}\n\n"
            f"Receives:\n{receive_summary}\n\n"
            f"Passes:\n{pass_summary}"
        )

def check_action(text):
    """
    Checks each part of the text and assigns the correct volleyball action.
    - 'a' → Attack
    - 's' → Service
    - 'b' → Block
    - 'r' → Receive
    - 'p' → Pass
    """
    pattern = r'\b(\d+)\s*([asbrp])'  # Matches a number followed by 'a', 's', 'b', 'r', or 'p'
    matches = re.findall(pattern, text)

    for match in matches:
        player_number = int(match[0])
        action_type = match[1]  # 'a', 's', 'b', 'r', or 'p'

        # Find the player, or create a new one if not found
        player = next((p for p in players if p.player_number == player_number), None)
        if player is None:
            print(f"Creating new player: #{player_number}")
            player = Player(player_number)
            players.append(player)

        # Avoid duplicate entries by checking last added action
        if action_type == 'a' and (not player.attacks or player.attacks[-1].attack_type != "Spike"):
            print(f"Attack detected for Player #{player_number}")
            player.add_attack(result="Point", block_number=1, attack_type="Spike")
            print(f"Attack added to Player #{player_number}")

        elif action_type == 's' and (not player.services or player.services[-1].service_type != "Jump Serve"):
            print(f"Service detected for Player #{player_number}")
            player.add_service(result="Ace", service_type="Jump Serve")
            print(f"Service added to Player #{player_number}")

        elif action_type == 'b' and (not player.blocks or player.blocks[-1].block_number != 2):
            print(f"Block detected for Player #{player_number}")
            player.add_block(result="Successful", block_number=2)
            print(f"Block added to Player #{player_number}")

        elif action_type == 'r' and (not player.receives or player.receives[-1].receive_type != "Forearm Pass"):
            print(f"Receive detected for Player #{player_number}")
            player.add_receive(result="Perfect", receive_type="Forearm Pass")
            print(f"Receive added to Player #{player_number}")

        elif action_type == 'p' and (not player.passes or player.passes[-1].pass_type != "Overhead Set"):
            print(f"Pass detected for Player #{player_number}")
            player.add_pass(result="Accurate", pass_type="Overhead Set")
            print(f"Pass added to Player #{player_number}")

def process_text(event=None):
    """Splits the input text at every '.' and updates the result box only once."""
    text_content = input_box.get("1.0", tk.END).strip()

    if not text_content:
        return

    parts = text_content.split('.')

    processed_parts = set()

    for part in parts:
        cleaned_part = part.strip()
        if cleaned_part and cleaned_part not in processed_parts:
            check_action(cleaned_part)
            processed_parts.add(cleaned_part)

    # Update result box
    result_box.config(state=tk.NORMAL)  
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, "\n".join(parts))
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

        result_box.config(state=tk.NORMAL)
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, content)
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
    """Displays player statistics in a table format using a Tkinter window."""
    if not players:
        messagebox.showinfo("Statistics", "No player data available.")
        return

    # Create a new window for displaying stats
    stats_window = tk.Toplevel()
    stats_window.title("Player Statistics")
    stats_window.geometry("600x400")

    # Create a Treeview table
    columns = ("Player", "Service", "Receive", "Attack", "Block", "Pass")
    tree = ttk.Treeview(stats_window, columns=columns, show="headings")

    # Define column headings
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center")  # Adjust width

    # Insert player data into the table
    for player in players:
        services_count = len(player.services)
        receives_count = len(player.receives)
        attacks_count = len(player.attacks)
        blocks_count = len(player.blocks)
        passes_count = len(player.passes)

        print(f"Player {player.player_number}: Services={services_count}, Receives={receives_count}, Attacks={attacks_count}, Blocks={blocks_count}, Passes={passes_count}")

        tree.insert("", tk.END, values=(
            player.player_number,
            services_count,
            receives_count,
            attacks_count,
            blocks_count,
            passes_count
        ))

    tree.pack(expand=True, fill="both")

    # Run the table window
    stats_window.mainloop()


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

