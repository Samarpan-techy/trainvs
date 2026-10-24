import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import random

# --- 1. Pandas ka use karke Data taiyaar karna (Real Trains Data) ---
def generate_dummy_data():
    REAL_TRAINS = [
        # NDLS to SVDK
        {'Train_No': 14033, 'Train_Name': 'Jammu Mail', 'Source': 'NDLS', 'Destination': 'SVDK', 'Class': ['1A', '2A', '3A', 'SL']},
        {'Train_No': 12445, 'Train_Name': 'Uttar Sampark Kranti', 'Source': 'NDLS', 'Destination': 'SVDK', 'Class': ['1A', '2A', '3A', 'SL']},
        {'Train_No': 22439, 'Train_Name': 'NDLS - SVDK Vande Bharat', 'Source': 'NDLS', 'Destination': 'SVDK', 'Class': ['CC', 'EC']},
        # SVDK to NDLS
        {'Train_No': 14034, 'Train_Name': 'Jammu Mail', 'Source': 'SVDK', 'Destination': 'NDLS', 'Class': ['1A', '2A', '3A', 'SL']},
        {'Train_No': 12446, 'Train_Name': 'Uttar Sampark Kranti', 'Source': 'SVDK', 'Destination': 'NDLS', 'Class': ['1A', '2A', '3A', 'SL']},
        {'Train_No': 22440, 'Train_Name': 'SVDK - NDLS Vande Bharat', 'Source': 'SVDK', 'Destination': 'NDLS', 'Class': ['CC', 'EC']},

        # NDLS to HWH / HWH to NDLS
        {'Train_No': 12302, 'Train_Name': 'New Delhi - Howrah Rajdhani', 'Source': 'NDLS', 'Destination': 'HWH', 'Class': ['1A', '2A', '3A']},
        {'Train_No': 12274, 'Train_Name': 'New Delhi - Howrah Duronto', 'Source': 'NDLS', 'Destination': 'HWH', 'Class': ['1A', '2A', '3A']},
        {'Train_No': 12304, 'Train_Name': 'Poorva Express', 'Source': 'NDLS', 'Destination': 'HWH', 'Class': ['1A', '2A', '3A', 'SL']},
        {'Train_No': 12306, 'Train_Name': 'Kolkata Rajdhani', 'Source': 'NDLS', 'Destination': 'HWH', 'Class': ['1A', '2A', '3A']},
        {'Train_No': 12301, 'Train_Name': 'Howrah - New Delhi Rajdhani', 'Source': 'HWH', 'Destination': 'NDLS', 'Class': ['1A', '2A', '3A']},

        # NDLS to BCT
        {'Train_No': 12952, 'Train_Name': 'Mumbai Rajdhani', 'Source': 'NDLS', 'Destination': 'BCT', 'Class': ['1A', '2A', '3A']},
        {'Train_No': 12954, 'Train_Name': 'August Kranti Rajdhani', 'Source': 'NDLS', 'Destination': 'BCT', 'Class': ['1A', '2A', '3A']},
        {'Train_No': 12926, 'Train_Name': 'Paschim Express', 'Source': 'NDLS', 'Destination': 'BCT', 'Class': ['1A', '2A', '3A', 'SL']},
        {'Train_No': 12904, 'Train_Name': 'Golden Temple Mail', 'Source': 'NDLS', 'Destination': 'BCT', 'Class': ['1A', '2A', '3A', 'SL']},
        {'Train_No': 12951, 'Train_Name': 'Mumbai Central - New Delhi Rajdhani', 'Source': 'BCT', 'Destination': 'NDLS', 'Class': ['1A', '2A', '3A']},

        # NDLS to MAS
        {'Train_No': 12616, 'Train_Name': 'Grand Trunk Express', 'Source': 'NDLS', 'Destination': 'MAS', 'Class': ['1A', '2A', '3A', 'SL']},
        {'Train_No': 12622, 'Train_Name': 'Tamil Nadu Express', 'Source': 'NDLS', 'Destination': 'MAS', 'Class': ['1A', '2A', '3A', 'SL']},
        {'Train_No': 12612, 'Train_Name': 'MAS Garib Rath', 'Source': 'NDLS', 'Destination': 'MAS', 'Class': ['3A']},
        {'Train_No': 12270, 'Train_Name': 'NZM MAS Duronto', 'Source': 'NDLS', 'Destination': 'MAS', 'Class': ['1A', '2A', '3A']},

        # NDLS to ADI
        {'Train_No': 12958, 'Train_Name': 'Swarna Jayanti Rajdhani', 'Source': 'NDLS', 'Destination': 'ADI', 'Class': ['1A', '2A', '3A']},
        {'Train_No': 12916, 'Train_Name': 'Ashram Express', 'Source': 'NDLS', 'Destination': 'ADI', 'Class': ['1A', '2A', '3A', 'SL']},
        {'Train_No': 14311, 'Train_Name': 'Ala Hazrat Express', 'Source': 'NDLS', 'Destination': 'ADI', 'Class': ['2A', '3A', 'SL']},
        {'Train_No': 12957, 'Train_Name': 'Swarna Jayanti Rajdhani', 'Source': 'ADI', 'Destination': 'NDLS', 'Class': ['1A', '2A', '3A']},

        # NDLS to BBS
        {'Train_No': 12820, 'Train_Name': 'Odisha Sampark Kranti', 'Source': 'NDLS', 'Destination': 'BBS', 'Class': ['1A', '2A', '3A', 'SL']},
        {'Train_No': 12876, 'Train_Name': 'Neelachal Express', 'Source': 'NDLS', 'Destination': 'BBS', 'Class': ['2A', '3A', 'SL']},

        # SVDK to HWH / BCT / ADI
        {'Train_No': 12332, 'Train_Name': 'Himgiri Express', 'Source': 'SVDK', 'Destination': 'HWH', 'Class': ['1A', '2A', '3A', 'SL']},
        {'Train_No': 12472, 'Train_Name': 'Swaraj Express', 'Source': 'SVDK', 'Destination': 'BCT', 'Class': ['2A', '3A', 'SL']},
        {'Train_No': 12474, 'Train_Name': 'Sarvodaya Express', 'Source': 'SVDK', 'Destination': 'ADI', 'Class': ['2A', '3A', 'SL']},

        # CSMT to PUNE
        {'Train_No': 12124, 'Train_Name': 'Deccan Queen', 'Source': 'CSMT', 'Destination': 'PUNE', 'Class': ['1A', '2A', 'CC']},
        {'Train_No': 12126, 'Train_Name': 'Pragati Express', 'Source': 'CSMT', 'Destination': 'PUNE', 'Class': ['1A', '2A', 'CC']},
        {'Train_No': 12127, 'Train_Name': 'Intercity Express', 'Source': 'CSMT', 'Destination': 'PUNE', 'Class': ['1A', '2A', 'CC']},

        # HWH to MAS / BBS
        {'Train_No': 12842, 'Train_Name': 'Coromandel Express', 'Source': 'HWH', 'Destination': 'MAS', 'Class': ['1A', '2A', '3A', 'SL']},
        {'Train_No': 12840, 'Train_Name': 'Chennai Mail', 'Source': 'HWH', 'Destination': 'MAS', 'Class': ['1A', '2A', '3A', 'SL']},
        {'Train_No': 12074, 'Train_Name': 'Jan Shatabdi', 'Source': 'HWH', 'Destination': 'BBS', 'Class': ['CC', 'EC']},
        
        # BCT to ADI / PBR
        {'Train_No': 12010, 'Train_Name': 'Shatabdi Express', 'Source': 'BCT', 'Destination': 'ADI', 'Class': ['CC', 'EC']},
        {'Train_No': 12902, 'Train_Name': 'Gujarat Mail', 'Source': 'BCT', 'Destination': 'ADI', 'Class': ['1A', '2A', '3A', 'SL']},
        {'Train_No': 19016, 'Train_Name': 'Saurashtra Express', 'Source': 'BCT', 'Destination': 'PBR', 'Class': ['2A', '3A', 'SL']},
        {'Train_No': 19202, 'Train_Name': 'Porbandar Express', 'Source': 'BCT', 'Destination': 'PBR', 'Class': ['2A', '3A', 'SL']},

        # CSMT to HWH
        {'Train_No': 12860, 'Train_Name': 'Gitanjali Express', 'Source': 'CSMT', 'Destination': 'HWH', 'Class': ['1A', '2A', '3A', 'SL']},
        {'Train_No': 12810, 'Train_Name': 'Howrah Mail', 'Source': 'CSMT', 'Destination': 'HWH', 'Class': ['1A', '2A', '3A', 'SL']},
        
        # PUNE to HWH
        {'Train_No': 20822, 'Train_Name': 'Pune Humsafar Express', 'Source': 'PUNE', 'Destination': 'HWH', 'Class': ['3A', 'SL']},
        
        # MAS to BBS
        {'Train_No': 12830, 'Train_Name': 'Chennai - Bhubaneswar Express', 'Source': 'MAS', 'Destination': 'BBS', 'Class': ['1A', '2A', '3A', 'SL']},
    ]
    
    df = pd.DataFrame(REAL_TRAINS)
    df = df.explode('Class').reset_index(drop=True)
    return df

