class samochód:

    def __init__(self):

        self.__silnik = False
        self.__bieg = 0
        self.__prędkość = 0

    def uruchom(self):
        self.__silnik = True

    def wyłącz(self):
        self.__silnik = False

    def __biegNastępny(self):
        if self.__bieg <= 6: self.__bieg += 1; print(self.__bieg)

    def __biegPoprzedni(self):
        if self.__bieg >= 0: self.__bieg -= 1; print(self.__bieg)

    def przyspiesz(self):
        if self.__silnik == True:
            self.__prędkość += 10
            self.__biegNastępny()
            print(self.__prędkość)


    def hamuj(self):
        if self.__prędkość >= 10:
            self.__prędkość -= 10
        else:
            self.__prędkość = 0
        self.__biegPoprzedni()
        print(self.__prędkość)



c1 = samochód()
c1.uruchom()
c1.przyspiesz()
c1.przyspiesz()
# c1.__bieg = 100
# c1.__prędkość = "10000000"
# c1.__prędkość = 432434324244234
c1.hamuj()
c1.hamuj()
c1.wyłącz()
