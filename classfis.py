class BesaranTurunan:
    def __init__(self):
        pass

    def Luas(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
        self.luas = self.panjang * self.lebar
        return self.luas

    def Volume(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.vol = self.panjang * self.lebar * self.tinggi
        return self.vol

    def MassaJenis(self, massa, volume):
        self.massa = massa
        self.volume = volume
        self.den = self.massa / self.volume
        return self.den

    def Kecepatan(self, perpindahan, waktu):
        self.perpindahan = perpindahan
        self.waktu = waktu
        self.vel = self.perpindahan / self.waktu
        return self.vel

    def Percepatan(self, kecepatan, waktu):
        self.kecepatan = kecepatan
        self.waktu = waktu
        self.acce = self.kecepatan / self.waktu
        return self.acce

    def Gaya(self, massa, percepatan):
        self.massa = massa
        self.percepatan = percepatan
        self.gaya = self.massa * self.percepatan
        return self.gaya

    def Usaha(self, gaya, perpindahan):
        self.gaya = gaya
        self.perpindahan = perpindahan
        self.usaha = self.gaya * self.perpindahan
        return self.usaha

    def Daya(self, usaha, waktu):
        self.usaha = usaha
        self.waktu = waktu
        self.daya = self.usaha * self.waktu
        return self.daya

    def Tekanan(self, gaya, luas):
        self.gaya = gaya
        self.luas = luas
        self.press = self.gaya / self.luas
        return self.press

    def Momentum(self, massa, kecepatan):
        self.massa = massa
        self.kecepatan = kecepatan
        self.mom = self.massa * self.kecepatan
        return self.mom
