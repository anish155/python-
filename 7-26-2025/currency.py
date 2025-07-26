currency_map = {
    "Nepal": "NPR",
    "USA": "USD",
    "India": "INR",
    "Japan": "JPY",
    "UK": "GBP",
    "France": "EUR"
}


exchange_rates = {
    "USD": 1.0,
    "NPR": 133.5,
    "INR": 83.1,
    "JPY": 155.7,
    "GBP": 0.77,
    "EUR": 0.92
}

def convert_currency():
    from_country = input("Convert from country: ")
    to_country = input("Convert to country: ")
    amount = float(input("Enter amount: "))

   
    from_currency = currency_map.get(from_country)
    to_currency = currency_map.get(to_country)

    if not from_currency or not to_currency:
        print("Invalid country provided.")
        return

    
    amount_in_usd = amount / exchange_rates[from_currency]
    converted_amount = amount_in_usd * exchange_rates[to_currency]

    print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

convert_currency()