df = generate_dummy_data()

# Route Database (Check karne ke liye ki train kis-kis station se hoke jayegi)
ROUTES = {
    14033: ['NDLS', 'PNP', 'UMB', 'LDH', 'JUC', 'PTK', 'JAT', 'SVDK'], # Jammu Mail
    14034: ['SVDK', 'JAT', 'PTK', 'JUC', 'LDH', 'UMB', 'PNP', 'NDLS'],
    22439: ['NDLS', 'UMB', 'LDH', 'JAT', 'SVDK'], # Vande Bharat
    22440: ['SVDK', 'JAT', 'LDH', 'UMB', 'NDLS'],
    12302: ['NDLS', 'CNB', 'PRYJ', 'GAYA', 'DHN', 'ASN', 'HWH'], # Rajdhani
    12952: ['NDLS', 'KOTA', 'RTM', 'BRC', 'ST', 'BCT'], # Mumbai Rajdhani
    12622: ['NDLS', 'AGC', 'GWL', 'JHS', 'BPL', 'NGP', 'BPQ', 'MAS'], # Tamil Nadu Exp
}

# --- 2. Route Checker Popup Function ---
def open_route_checker():
    route_win = tk.Toplevel(root)
    route_win.title("Check Train Route")
    route_win.geometry("450x500")
    route_win.configure(bg="white")
    route_win.transient(root)
    route_win.grab_set()

    tk.Label(route_win, text="🛤️ Check Train Route", font=("Helvetica", 16, "bold"), bg="white", fg="#cc0000").pack(pady=15)
    tk.Label(route_win, text="Select a train to view its route:", font=("Helvetica", 10), bg="white").pack(pady=5)

    # Saari unique trains ki list nikalna dropdown ke liye
    unique_trains = df.drop_duplicates(subset=['Train_No']).apply(
        lambda row: f"{row['Train_No']} - {row['Train_Name']}", axis=1
    ).tolist()
    
    train_combo = ttk.Combobox(route_win, values=unique_trains, width=45, state="readonly")
    train_combo.pack(pady=10)

    # Route dikhane ke liye Text Box
    route_text = tk.Text(route_win, font=("Courier New", 11), bg="#f9f9f9", bd=2, relief="sunken", width=45, height=15)
    route_text.pack(pady=10, padx=20)
    route_text.config(state=tk.DISABLED)

    def show_route(event=None):
        selected = train_combo.get()
        if not selected:
            return
        
        t_no = int(selected.split(" - ")[0])
        row = df[df['Train_No'] == t_no].iloc[0]
        
        # Agar dictionary me route hai toh wahan se lo, warna Source aur Destination dikha do
        route_list = ROUTES.get(t_no, [row['Source'], '...', row['Destination']])
        
        route_text.config(state=tk.NORMAL)
        route_text.delete(1.0, tk.END)
        
        route_text.insert(tk.END, f"Train: {row['Train_Name']}\n")
        route_text.insert(tk.END, "=" * 35 + "\n\n")
        
        for i, station in enumerate(route_list):
            route_text.insert(tk.END, f" 📍 {station}\n")
            if i < len(route_list) - 1:
                route_text.insert(tk.END, "    |\n    v\n")
                
        route_text.config(state=tk.DISABLED)

    train_combo.bind("<<ComboboxSelected>>", show_route)
    
    close_btn = tk.Button(route_win, text="Close", bg="#666", fg="white", font=("Helvetica", 10, "bold"), command=route_win.destroy)
    close_btn.pack(pady=10)

