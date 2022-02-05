#задал  параметры в edit configuration

from sys import argv
scriptname, time, money, prem = argv

print((int(time) * int(money)) + int(prem))