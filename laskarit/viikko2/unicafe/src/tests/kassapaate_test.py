import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_luodun_kassan_rahamaara_ja_lounaiden_maara_oikea(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset + self.kassa.maukkaat, 0)

    def test_kassan_rahanmaara_nousee_oikein_edullisten_hinnalla_kun_rahat_riittavat_kateisella(self):
        maksu = self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        self.assertEqual(maksu, 0)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_kassan_rahanmaara_nousee_oikein_edullisten_hinnalla_kun_rahat_eivat_riittavat_kateisella(self):
        maksu = self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(maksu, 200)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_kassan_rahanmaara_nousee_oikein_maukkaiden_hinnalla_kun_rahat_riittavat_kateisella(self):
        maksu = self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
        self.assertEqual(maksu, 0)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_kassan_rahanmaara_nousee_oikein_maukkaiden_hinnalla_kun_rahat_eivat_riittavat_kateisella(self):
        maksu = self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(maksu, 200)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kassan_rahanmaara_nousee_oikein_edullisten_hinnalla_kun_rahat_riittavat_kortilla(self):
        kortti = Maksukortti(240)
        arvo = self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(arvo, True)
        self.assertEqual(kortti.saldo, 0)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_kassan_rahanmaara_nousee_oikein_edullisten_hinnalla_kun_rahat_eivat_riittavat_kortilla(self):
        kortti = Maksukortti(200)
        arvo = self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(arvo, False)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_kassan_rahanmaara_nousee_oikein_maukkaiden_hinnalla_kun_rahat_riittavat_kortilla(self):
        kortti = Maksukortti(400)
        arvo = self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(arvo, True)
        self.assertEqual(kortti.saldo, 0)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_kassan_rahanmaara_nousee_oikein_maukkaiden_hinnalla_kun_rahat_eivat_riittavat_kortilla(self):
        kortti = Maksukortti(200)
        arvo = self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(arvo, False)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_rahan_lataus_kortille_toimii_oikein(self):
        kortti = Maksukortti(1000)
        self.kassa.lataa_rahaa_kortille(kortti, 200)
        self.assertEqual(kortti.saldo, 1200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100200)

    def test_rahan_lataus_kortille_toimii_oikein_kun_summa_negatiivinen(self):
        kortti = Maksukortti(1000)
        self.kassa.lataa_rahaa_kortille(kortti, -200)
        self.assertEqual(kortti.saldo, 1000)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)