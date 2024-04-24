#Aplikacja do nauki Pythona




#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/



# Zmienne liczbowe
x = 7
print('x is {}'.format(x))
print(type(x))

# Zmienne tekstowe

x1 = 'After seven is "{0}" "{1}"'.format(8, 90)

x2 = 'after seven is "{1:<09}" "{0:>09}"'.format(8, 90)

x3 = 'after seven is "{1:<09}" "{0:>09}"'.format(23458, 90)
print('x1 is {}'.format(x1))
print('x2 is {}'.format(x2))
print('x3 is {}'.format(x3))

a = 3
b = 234
x4 = f'Liczba {b} jest większa od {a}'
print(x4)

print(type(x))
