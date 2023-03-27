import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

#Kortin saldo alussa oikein
    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

#Rahan lataaminen kasvattaa saldoa oikein
    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(2500)
        self.assertEqual(self.maksukortti.saldo, 3500)

#Rahan ottaminen toimii:
    #Saldo vähenee oikein, jos rahaa on tarpeeksi

    def test_ota_rahaa_vahentaa_saldoa_oikein(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo, 500)    

    #Saldo ei muutu, jos rahaa ei ole tarpeeksi

    def test_ota_rahaa_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        kortti.ota_rahaa(500)

        self.assertEqual(kortti.saldo, 200)

    #Metodi palauttaa True, jos rahat riittivät ja muuten False

    def test_ota_rahaa_ja_rahat_riittaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)
    
    def test_ota_rahaa_ja_rahat_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1100), False)

