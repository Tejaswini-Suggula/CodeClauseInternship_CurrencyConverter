exchange_rates = {
    'USD': 1.0,
    'EUR': 0.85,
    'GBP': 0.75,
    'JPY': 110.57,
    'INR': 83.98,
    'CAD': 1.26,
    'AUD': 1.35
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency != 'USD':
        amount_in_usd = amount / exchange_rates[from_currency]
    else:
        amount_in_usd = amount
        
    if to_currency != 'USD':
        converted_amount = amount_in_usd * exchange_rates[to_currency]
    else:
        converted_amount = amount_in_usd

    return converted_amount

def main():
    print("Welcome To The Currency Converter")
    
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the currency to convert from: ").upper()
    to_currency = input("Enter the currency to convert to: ").upper()

    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print("Invalid currency. Please use one of the following: ", ", ".join(exchange_rates.keys()))
        return

    converted_amount = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")

if __name__ == "__main__":
    main()