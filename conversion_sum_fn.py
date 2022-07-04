"""
This script will describe a function that takes a list of USD amounts, converts them into EGP and then sum
the results.
"""
def convert_usd_to_egp(amount, rate = 18.65):
    return amount * rate

def convert_and_sum_list_kwargs(usd_list, **kwargs):
    total = 0
    for amount in usd_list:
        total += convert_usd_to_egp(amount, **kwargs)
    return total
print(convert_and_sum_list_kwargs([1, 3], rate= 18.65))