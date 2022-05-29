xh = input('Please enter hours: ')
xr = input('Please enter rate: ')
try:
    hours = float(xh)
    rate = float(xr)
    pay = hours * rate * 1.5
    print('Your pay is: $', pay)
except:
    print('Enter numeric values!')
