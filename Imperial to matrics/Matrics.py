''' 
    from matrics to imperial 
    kg l sq_m
'''


import numpy as np


class length:

    arr = np.array([])

    def __init__(self, *values: float):

        lst = []

        for i in values:
            lst.append(i)

        global arr
        arr = np.array(lst, dtype=float)

    def meter(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*9.37007874  # inch
        return arr

    def centi_meter(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*(39.37007874/100)  # inches

        return arr

    def milli_meter(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*(39.37007874/1000)  # inches

        return arr

    def nano_meter(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*(39.37007874/(10**-9))  # inches

        return arr

    def micro_meter(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*(39.37007874/(10**-6))  # inches

        return arr

    def kilo_meter(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*(39.37007874*1000)  # inches

        return arr


class volume:
    arr = np.array([])

    def __init__(self, *values: float):

        lst = []

        for i in values:
            lst.append(i)

        global arr
        arr = np.array(lst, dtype=float)

    def liter(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*0.2641720524  # gallon

        return arr

    def milli_liter(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*(0.2641720524/1000)  # gallon

        return arr

    def centimeter_cube(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*(0.00021997)  # gallon

        return arr


class mass:  # lbs
    arr = np.array([])

    def __init__(self, *values: float):

        lst = []

        for i in values:
            lst.append(i)

        global arr
        arr = np.array(lst, dtype=float)

    def kilo_gram(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*2.20462262

        return arr

    def gram(self):
        for items in range(len(arr)):
            arr[items] = arr[items]*(0.00220462)

        return arr
