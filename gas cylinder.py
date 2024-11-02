import tkinter as tk
from tkinter import ttk
import sqlite3

# Functionality Part

def connectandcreatetable():
# Connect to SQLite database
    conn = sqlite3.connect('gascylinder.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT NOT NULL,
        batch_no INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        purchase_price REAL NOT NULL,
        date_received DATE NOT NULL
    );
    ''')
    conn.close()
connectandcreatetable()


def open_inventory_window():
    inventory_window = tk.Toplevel()
    inventory_window.title("Inventory Management")
    inventory_window.geometry("800x500")

    headingLabel = tk.Label(inventory_window, text="Inventory Management", font=('times new roman', 30, 'bold'), background='gray20', foreground='gold', bd=12, relief=tk.GROOVE)
    headingLabel.pack(fill=tk.X, pady=5)

    # Project Details
    treeviewFrame = tk.Frame(inventory_window, background='gray20', bd=8, relief=tk.GROOVE)
    treeviewFrame.pack(fill=tk.X, pady=5)

    columns = ('#1', '#2', '#3', '#4', '#5', '#6')
    tree = ttk.Treeview(treeviewFrame, columns=columns, show='headings')
    tree.heading('#1', text='Sr')
    tree.heading('#2', text='Item Name')
    tree.heading('#3', text='Batch Number')
    tree.heading('#4', text='Quantity')
    tree.heading('#5', text='Purchased Price')
    tree.heading('#6', text='Purchased Date')

    # Setting column widths
    tree.column('#1', width=30)
    tree.column('#2', width=150)
    tree.column('#3', width=100)
    tree.column('#4', width=100)
    tree.column('#5', width=70)
    tree.column('#6', width=70)

    # Adding Vertical Scrollbar
    vsb = ttk.Scrollbar(treeviewFrame, orient="vertical", command=tree.yview)
    vsb.pack(side='right', fill='y')
    tree.configure(yscrollcommand=vsb.set)

    # Adding Horizontal Scrollbar
    hsb = ttk.Scrollbar(treeviewFrame, orient="horizontal", command=tree.xview)
    hsb.pack(side='bottom', fill='x')
    tree.configure(xscrollcommand=hsb.set)
    tree.pack(fill='both', expand=True)

    # Configure Treeview Style 
    style = ttk.Style() 
    style.configure("Treeview", rowheight=25) 
    style.configure("Treeview.Heading", font=('Calibri', 10,'bold')) 
    style.map('Treeview', background=[('selected', 'blue')])

    def clear_treeview():
        for item in tree.get_children():
            tree.delete(item)

    # Reading Data from DB and inserting into Treeview
    def readintotreeview():
        conn = sqlite3.connect('gascylinder.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM inventory;")
        completeRow = cursor.fetchall()

        conn.close()

        clear_treeview()

        # projectsList.delete(0, tk.END)
        tree.tag_configure('low', background='red', foreground='white')
        for record in completeRow:
            # projectsList.insert(tk.END, f'{record[0]}')
            tag = "low" if record[4] < 10 else ""
            tree.insert('', 'end', values=(record[0], record[1], record[2], record[3], record[4], record[5]), tags=(tag,))

    
    readintotreeview()

    def open_new_entry_window():
        new_entry_window = tk.Toplevel(inventory_window)
        new_entry_window.title("New Entry")
        new_entry_window.geometry("550x450")

        headingLabel = tk.Label(new_entry_window, text="New Entry", font=('times new roman', 30, 'bold'), background='gray20', foreground='gold', bd=12, relief=tk.GROOVE)
        headingLabel.pack(fill=tk.X, pady=5)

        # Create form labels and entries
        newentryFrame = tk.Frame(new_entry_window, background='gray20', bd=8, relief=tk.GROOVE)
        newentryFrame.pack(fill=tk.X, pady=5)
        
        tk.Label(newentryFrame, text="Item Name",font=('times new roman',15,'bold'),background='gray20',foreground='white').grid(row=0, column=0, padx=10, pady=5)
        medicine_name_entry = tk.Entry(newentryFrame,font=('arial',15),bd=7,width=18)
        medicine_name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(newentryFrame, text="Batch No",font=('times new roman',15,'bold'),background='gray20',foreground='white').grid(row=2, column=0, padx=10, pady=5)
        batch_no_entry = tk.Entry(newentryFrame,font=('arial',15),bd=7,width=18)
        batch_no_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(newentryFrame, text="Quantity",font=('times new roman',15,'bold'),background='gray20',foreground='white').grid(row=3, column=0, padx=10, pady=5)
        quantity_entry = tk.Entry(newentryFrame,font=('arial',15),bd=7,width=18)
        quantity_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(newentryFrame, text="Purchased Price",font=('times new roman',15,'bold'),background='gray20',foreground='white').grid(row=4, column=0, padx=10, pady=5)
        price_entry = tk.Entry(newentryFrame,font=('arial',15),bd=7,width=18)
        price_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(newentryFrame, text="Purchased Date (YYYY-MM-DD)",font=('times new roman',15,'bold'),background='gray20',foreground='white').grid(row=1, column=0, padx=10, pady=5)
        expiry_entry = tk.Entry(newentryFrame,font=('arial',15),bd=7,width=18)
        expiry_entry.grid(row=1, column=1, padx=10, pady=5)

        # Function to insert data into database
        def add_entry():
            conn = sqlite3.connect('gascylinder.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO inventory (item_name,  batch_no, quantity, price, expiry)
                VALUES (?, ?, ?, ?, ?)
            ''', (medicine_name_entry.get(), expiry_entry.get(), batch_no_entry.get(), quantity_entry.get(), price_entry.get()))
            conn.commit()
            new_id = cursor.lastrowid
            conn.close()
            # Insert new data into Treeview 
            # tree.insert('', 'end', values=(new_id, medicine_name_entry.get(), expiry_entry.get(), batch_no_entry.get(), quantity_entry.get(), price_entry.get()))
            # readintotreeview() 
            # readitems()
            new_entry_window.destroy()

        # Add submit button
        submit_button = tk.Button(newentryFrame, text="Submit", font=('arial', 16, 'bold'), background="gray20", foreground='white', bd=5, width=8, pady=10,command=add_entry)
        submit_button.grid(row=5, column=0, columnspan=2, pady=10)

    # Add edit, delete, update buttons
    def edit_item():
        pass  # Add your logic here

    # def delete_item():
    #     pass  # Add your logic here
    def delete_item():
        selected_item = tree.selection()[0]  # Get selected item
        item_values = tree.item(selected_item, 'values')  # Get values of the selected item
        item_id = item_values[0]  # Assuming 'id' is the first value in the tuple

        conn = sqlite3.connect('medicspharmacy.db')
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM inventory WHERE id = ?
        ''', (item_id,))
        conn.commit()
        conn.close()

        # tree.delete(selected_item)  # Remove the item from Treeview
        # readintotreeview()
        # readitems()


    # def update_item():
    #     pass  # Add your logic here

    def update_item():
        selected_item = tree.selection()[0]
        values = tree.item(selected_item, 'values')

        update_window = tk.Toplevel(inventory_window)
        update_window.title("Update Entry")
        update_window.geometry("450x420")

        headingLabel = tk.Label(update_window, text="Edit", font=('times new roman', 30, 'bold'), background='gray20', foreground='gold', bd=12, relief=tk.GROOVE)
        headingLabel.pack(fill=tk.X, pady=5)

        # Create form labels and entries
        editentryFrame = tk.Frame(update_window, background='gray20', bd=8, relief=tk.GROOVE)
        editentryFrame.pack(fill=tk.X, pady=5)

        tk.Label(editentryFrame, text="Medicine Name", font=('times new roman',15,'bold'),background='gray20',foreground='white').grid(row=0, column=0, padx=10, pady=5)
        med_name_entry = tk.Entry(editentryFrame,font=('arial',15),bd=7,width=18)
        med_name_entry.grid(row=0, column=1, padx=10, pady=5)
        med_name_entry.insert(0, values[1])

        tk.Label(editentryFrame, text="Expiry", font=('times new roman',15,'bold'),background='gray20',foreground='white').grid(row=1, column=0, padx=10, pady=5)
        expiry_entry = tk.Entry(editentryFrame,font=('arial',15),bd=7,width=18)
        expiry_entry.grid(row=1, column=1, padx=10, pady=5)
        expiry_entry.insert(0, values[2])

        tk.Label(editentryFrame, text="Batch No", font=('times new roman',15,'bold'),background='gray20',foreground='white').grid(row=2, column=0, padx=10, pady=5)
        batch_no_entry = tk.Entry(editentryFrame,font=('arial',15),bd=7,width=18)
        batch_no_entry.grid(row=2, column=1, padx=10, pady=5)
        batch_no_entry.insert(0, values[3])

        tk.Label(editentryFrame, text="Quantity", font=('times new roman',15,'bold'),background='gray20',foreground='white').grid(row=3, column=0, padx=10, pady=5)
        quantity_entry = tk.Entry(editentryFrame,font=('arial',15),bd=7,width=18)
        quantity_entry.grid(row=3, column=1, padx=10, pady=5)
        quantity_entry.insert(0, values[4])

        tk.Label(editentryFrame, text="Price", font=('times new roman',15,'bold'),background='gray20',foreground='white').grid(row=4, column=0, padx=10, pady=5)
        price_entry = tk.Entry(editentryFrame,font=('arial',15),bd=7,width=18)
        price_entry.grid(row=4, column=1, padx=10, pady=5)
        price_entry.insert(0, values[5])

        def save_changes():
            conn = sqlite3.connect('medicspharmacy.db')
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE inventory
                SET medicine_name=?, expiry=?, batch_no=?, quantity=?, price=?
                WHERE id=?
            ''', (med_name_entry.get(), expiry_entry.get(), batch_no_entry.get(), quantity_entry.get(), price_entry.get(), values[0]))
            conn.commit()
            conn.close()

            # Update Treeview
            # tree.item(selected_item, values=(values[0], med_name_entry.get(), expiry_entry.get(), batch_no_entry.get(), quantity_entry.get(), price_entry.get()))
            # readintotreeview()
            # readitems()
            update_window.destroy()

        tk.Button(editentryFrame, text="Save", font=('arial', 12, 'bold'), background="gray20", foreground='white', bd=5, width=8, pady=10,command=save_changes).grid(row=5, column=0, columnspan=2, pady=10)






    inventorybuttonFrame = tk.Frame(inventory_window, background='gray20', bd=8, relief=tk.GROOVE)
    inventorybuttonFrame.pack(fill=tk.X, pady=5)

    # Buttons
    add_button = tk.Button(inventorybuttonFrame, text="New Entry", font=('arial', 16, 'bold'), background="gray20", foreground='white', bd=5, width=8, pady=10, command=open_new_entry_window)
    add_button.pack(side='left')

    edit_button = tk.Button(inventorybuttonFrame, text="Edit", font=('arial', 16, 'bold'), background="gray20", foreground='white', bd=5, width=8, pady=10, command=edit_item)
    edit_button.pack(side='left')

    delete_button = tk.Button(inventorybuttonFrame, text="Delete", font=('arial', 16, 'bold'), background="gray20", foreground='white', bd=5, width=8, pady=10, command=delete_item)
    delete_button.pack(side='left')

    update_button = tk.Button(inventorybuttonFrame, text="Update", font=('arial', 16, 'bold'), background="gray20", foreground='white', bd=5, width=8, pady=10, command=update_item)
    update_button.pack(side='left')

    print_button = tk.Button(inventorybuttonFrame, text="Print", font=('arial', 16, 'bold'), background="gray20", foreground='white', bd=5, width=8, pady=10, command=update_item)
    print_button.pack(side='left')







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

inventory_button = tk.Button(button_frame, text="Manage Inventory", font=('Helvetica', 14), bg='gray30', fg='white', command=open_inventory_window)
inventory_button.pack(side='left', padx=10)

sales_button = tk.Button(button_frame, text="Record Sales", font=('Helvetica', 14), bg='gray30', fg='white')
sales_button.pack(side='left', padx=10)

settings_button = tk.Button(button_frame, text="Settings", font=('Helvetica', 14), bg='gray30', fg='white')
settings_button.pack(side='left', padx=10)

root.mainloop()
