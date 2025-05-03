import tkinter as tk
from tkinter import ttk, messagebox

# Hardcoded exchange rates (Base: USD)
exchange_rates = {
    "USD": {"INR": 75.0, "EUR": 0.85, "GBP": 0.75, "AUD": 1.35, "CAD": 1.25},
    "INR": {"USD": 0.013, "EUR": 0.011, "GBP": 0.010, "AUD": 0.018, "CAD": 0.017},
    "EUR": {"USD": 1.18, "INR": 88.24, "GBP": 0.88, "AUD": 1.59, "CAD": 1.47},
    "GBP": {"USD": 1.33, "INR": 100.0, "EUR": 1.14, "AUD": 1.80, "CAD": 1.67},
    "AUD": {"USD": 0.74, "INR": 55.56, "EUR": 0.63, "GBP": 0.56, "CAD": 0.93},
    "CAD": {"USD": 0.80, "INR": 60.0, "EUR": 0.68, "GBP": 0.60, "AUD": 1.08},
}

# Function to perform currency conversion
def convert_currency():
    try:
        from_currency = currency_from.get()
        to_currency = currency_to.get()
        amount = float(entry_amount.get())

        if from_currency == to_currency:
            messagebox.showerror("Input Error", "Currencies must be different.")
            return

        # Fetching the exchange rate
        rate = exchange_rates[from_currency].get(to_currency)
        if rate:
            result = amount * rate
            result_label.config(text=f"Converted Amount: {to_currency} {result:.2f}")
        else:
            messagebox.showerror("Error", f"Conversion rate not available for {from_currency} to {to_currency}.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid numeric value for the amount.")

# Set up the main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x400")
root.config(bg="#f7f7f7")

# Title
tk.Label(root, text="💰 Currency Converter", font=("Helvetica", 18, "bold"), bg="#f7f7f7").pack(pady=20)

# Currency Selection
tk.Label(root, text="From Currency:", font=("Helvetica", 12), bg="#f7f7f7").pack()
currency_from = ttk.Combobox(root, values=["USD", "INR", "EUR", "GBP", "AUD", "CAD"], width=20)
currency_from.set("USD")
currency_from.pack(pady=5)

tk.Label(root, text="To Currency:", font=("Helvetica", 12), bg="#f7f7f7").pack()
currency_to = ttk.Combobox(root, values=["USD", "INR", "EUR", "GBP", "AUD", "CAD"], width=20)
currency_to.set("INR")
currency_to.pack(pady=5)

# Amount Entry
tk.Label(root, text="Amount:", font=("Helvetica", 12), bg="#f7f7f7").pack()
entry_amount = tk.Entry(root, font=("Helvetica", 12), width=20)
entry_amount.pack(pady=5)

# Convert Button
tk.Button(root, text="Convert", font=("Helvetica", 14), bg="#4CAF50", fg="white", command=convert_currency).pack(pady=20)

# Result Label
result_label = tk.Label(root, text="Converted Amount: ", font=("Helvetica", 14), bg="#f7f7f7")
result_label.pack(pady=10)

# Run the application
root.mainloop()
