class Brand(object):
    def __init__(self, bname, mo):
        self.bname = bname
        self.mo = mo

    # Parent class 2


class Mseries(object):
    def __init__(self, m, price):
        self.m = m
        self.price = price
    # Deriving a child class from the two parent classes


class B(Brand, Mseries):
    def __init__(self, bname, mo, m, price, warr):
        self.warr = warr
        Brand.__init__(self, bname, mo)
        Mseries.__init__(self, m, price)
        print("Brand Name: {}, Model: {}, Price: {}, Warranty: {}".format(self.bname, self.m, self.price, self.warr))


H = B('Samsung','M-series', 'M30', 15000, '2 years')