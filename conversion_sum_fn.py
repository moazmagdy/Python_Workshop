"""
This script will describe a function that takes a list of USD amounts, converts them into EGP and then sum
the results.
"""
def convert_usd_to_egp(amount, rate = 18.65):
    return amount * rate
    
def convert_and_sum_list(usd_list, rate= 18.65):
    total = 0
    for amount in usd_list:
        total += convert_usd_to_egp(amount, rate)
    return total
print(convert_and_sum_list([1, 3]))