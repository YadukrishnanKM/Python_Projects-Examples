import numpy as np


class Imperial:

    arr = np.array([], dtype=float)

    def __init__(self, *values: float):

        global arr

        lst = []

        for i in (values):
            lst.append(i)

        arr = np.array(lst, dtype=float)

        pass

    class pounds:

        global arr

        def ounce(self):
            for i in range(len(arr)):
                arr[i] = arr[i]*(16)
            return arr

        def ton(self):
            for i in range(len(arr)):
                arr[i] = arr[i]/(2240)
            return arr

    class ton:
        global arr

        def ounce(self):
            for i in range(len(arr)):
                arr[i] = arr[i]*(16*2240)
            return arr

        def pounds(self):
            for i in range(len(arr)):
                arr[i] = arr[i]*(2240)
            return arr

    class ounce:
        def tone(self):
            for i in range(len(arr)):
                arr[i] = arr[i]/(16*2240)
            return arr

        def pounds(self):
            for i in range(len(arr)):
                arr[i] = arr[i]/(16)
            return arr

    class mile:
        def yard(self):
            for i in range(len(arr)):
                arr[i] = arr[i]*(1760)
            return arr

        def nautical_mile(self):
            for i in range(len(arr)):
                arr[i] = arr[i]*(0.86897624)
            return arr

    class yard:
        def mile(self):
            for i in range(len(arr)):
                arr[i] = arr[i]/(1760)
            return arr

        def nautical_mile(self):
            for i in range(len(arr)):
                arr[i] = arr[i]*(0.00049374)
            return arr

    class nautical_mile:
        def mile(self):
            for i in range(len(arr)):
                arr[i] = arr[i]*(1.15077945)
            return arr

        def yard(self):
            for i in range(len(arr)):
                arr[i] = arr[i]*(2025.37183)
            return arr


class Matrics:

    arr = np.array([], dtype=float)

    def __init__(self, *values: float):

        global arr

        lst = []

        for i in (values):
            lst.append(i)

        arr = np.array(lst, dtype=float)
        self.kilo_gram = self.kilo_gram()
        self.gram = self.gram()
        self.milli_gram = self.milli_gram()
        self.kilo_meter = self.kilo_meter()
        self.meter = self.meter()
        self.milli_meter = self.milli_meter()

    class kilo_gram:

        global arr

        def __init__(self):
            self.arr = arr

        def gram(self):
            for i in range(len(arr)):
                arr[i] = arr[i]*(1000)
            return arr

        def milli_gram(self):
            for i in range(len(arr)):
                arr[i] = arr[i]*(10**6)
            return arr

    class gram:

        def __init__(self):
            self.arr = arr
        global arr

        def kilo_gram(self):
            for i in range(len(arr)):
                arr[i] = arr[i]*(1/1000)
            return arr

        def milli_gram(self):
            for i in range(len(arr)):
                arr[i] = arr[i]*(1000)
            return arr

    class milli_gram:

        def __init__(self):
            self.arr = arr

        def kilo_gram(self):
            for i in range(len(arr)):
                arr[i] = arr[i]/(10**6)
            return arr

        def gram(self):
            for i in range(len(arr)):
                arr[i] = arr[i]/(10**3)
            return arr

    class kilo_meter:

        def __init__(self):
            self.arr = arr

        def meter(self):
            for i in range(len(arr)):
                arr[i] = arr[i]*(1000)
            return arr

        def milli_meter(self):
            for i in range(len(arr)):
                arr[i] = arr[i]*(10**6)
            return arr

    class meter:

        def __init__(self):
            self.arr = arr

        def kilo_meter(self):
            for i in range(len(arr)):
                arr[i] = arr[i]/(1000)
            return arr

        def milli_meter(self):
            for i in range(len(arr)):
                arr[i] = arr[i]*(1000)
            return arr

    class milli_meter:

        def __init__(self):
            self.arr = arr

        def kilo_meter(self):
            for i in range(len(arr)):
                arr[i] = arr[i]/(10**6)
            return arr

        def meter(self):
            for i in range(len(arr)):
                arr[i] = arr[i]/(10**3)
            return arr
