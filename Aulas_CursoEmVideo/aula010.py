n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
m = (n1+n2)/2
print('A sua média é {:.1f}'.format(m))
if m >= 8:
    print('Ótima nota!!!')
if m > 6 and m<8 :
    print('Boa nota!')
if m <= 6 :
    print('Bela bosta!')