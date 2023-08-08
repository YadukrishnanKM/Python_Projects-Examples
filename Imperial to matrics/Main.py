import Imperial as ial
import Matrics as mt
import conversion as co

print('________________________________________\n')
# program to convert the Imperial yards to m
u = ial.length(123.7, 1, 6.784)
a = u.yard()

for i in range(len(a)):
    print('the yards in meters is %.4f' % a[i])

print('________________________________________\n')

# program to convert Matrics kg to imperial lbs

u = mt.mass(123.7, 1, 6.784)
a = u.kilo_gram()

for i in range(len(a)):
    print('the kg in lbs is %.4f' % a[i])

print('________________________________________\n')

# program to convert km to m

u = co.Matrics(123.7, 1, 6.784)
a = u.kilo_meter.meter()

for i in range(len(a)):
    print('the kilo meter in meters is %.4f' % a[i])


print('________________________________________\n')