# --- 3. Interactive Dropdown & Popup Functions (Booking) ---
def on_class_select(train_no, cls):
    ask_coach_number(train_no, cls)

def show_classes_menu(event, train_no):
    classes = df[df['Train_No'] == int(train_no)]['Class'].unique()
    
    popup = tk.Menu(root, tearoff=0)
    popup.add_command(label=f"Train {train_no} Classes:", state="disabled")
    popup.add_separator()
    
    for cls in classes:
        popup.add_command(label=cls, command=lambda c=cls, t=train_no: on_class_select(t, c))
        
    try:
        popup.tk_popup(event.x_root, event.y_root, 0)
    finally:
        popup.grab_release()

def on_train_click(event):
    index = result_text.index(f"@{event.x},{event.y}")
    tags = result_text.tag_names(index)
    
    for tag in tags:
        if tag.startswith("train_"):
            t_no = tag.split("_")[1]
            show_classes_menu(event, t_no)
            break

def ask_coach_number(train_no, cls):
    prefix_map = {
        'SL': 'S', '3A': 'B', '2A': 'A', '1A': 'M', 'CC': 'CC', 'EC': 'EC'
    }
    expected_prefix = prefix_map.get(cls, '')

    coach_win = tk.Toplevel(root)
    coach_win.title("Enter Coach Number")
    coach_win.geometry("380x230")
    coach_win.transient(root)
    coach_win.grab_set()
    coach_win.geometry(f"+{root.winfo_rootx() + 230}+{root.winfo_rooty() + 200}")
    coach_win.configure(bg="white")

    tk.Label(coach_win, text=f"Train: {train_no} | Class: {cls}", font=("Helvetica", 11, "bold"), bg="white", fg="#cc0000").pack(pady=(15, 5))
    tk.Label(coach_win, text=f"Enter Coach Number (Starts with {expected_prefix}):", font=("Helvetica", 10), bg="white").pack(pady=5)
    
    coach_entry = ttk.Entry(coach_win, font=("Helvetica", 12), justify="center")
    coach_entry.pack(pady=5, ipadx=20, ipady=5)
    
    coach_entry.insert(0, expected_prefix)
    coach_entry.focus()
    coach_entry.icursor(tk.END)
    
    def generate_seat():
        coach = coach_entry.get().strip().upper()
        
        if not coach.startswith(expected_prefix):
            coach = expected_prefix + coach

        if coach == expected_prefix:
            messagebox.showwarning("Input Error", f"Please enter the coach number after '{expected_prefix}' (e.g., {expected_prefix}1).", parent=coach_win)
            return
            
        num_part = coach[len(expected_prefix):]
        if not num_part.isdigit():
             messagebox.showwarning("Input Error", f"Coach number must be like {expected_prefix}1, {expected_prefix}2, etc.", parent=coach_win)
             return

        seat_no = random.randint(1, 72)
        coach_win.destroy() 
        
        messagebox.showinfo(
            "Booking Successful 🎉",
            f"Aapki seat mil gayi hai!\n\n"
            f"🚆 Train: {train_no}\n"
            f"🎟️ Class: {cls}\n"
            f"🚃 Coach: {coach}\n"
            f"💺 Seat No: {seat_no}\n\n"
            f"Happy Journey!",
            parent=root
        )

    submit_btn = tk.Button(coach_win, text="Find Seat", bg="#ff6600", fg="white", 
                           font=("Helvetica", 10, "bold"), padx=20, pady=5, bd=0, cursor="hand2",
                           command=generate_seat)
    submit_btn.pack(pady=15)
    coach_entry.bind("<Return>", lambda e: generate_seat())

