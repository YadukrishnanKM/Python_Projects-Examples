# from imperial to matrics

import numpy as np


class length:  # m
    arr = np.array([])

    def __init__(self, *values: float):

        lst = []

        for i in values:
            lst.append(i)

        global arr
        arr = np.array(lst, dtype=float)

    def twip(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*0.0000176389

        return arr

    def thou(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*0.0000254

        return arr

    def barleycorn(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*0.0084667

        return arr

    def inch(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*0.0254

        return arr

    def hand(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*0.1016

        return arr

    def foot(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*0.3048

        return arr

    def yard(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*0.9144

        return arr

    def chain(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*20.1168

        return arr

    def furlong(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*201.168

        return arr

    def mile(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*1609.344

        return arr

    def league(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*4828.032

        return arr

    def fathom(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*1.852

        return arr

    def cable(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*185.2

        return arr

    def nautical_mile(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*1852

        return arr

    def link(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*0.201168

        return arr

    def rod(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*5.0292

        return arr

##################################################################################################################


class Area:  # sq_m
    arr = np.array([])

    def __init__(self, *values: float):

        lst = []

        for i in values:
            lst.append(i)

        global arr
        arr = np.array(lst, dtype=float)

    def perch(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*25.29285264

        return arr

    def rood(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*1011.7141056

        return arr

    def acre(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*4046.8564224

        return arr

    def square_mile(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*2589988.110336

        return arr


########################################################################################

class volume:  # ml
    arr = np.array([])

    def __init__(self, *values: float):

        lst = []

        for i in values:
            lst.append(i)

        global arr
        arr = np.array(lst, dtype=float)

    def ounce(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*28.4130625

        return arr

    def gill(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*28.4130625*5

        return arr

    def pint(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*28.4130625*20

        return arr

    def quart(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*28.4130625*40

        return arr

    def gallon(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*28.4130625*160

        return arr


###########################################################################################################

class mass:  # kg
    arr = np.array([])

    def __init__(self, *values: float):

        lst = []

        for i in values:
            lst.append(i)

        global arr
        arr = np.array(lst, dtype=float)

    def grain(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*(0.45359237/7000)

        return arr

    def drachm(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*(0.45359237/256)

        return arr

    def ounce(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*(0.45359237/16)

        return arr

    def pound(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*(0.45359237)

        return arr

    def stone(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*(0.45359237*14)

        return arr

    def quarter(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*(0.45359237*28)

        return arr

    def hundredweight(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*(0.45359237*112)

        return arr

    def ton(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*(0.45359237*2240)

        return arr

    def slug(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*(0.45359237*32.17404856)

        return arr
