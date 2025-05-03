# Currency-Converter
# 💰 Currency Converter (Python + Tkinter)

A simple and interactive **Currency Converter** built using **Python** and **Tkinter**. This app allows users to convert between multiple currencies based on **predefined exchange rates**.

---

## 🚀 Features

- Convert between multiple currencies (USD, INR, EUR, GBP, AUD, CAD).
- **Hardcoded Exchange Rates**: No need for an external API, everything is predefined.
- Easy-to-use GUI with a simple and intuitive design.
- **Real-time result display** with an option to input the amount and select source/destination currency.

---

## 🖥️ Tech Stack

- **Programming Language**: Python 3.x
- **GUI Library**: Tkinter (Standard Python Library)

No external libraries are required.

---

## 📦 Requirements

- **Python 3.x** (Download from [python.org](https://www.python.org/downloads/))
- Tkinter (pre-installed with Python)

---

## ▶️ How to Run

1. **Clone or Download** this repository.
2. Open a terminal or command prompt in the project directory.
3. Run the app using the following command:

   ```bash
   python currency_converter.py
## 📁 File Structure

currency-converter/
│
├── currency_converter.py   # Main Python GUI app
├── README.md               # Project documentation
└── assets/                 # (Optional) Folder for any additional assets, like images
## 🔧 How It Works
Hardcoded Exchange Rates: The app uses a dictionary to store exchange rates between a few popular currencies. You can modify these rates manually.

Example of the rates:

exchange_rates = {
    "USD": {"INR": 75.0, "EUR": 0.85, "GBP": 0.75, "AUD": 1.35, "CAD": 1.25},
    "INR": {"USD": 0.013, "EUR": 0.011, "GBP": 0.010, "AUD": 0.018, "CAD": 0.017},
    "EUR": {"USD": 1.18, "INR": 88.24, "GBP": 0.88, "AUD": 1.59, "CAD": 1.47},
    "GBP": {"USD": 1.33, "INR": 100.0, "EUR": 1.14, "AUD": 1.80, "CAD": 1.67},
    "AUD": {"USD": 0.74, "INR": 55.56, "EUR": 0.63, "GBP": 0.56, "CAD": 0.93},
    "CAD": {"USD": 0.80, "INR": 60.0, "EUR": 0.68, "GBP": 0.60, "AUD": 1.08},
}
The user inputs the amount and selects the from and to currencies. The conversion is performed using the predefined rates and the result is displayed instantly.

## ✨ Preview

(Replace this with a real screenshot if desired)

## 💡 Customization Ideas
Add more currencies to the converter.

Update the exchange rates manually when needed.

Add an option to save the results to a file (CSV, Excel).

Convert this app to a web version using Flask or Django.

Enhance the user interface for better design.