# --- 4. Search Function (Logic) ---
def search_trains():
    from_station = from_entry.get().strip().upper()
    to_station = to_entry.get().strip().upper()
    
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
        
    if not from_station or not to_station:
        messagebox.showwarning("Input Error", "Please enter both From and To stations.")
        result_text.config(state=tk.DISABLED)
        return

    filtered_df = df[(df['Source'] == from_station) & (df['Destination'] == to_station)]

    if not filtered_df.empty:
        unique_trains = filtered_df.drop_duplicates(subset=['Train_No'])
        
        result_text.insert(tk.END, f"Found {len(unique_trains)} trains from {from_station} to {to_station}.\n\n")
        result_text.insert(tk.END, f"{'Train No':<10} | {'Train Name (Click Here)':<35} | {'Available Classes'}\n")
        result_text.insert(tk.END, "-" * 85 + "\n")
        
        for index, row in unique_trains.iterrows():
            t_no = row['Train_No']
            t_name = row['Train_Name']
            
            classes_for_train = df[df['Train_No'] == t_no]['Class'].unique()
            classes_str = ", ".join(classes_for_train)
            
            result_text.insert(tk.END, f"{t_no:<10} | ")
            result_text.insert(tk.END, f"{t_name:<35}", ("clickable", f"train_{t_no}"))
            result_text.insert(tk.END, f" | {classes_str}\n")
            
        result_text.insert(tk.END, "\n💡 Tip: Kisi bhi train ke naam par click karein, waha dropdown khul jayega.\n")
            
    else:
        result_text.insert(tk.END, f"Sorry, no trains found from {from_station} to {to_station}.\n")
    
    result_text.config(state=tk.DISABLED)

# --- 5. GUI (Tkinter) Setup ---
root = tk.Tk()
root.title("Trainvs")
root.geometry("850x700") 
root.minsize(650, 550)   

