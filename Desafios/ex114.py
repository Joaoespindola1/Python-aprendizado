import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
    print('O site está acessível!')
except:
    print('O site não está acessível no momento')