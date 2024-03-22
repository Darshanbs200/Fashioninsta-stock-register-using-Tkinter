import tkinter as tk
from tkinter import ttk

class Fashionista:
    def __init__(self):
        self.store_inventory = {
            'men': [],
            'women': [],
            'children': []
        }

    def add_garment(self, section, garment):
        self.store_inventory[section].append(garment)

    def update_stock(self, garment_id, new_quantity):
        for section in self.store_inventory.values():
            for garment in section:
                if garment['id'] == garment_id:
                    garment['stock'] = new_quantity
                    break

    def calculate_sales(self, section):
        total_sales = 0
        for garment in self.store_inventory[section]:
            total_sales += garment['sales']
        return total_sales

    def generate_report(self, section):
        report = ''
        for garment in self.store_inventory[section]:
            report += f"Type: {garment['type']}, Price: ${garment['price']}, Stock: {garment['stock']}, Sales: {garment['sales']}\n"
        return report

class FashionistaGUI:
    def __init__(self, master):
        self.master = master
        master.title("Fashionista")

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#FFFFFF')  # Background color for the frame
        self.fashionista = Fashionista()

        # Section selection
        self.section_label = tk.Label(master, text="Select Section:")
        self.section_label.grid(row=0, column=0)
        self.section_var = tk.StringVar(master)
        self.section_var.set("men")
        self.section_menu = tk.OptionMenu(master, self.section_var, "men", "women", "children")
        self.section_menu.grid(row=0, column=1)

        # Garment details entry
        self.details_frame = ttk.Frame(master)
        self.details_frame.grid(row=1, column=0, columnspan=2, pady=10)

        self.type_label = tk.Label(self.details_frame, text="Garment Types:")
        self.type_label.grid(row=0, column=0)
        self.type_entry = tk.Entry(self.details_frame)
        self.type_entry.grid(row=0, column=1)

        self.price_label = tk.Label(self.details_frame, text="Price:")
        self.price_label.grid(row=1, column=0)
        self.price_entry = tk.Entry(self.details_frame)
        self.price_entry.grid(row=1, column=1)

        self.stock_label = tk.Label(self.details_frame, text="Stock Quantity:")
        self.stock_label.grid(row=2, column=0)
        self.stock_entry = tk.Entry(self.details_frame)
        self.stock_entry.grid(row=2, column=1)

        self.sales_label = tk.Label(self.details_frame, text="Sales:")
        self.sales_label.grid(row=3, column=0)
        self.sales_entry = tk.Entry(self.details_frame)
        self.sales_entry.grid(row=3, column=1)

        # Buttons
        self.buttons_frame = ttk.Frame(master)
        self.buttons_frame.grid(row=2, column=0, columnspan=2, pady=10)

        self.add_button = tk.Button(self.buttons_frame, text="Add Garment", command=self.add_garment)
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        self.update_button = tk.Button(self.buttons_frame, text="Update Stock", command=self.update_stock)
        self.update_button.grid(row=0, column=1, padx=5, pady=5)

        self.sales_button = tk.Button(self.buttons_frame, text="Calculate Sales", command=self.calculate_sales)
        self.sales_button.grid(row=0, column=2, padx=5, pady=5)

        self.report_button = tk.Button(self.buttons_frame, text="Generate Report", command=self.generate_report)
        self.report_button.grid(row=0, column=3, padx=5, pady=5)

        # Listbox for inventory display
        self.inventory_label = tk.Label(master, text="Inventory:")
        self.inventory_label.grid(row=3, column=0, sticky=tk.W, padx=10)
        self.inventory_listbox = tk.Listbox(master, width=50)
        self.inventory_listbox.grid(row=4, column=0, rowspan=2, padx=10)

        # Listbox for report display
        self.report_label = tk.Label(master, text="Report:")
        self.report_label.grid(row=3, column=1, sticky=tk.W, padx=10)
        self.report_listbox = tk.Listbox(master, width=50)
        self.report_listbox.grid(row=4, column=1, rowspan=2, padx=10)

    def add_garment(self):
        section = self.section_var.get()
        garment = {
            'id': len(self.fashionista.store_inventory[section]) + 1,
            'type': self.type_entry.get(),
            'price': float(self.price_entry.get()),
            'stock': int(self.stock_entry.get()),
            'sales': int(self.sales_entry.get())
        }
        self.fashionista.add_garment(section, garment)
        self.update_inventory_listbox()

    def update_stock(self):
        garment_id = int(self.type_entry.get())
        new_quantity = int(self.stock_entry.get())
        self.fashionista.update_stock(garment_id, new_quantity)
        self.update_inventory_listbox()

    def calculate_sales(self):
        section = self.section_var.get()
        total_sales = self.fashionista.calculate_sales(section)
        self.report_listbox.delete(0, tk.END)
        self.report_listbox.insert(tk.END, f"Total sales for {section} section: ${total_sales}")

    def generate_report(self):
        section = self.section_var.get()
        for garment in self.fashionista.store_inventory[section]:
            report = f"Type: {garment['type']}, Price: ${garment['price']}, Stock: {garment['stock']}, Sales: {garment['sales']}"
            self.report_listbox.insert(tk.END, report)

    def update_inventory_listbox(self):
        section = self.section_var.get()
        self.inventory_listbox.delete(0, tk.END)
        for garment in self.fashionista.store_inventory[section]:
            self.inventory_listbox.insert(tk.END, f"ID: {garment['id']}, Type: {garment['type']}, Price: ${garment['price']}, Stock: {garment['stock']}, Sales: {garment['sales']}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = FashionistaGUI(root)
    root.mainloop()
