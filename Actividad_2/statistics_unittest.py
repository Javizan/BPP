import statistics
import unittest

# En este script se declara una única clase PruebasUnitarias que contiene diversos métodos para testear las
# funciones definidias en statistics.py siguiendo la librería unittest.

class PruebasUnitarias(unittest.TestCase):
    def test_media(self):
        self.assertEqual(statistics.media([3, 5, 7]), 5)
    def test_moda(self):
        self.assertEqual(statistics.moda([3, 4, 4, 5]), 4)
    def test_mediana(self):
        self.assertEqual(statistics.mediana([1, 2, 3, 4]), 2.5)
    def test_varianza(self):
        self.assertEqual(statistics.varianza([2,4,2,4,2,4]), 1)
    def test_desviacion_tipica(self):
        self.assertEqual(statistics.desviacion_tipica([2,4,2,4,2,4]), 1)
if __name__ == '__main__':
    unittest.main()