root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1) 

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", font=("Helvetica", 10))
style.configure("TButton", font=("Helvetica", 10, "bold"))

# Header Frame
header_frame = tk.Frame(root, bg="#cc0000", pady=15)
header_frame.grid(row=0, column=0, sticky="ew")
tk.Label(header_frame, text="TRAINVS", font=("Helvetica", 20, "bold"), bg="#cc0000", fg="white").pack()

# Search Form Frame
form_frame = tk.Frame(root, bg="white", padx=20, pady=20)
form_frame.grid(row=1, column=0, sticky="ew")
form_frame.columnconfigure(0, weight=1)
form_frame.columnconfigure(1, weight=1)

tk.Label(form_frame, text="BOOK TICKET", font=("Helvetica", 16, "bold"), bg="white", fg="#cc0000").grid(row=0, column=0, columnspan=4, pady=(0, 15))

tk.Label(form_frame, text="From (e.g. SVDK, NDLS)", bg="white").grid(row=1, column=0, sticky="w")
from_entry = ttk.Entry(form_frame)
from_entry.grid(row=2, column=0, pady=(0, 10), padx=(0, 10), sticky="ew")

tk.Label(form_frame, text="To (e.g. NDLS, HWH)", bg="white").grid(row=1, column=2, sticky="w")
to_entry = ttk.Entry(form_frame)
to_entry.grid(row=2, column=2, pady=(0, 10), padx=(10, 0), sticky="ew")

tk.Label(form_frame, text="DD/MM/YYYY *", bg="white").grid(row=3, column=0, sticky="w")
date_entry = ttk.Entry(form_frame)
date_entry.insert(0, "08/10/2026")
date_entry.grid(row=4, column=0, pady=(0, 15), padx=(0, 10), sticky="ew")

tk.Label(form_frame, text="Quota", bg="white").grid(row=3, column=2, sticky="w")
quota_combo = ttk.Combobox(form_frame, values=["GENERAL", "LADIES", "TATKAL", "PREMIUM TATKAL"], state="readonly")
quota_combo.current(0)
quota_combo.grid(row=4, column=2, pady=(0, 15), padx=(10, 0), sticky="ew")

# Buttons Frame (Search aur Route button ek sath rakhne ke liye)
btn_frame = tk.Frame(form_frame, bg="white")
btn_frame.grid(row=5, column=0, columnspan=4, pady=10)

search_btn = tk.Button(btn_frame, text="Search Trains", bg="#ff6600", fg="white", 
                       font=("Helvetica", 11, "bold"), padx=20, pady=8, bd=0, cursor="hand2",
                       command=search_trains)
search_btn.pack(side="left", padx=10)

# Naya Route Check Button
route_btn = tk.Button(btn_frame, text="🛤️ Check Train Route", bg="#1a365d", fg="white", 
                      font=("Helvetica", 11, "bold"), padx=20, pady=8, bd=0, cursor="hand2",
                      command=open_route_checker)
route_btn.pack(side="left", padx=10)

# Results Frame (Text Widget)
result_frame = tk.Frame(root, bg="white", padx=20, pady=0)
result_frame.grid(row=2, column=0, sticky="nsew", pady=(0, 20)) 
result_frame.columnconfigure(0, weight=1)
result_frame.rowconfigure(0, weight=1)

result_text = tk.Text(result_frame, wrap="none", font=("Courier New", 11), bg="#f9f9f9", bd=2, relief="sunken")
result_text.grid(row=0, column=0, sticky="nsew")

result_text.tag_config("clickable", foreground="#cc0000", underline=True)
result_text.tag_bind("clickable", "<Button-1>", on_train_click)

v_scrollbar = ttk.Scrollbar(result_frame, orient="vertical", command=result_text.yview)
v_scrollbar.grid(row=0, column=1, sticky="ns")

h_scrollbar = ttk.Scrollbar(result_frame, orient="horizontal", command=result_text.xview)
h_scrollbar.grid(row=1, column=0, sticky="ew")

result_text.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
result_text.config(state=tk.DISABLED)

# Initial Data Display
result_text.config(state=tk.NORMAL)
result_text.insert(tk.END, "Welcome to Trainvs!\n\n")
result_text.insert(tk.END, "कृपया टेस्ट करने के लिए यहाँ से सर्च करें:\n")
result_text.insert(tk.END, "From: SVDK  |  To: NDLS\n")
result_text.insert(tk.END, "From: NDLS |  To: SVDK\n")
result_text.insert(tk.END, "From: NDLS |  To: HWH\n")
result_text.config(state=tk.DISABLED)

root.mainloop()