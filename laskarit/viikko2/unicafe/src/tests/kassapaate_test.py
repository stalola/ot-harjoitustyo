import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

maukkaasti = 400
edullisesti = 240

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassa_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)


# Luodun kassapäätteen rahamäärä ja myytyjen lounaiden määrä on oikea (rahaa 
# 1000 euroa, lounaita myyty 0)
    def test_luodun_kassan_rahamaara(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_luodun_kassan_lounasmaara(self):
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)

#   Huomaa, että luokka tallentaa rahamäärän sentteinä
# Käteisosto toimii sekä edullisten että maukkaiden lounaiden osalta
#   Jos maksu riittävä: kassassa oleva rahamäärä kasvaa lounaan hinnalla ja 
# vaihtorahan suuruus on oikea
#   Jos maksu on riittävä: myytyjen lounaiden määrä kasvaa

    def test_kateisosto_edullisesti_rahat_riittaa(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + edullisesti)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(vaihtoraha, 300 - edullisesti)

    def test_kateisosto_maukkaasti_rahat_riittaa(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + maukkaasti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(vaihtoraha, 500 - maukkaasti)

#   Jos maksu ei ole riittävä: kassassa oleva rahamäärä ei muutu, kaikki rahat 
# palautetaan vaihtorahana ja myytyjen lounaiden määrässä ei muutosta
    def test_kateisosto_edullisesti_rahat_ei_riita(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_maukkaasti_rahat_ei_riita(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(vaihtoraha, 300)
        self.assertEqual(self.kassapaate.maukkaat, 0)


# seuraavissa testeissä tarvitaan myös Maksukorttia jonka oletetaan toimivan 
# oikein

# Korttiosto toimii sekä edullisten että maukkaiden lounaiden osalta
#   Jos kortilla on tarpeeksi rahaa, veloitetaan summa kortilta ja palautetaan 
# True
    def test_korttiosto_edullisesti_rahat_riittaa(self):
        maksukortti = Maksukortti(300)
        riittaa = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 300 - edullisesti)
        self.assertEqual(riittaa, True)

    def test_korttiosto_maukkaasti_rahat_riittaa(self):
        maksukortti = Maksukortti(500)
        riittaa = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 500 - maukkaasti)
        self.assertEqual(riittaa, True)

#   Jos kortilla on tarpeeksi rahaa, myytyjen lounaiden määrä kasvaa
    def test_korttiosto_lounaiden_maara_kasvaa(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 1)

#   Jos kortilla ei ole tarpeeksi rahaa, kortin rahamäärä ei muutu, myytyjen 
# lounaiden määrä muuttumaton ja palautetaan False
    def test_korttiosto_kortilla_ei_tarpeeksi_rahaa(self):
        maksukortti = Maksukortti(edullisesti - 1)
        riittaa_maukk = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        riittaa_edull = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(riittaa_edull, False)
        self.assertEqual(riittaa_maukk, False)
#   Kassassa oleva rahamäärä ei muutu kortilla ostettaessa
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

# Kortille rahaa ladattaessa kortin saldo muuttuu ja kassassa oleva rahamäärä 
# kasvaa ladatulla summalla
    def test_rahaa_ladattaessa_saldo_ja_rahamaara_muuttuu(self):
        maksukortti = Maksukortti(200)
        talletus = 1000
        self.kassapaate.lataa_rahaa_kortille(maksukortti, talletus)
        self.assertEqual(maksukortti.saldo, 200 + talletus)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + talletus)

    def test_negatiivinen_lataus(self):
        maksukortti = Maksukortti(200)
        talletus = -200
        self.kassapaate.lataa_rahaa_kortille(maksukortti, talletus)
        self.assertEqual(maksukortti.saldo, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        

        