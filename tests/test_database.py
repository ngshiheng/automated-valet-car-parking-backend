import unittest

from lib.database import VehicleType, create_parking_lot


class TestDatabaseCRUD(unittest.TestCase):
    def test_create_parking_lot(self) -> None:
        parking_lot = create_parking_lot(VehicleType.CAR, 5)
        self.assertEqual(len(parking_lot), 5)
        self.assertDictEqual(
            parking_lot, {
                "CarLot1": None,
                "CarLot2": None,
                "CarLot3": None,
                "CarLot4": None,
                "CarLot5": None,
            },
        )


if __name__ == "__main__":
    unittest.main()
