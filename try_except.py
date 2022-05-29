x= input('Please, enter a number: ')
try:
    istr = int(x)
except:
    istr = -1

if abs(istr) > 0:
    print('Nice work!')
else:
    print('Not a number!')