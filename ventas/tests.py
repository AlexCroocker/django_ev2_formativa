from decimal import Decimal
from django.test import SimpleTestCase
from .admin import formatear_pesos_chilenos


class FormatearPesosChilenosTests(SimpleTestCase):
	def test_formatea_miles_sin_decimales(self):
		self.assertEqual(formatear_pesos_chilenos(Decimal("12990.00")), "$12.990")
