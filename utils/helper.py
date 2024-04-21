def format_currency(amount, currency):
    if currency == "VND":
        # Format the amount for VND, no decimal places
        return "{:,.0f}".format(amount)
    elif currency == "USDT":
        # Format the amount for USDT, two decimal places
        return "{:,.2f}".format(amount)
    else:
        # Default formatting if currency is not recognized
        return "{:,.2f}".format(amount)
