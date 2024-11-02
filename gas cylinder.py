import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Gas Cylinder Management System")
root.geometry("800x600")
root.configure(bg='gray20')

# Dashboard Heading
headingLabel = tk.Label(root, text="Gas Cylinder Management System", font=('Helvetica', 24, 'bold'), bg='gray20', fg='gold')
headingLabel.pack(pady=20)

# Inventory Overview Frame
inventory_frame = tk.Frame(root, bg='gray25', bd=5, relief=tk.GROOVE)
inventory_frame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.2)

inventory_label = tk.Label(inventory_frame, text="Inventory Overview", font=('Helvetica', 16, 'bold'), bg='gray25', fg='white')
inventory_label.pack(pady=10)

# Sales Summary Frame
sales_frame = tk.Frame(root, bg='gray25', bd=5, relief=tk.GROOVE)
sales_frame.place(relx=0.1, rely=0.45, relwidth=0.8, relheight=0.2)

sales_label = tk.Label(sales_frame, text="Sales Summary", font=('Helvetica', 16, 'bold'), bg='gray25', fg='white')
sales_label.pack(pady=10)

# Purchase Records Frame
purchase_frame = tk.Frame(root, bg='gray25', bd=5, relief=tk.GROOVE)
purchase_frame.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.2)

purchase_label = tk.Label(purchase_frame, text="Purchase Records", font=('Helvetica', 16, 'bold'), bg='gray25', fg='white')
purchase_label.pack(pady=10)

# Safety Alerts Frame
alerts_frame = tk.Frame(root, bg='gray25', bd=5, relief=tk.GROOVE)
alerts_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

alerts_label = tk.Label(alerts_frame, text="Safety Alerts", font=('Helvetica', 16, 'bold'), bg='gray25', fg='white')
alerts_label.pack(pady=10)

# Navigation Buttons
button_frame = tk.Frame(root, bg='gray20')
button_frame.pack(pady=20)

inventory_button = tk.Button(button_frame, text="Manage Inventory", font=('Helvetica', 14), bg='gray30', fg='white')
inventory_button.pack(side='left', padx=10)

sales_button = tk.Button(button_frame, text="Record Sales", font=('Helvetica', 14), bg='gray30', fg='white')
sales_button.pack(side='left', padx=10)

settings_button = tk.Button(button_frame, text="Settings", font=('Helvetica', 14), bg='gray30', fg='white')
settings_button.pack(side='left', padx=10)

root.mainloop()
