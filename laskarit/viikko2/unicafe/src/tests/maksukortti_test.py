import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_luodun_kortin_saldo_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(self.maksukortti.saldo, 1100)

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(self.maksukortti.saldo, 900)

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1100)
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_tulostus_on_oikea(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")