"""Functions for calculating steps in exchanging currency."""

def exchange_money(budget, exchange_rate):
    """Calculate estimated value after exchange."""
    return float(budget) / float(exchange_rate)


def get_change(budget, exchanging_value):
    """Calculate currency left after an exchange."""
    return float(budget) - float(exchanging_value)


def get_value_of_bills(denomination, number_of_bills):
    """Calculate the total value of currency at current denomination."""
    return int(denomination) * int(number_of_bills)


def get_number_of_bills(amount, denomination):
    """Calculate the number of currency units (bills) within the amount."""    
    return int(float(amount) // int(denomination))


def get_leftover_of_bills(amount, denomination):
    """Calculate leftover amount after exchanging into bills."""    
    return float(amount) % int(denomination)


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Calculate the maximum value of the new currency."""
    actual_rate = exchange_rate * (1 + spread / 100)
    total_currency = budget / actual_rate
    get_number_of_bills = total_currency // denomination
    return int(get_number_of_bills * denomination)
