
class ComplexNumbers:
    def __init__(self,im,re):
        self.__im = im*1j
        self.__re = re

    @property
    def im(self):
        return self.__im

    @im.setter
    def im(self, im):
        self.__im = im

    @im.getter
    def im(self):
        return self.__im

    @property
    def re(self):
        return self.__re

    @re.setter
    def im(self, re):
        self.__re = re

    @re.getter
    def im(self):
        return self.__re

    def __add__(self, other):
        return self.__im + other.__im + self.__re + other.__re

    def __sub__(self, other):
        return self.__im - other.__im + self.__re - other.__re

    def __str__(self):
        return str(self.__re + self.__im)

z1 = ComplexNumbers(1,3)
z2 = ComplexNumbers(3,-1)
print(z1)
print(z2)
print(z1+z2)
print(z1-z2)

