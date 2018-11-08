from point import *

a = [(0, 0), (3, 0), (4, 0)]

if Point.ori(Point(*a[0]), Point(*a[1]), Point(*a[2])) == 1:
    print("Pozitivne")
elif Point.ori(Point(*a[0]), Point(*a[1]), Point(*a[2])) == 0:
    print("Negativno")
else:
    print("Kolirenarne")
