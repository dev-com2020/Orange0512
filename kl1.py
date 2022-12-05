from abc import ABC, abstractmethod


class Ptak(ABC):
    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lataj(self):
        print(f"Tu {self.gatunek} startuje i osiągam prędkość {self.szybkosc}")

    def gniazdo(self):
        print(f"Tu {self.gatunek} tworzę gniazdo")

    @abstractmethod
    def wydajOdglos(self):
        pass


class Orzel(Ptak):
    def poluj(self):
        print(f"Tu {self.gatunek} startuje i rozpoczynam polowanie")

    def gniazdo(self):
        print(f"Tu {self.gatunek} tworzę gniazdo i będę spał")

    def wydajOdglos(self):
        print("piiiiiiii")


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 1)

    def lataj(self):
        print(f"Tu {self.gatunek} ja nie latam :(")

    def wydajOdglos(self):
        print("kokoko")


# p1 = Ptak('wróbel', 10)
p2 = Orzel('bielik', 100)
p3 = Kura('kura')
# p1.lataj()
p2.poluj()
p3.lataj()
print(p3.gatunek)
p3.wydajOdglos()
p3.gniazdo()
print(Kura.mro())
