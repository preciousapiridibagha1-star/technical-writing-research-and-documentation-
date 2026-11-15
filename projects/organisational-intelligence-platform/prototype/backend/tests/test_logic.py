import unittest

from main import PROGRAMMES, SECTORS, find_programme, progress_percent


class PrototypeLogicTests(unittest.TestCase):
    def test_three_initial_sector_configurations_exist(self):
        self.assertEqual(
            set(SECTORS.keys()),
            {"public-health", "health-organisations", "education"},
        )

    def test_each_sector_has_a_synthetic_programme(self):
        for sector in SECTORS:
            self.assertEqual(find_programme(sector)["sector"], sector)

    def test_progress_is_calculated_deterministically(self):
        indicator = {"target": 100, "actual": 75}
        self.assertEqual(progress_percent(indicator), 75.0)

    def test_missing_actual_value_has_no_percentage(self):
        indicator = {"target": 100, "actual": None}
        self.assertIsNone(progress_percent(indicator))

    def test_progress_is_not_capped_at_one_hundred(self):
        indicator = {"target": 100, "actual": 125}
        self.assertEqual(progress_percent(indicator), 125.0)


if __name__ == "__main__":
    unittest.main()
