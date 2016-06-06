from django.test import TestCase
from .models import ElectricalConductivity, Temperature


class ElectricalConductivityTestCase(TestCase):
    def setUp(self):
        ElectricalConductivity.objects.create(electrical_conductivity=13.4)

    def test_time_created_exists(self):
        ec_test = ElectricalConductivity.objects.get(
                electrical_conductivity=13.4)
        self.assertEqual(ec_test.time_collected, not None)

    def test_electrical_conductivity_saves_number(self):
        ec_test = ElectricalConductivity.objects.get(
                electrical_conductivity=13.4)
        self.assertEqual(ec_test, 13.4)


class TemperatureTestCase(TestCase):
    def setUp(self):
        Temperature.objects.create(temperature=23.2)

    def test_time_created_exists(self):
        temp_test = Temperature.objects.get(temperature=23.2)
        self.assertEqual(temp_test.time_collected, not None)

    def test_temperature_saves_number(self):
        temp_test = Temperature.objects.get(temperature=23.2)
        self.assertEqual(temp_test, 23.2)
