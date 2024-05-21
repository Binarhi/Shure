import tkinter as tk
from tkinter import ttk, messagebox

# List to store entries as dictionaries
mics = []


def process_input():
    try:
        receiver_name = entry_receiver_name.get()
        ip_address = entry_ip.get()
        receiver_channel = combo_receiver_channel.get()
        m32_channel = f"{int(combo_m32_channel.get()):02d}"
        m32_ip = entry_m32_ip.get()

        # Validate input ranges
        if receiver_channel not in ["A", "B", "C", "D"]:
            raise ValueError("Invalid receiver_ch. Please select A, B, C, or D.")

        receiver_type = combo_receiver_type.get()

        # Create a dictionary with the input data
        mic = {
            "receiver_name": receiver_name,
            "receiver_ip": ip_address,
            "receiver_type": receiver_type,
            "receiver_ch": receiver_channel,
            "receiver_x32_ch": m32_channel,
            "M32 IP": m32_ip,
        }

        # Append the dictionary to the list
        mics.append(mic)

        # Display a message box with the processed information
        result_message = f"Entry added to the list:\n{mic}"
        messagebox.showinfo("Input Processed", result_message)

        # Clear the entry fields for the next input
        entry_receiver_name.delete(0, tk.END)
        entry_ip.delete(0, tk.END)
        combo_receiver_channel.set("")  # Clear the selected value
        combo_m32_channel.set("")  # Clear the selected value

        # Update the displayed entries in the table
        update_entries_table()

    except ValueError as e:
        messagebox.showerror("Error", str(e))

def update_entries_table():
    # Clear the existing entries in the table
    for row in tree.get_children():
        tree.delete(row)

    # Insert the entered data into the table
    for i, mic in enumerate(mics, 1):
        tree.insert("", "end", values=(i, mic["receiver_name"], mic["receiver_ip"],
                                       mic["receiver_type"], mic["receiver_ch"],
                                       mic["receiver_x32_ch"], mic["M32 IP"]))

def remove_selected_entry():
    # Get the selected item(s) from the tree
    selected_items = tree.selection()

    # Remove the selected entries from the list and update the table
    for item in selected_items:
        index = int(tree.item(item, "values")[0]) - 1
        del mics[index]

    # Update the displayed entries in the table
    update_entries_table()

def toggle_button():
    global toggle_state
    toggle_state = not toggle_state
    if toggle_state:
        button_toggle.config(text="RUNNING")
        # Additional functionality to be executed when toggle is on
    else:
        button_toggle.config(text="STOPPED")
        # Additional functionality to be executed when toggle is off

# Create the main window
root = tk.Tk()
root.title("Shure/M32 Monitor - Femi Oyedeji 2023 Test")

# Create and place labels and entry fields horizontally
label_receiver_name = tk.Label(root, text="receiver_name:")
label_receiver_name.grid(row=0, column=0, padx=10, pady=5)
entry_receiver_name = ttk.Entry(root, font=('Arial', 12))
entry_receiver_name.grid(row=0, column=1, padx=10, pady=5)

label_ip = tk.Label(root, text="receiver_ip:")
label_ip.grid(row=0, column=2, padx=10, pady=5)
entry_ip = ttk.Entry(root, font=('Arial', 12))
entry_ip.grid(row=0, column=3, padx=10, pady=5)

label_receiver_type = tk.Label(root, text="receiver_type:")
label_receiver_type.grid(row=0, column=4, padx=10, pady=5)
receiver_type_choices = ["SLXD", "QLXD", "ULXD", "AXTD"]
combo_receiver_type = ttk.Combobox(root, values=receiver_type_choices, state="readonly")
combo_receiver_type.grid(row=0, column=5, padx=10, pady=5)

label_receiver_channel = tk.Label(root, text="receiver_ch:")
label_receiver_channel.grid(row=0, column=6, padx=10, pady=5)
receiver_channel_choices = ["A", "B", "C", "D"]
combo_receiver_channel = ttk.Combobox(root, values=receiver_channel_choices, state="readonly")
combo_receiver_channel.grid(row=0, column=7, padx=10, pady=5)

label_m32_channel = tk.Label(root, text="receiver_x32_ch:")
label_m32_channel.grid(row=0, column=8, padx=10, pady=5)
m32_channel_choices = [f"{i:02d}" for i in range(1, 33)]
combo_m32_channel = ttk.Combobox(root, values=m32_channel_choices, state="readonly")
combo_m32_channel.grid(row=0, column=9, padx=10, pady=5)

# Add M32 IP entry field
label_m32_ip = tk.Label(root, text="M32 IP:")
label_m32_ip.grid(row=1, column=0, padx=10, pady=5)
entry_m32_ip = ttk.Entry(root, font=('Arial', 12))
entry_m32_ip.grid(row=1, column=1, padx=10, pady=5)
entry_m32_ip.insert(0, "192.168.1.1")  # Set a default M32_IP value

# Create a button to trigger the processing of input
process_button = tk.Button(root, text="Process Input", command=process_input)
process_button.grid(row=2, column=0, columnspan=10, pady=10)

# Create a frame to display the entered data in a table
frame_table = tk.Frame(root)
frame_table.grid(row=3, column=0, columnspan=10, padx=10, pady=10, sticky="w")

# Create a Treeview widget (table)
tree = ttk.Treeview(frame_table, columns=("ID", "receiver_name", "receiver_ip", "receiver_type", "receiver_ch", "receiver_x32_ch", "M32 IP"), show="headings")
tree.heading("ID", text="ID")
tree.heading("receiver_name", text="receiver_name")
tree.heading("receiver_ip", text="receiver_ip")
tree.heading("receiver_type", text="receiver_type")
tree.heading("receiver_ch", text="receiver_ch")
tree.heading("receiver_x32_ch", text="receiver_x32_ch")
tree.heading("M32 IP", text="M32 IP")
tree.pack()

X32_IP = entry_m32_ip
# Create a button to remove selected entries from the table
remove_button = tk.Button(root, text="Remove Selected", command=remove_selected_entry)
remove_button.grid(row=4, column=0, columnspan=10, pady=10)

# Create a toggle button
toggle_state = False
button_toggle = tk.Button(root, text="STOPPED", command=toggle_button)
button_toggle.grid(row=3, column=11, padx=10, pady=10)

# Update the table with the initial entries
update_entries_table()

# Start the main event loop
root.mainloop()
