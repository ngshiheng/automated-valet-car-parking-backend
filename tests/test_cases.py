import os
import unittest
from io import StringIO
from unittest.mock import patch

from main import event_handler, parse_input_file


class TestAutomatedValetParkingSystems(unittest.TestCase):
    def tearDown(self) -> None:
        os.remove('test_input.txt')
        return super().tearDown()

    def test_parse_input_file_returns_a_list_of_events(self) -> None:
        with open("test_input.txt", "w") as f:
            text_list = [
                "3 4\n",
                "Enter motorcycle SGX1234A 1613541902\n",
                "Enter car SGF9283P 1613541902\n",
                "Exit SGX1234A 1613545602\n",
                "Enter car SGP2937F 1613546029\n",
                "Enter car SDW2111W 1613549730\n",
                "Enter car SSD9281L 1613549740\n",
                "Exit SDW2111W 1613559745",
            ]
            f.writelines(text_list)

        events = parse_input_file("test_input.txt")

        self.assertIsInstance(events, list)
        self.assertEqual(events, text_list[1:])

    def test_event_handler_default(self) -> None:
        with patch('sys.stdout', new=StringIO()) as output:
            with open("test_input.txt", "w") as f:
                text_list = [
                    "3 4\n",
                    "Enter motorcycle SGX1234A 1613541902\n",
                    "Enter car SGF9283P 1613541902\n",
                    "Exit SGX1234A 1613545602\n",
                    "Enter car SGP2937F 1613546029\n",
                    "Enter car SDW2111W 1613549730\n",
                    "Enter car SSD9281L 1613549740\n",
                    "Exit SDW2111W 1613559745",
                ]
                f.writelines(text_list)

            events = parse_input_file("test_input.txt")
            event_handler(events)

        self.assertEqual(
            output.getvalue(),
            (
                "Accept MotorcycleLot1\n"
                "Accept CarLot1\n"
                "MotorcycleLot1 2\n"
                "Accept CarLot2\n"
                "Accept CarLot3\n"
                "Reject\n"
                "CarLot3 6\n"
            ),
        )

    def test_event_handler_when_no_car_parking_lot(self) -> None:
        with patch('sys.stdout', new=StringIO()) as output:
            with open("test_input.txt", "w") as f:
                text_list = [
                    "0 3\n",
                    "Enter motorcycle SGX1234A 1613541902\n",
                    "Enter car SGF9283P 1613541902\n",
                    "Exit SGX1234A 1613545602\n",
                    "Enter car SGP2937F 1613546029\n",
                    "Enter car SDW2111W 1613549730\n",
                    "Enter car SSD9281L 1613549740\n",
                ]
                f.writelines(text_list)

            events = parse_input_file("test_input.txt")
            event_handler(events)

        self.assertEqual(
            output.getvalue(),
            (
                "Accept MotorcycleLot1\n"
                "Reject\n"
                "MotorcycleLot1 2\n"
                "Reject\n"
                "Reject\n"
                "Reject\n"
            ),
        )

    def test_event_handler_when_no_motorcycle_parking_lot(self) -> None:
        with patch('sys.stdout', new=StringIO()) as output:
            with open("test_input.txt", "w") as f:
                text_list = [
                    "1 0\n",
                    "Enter motorcycle SGX1234A 1613541902\n",
                    "Enter car SGF9283P 1613541902\n",
                    "Enter car SGP2937F 1613546029\n",
                    "Enter car SSD9281L 1613549740\n",
                ]
                f.writelines(text_list)

            events = parse_input_file("test_input.txt")
            event_handler(events)

        self.assertEqual(
            output.getvalue(),
            (
                "Reject\n"
                "Accept CarLot1\n"
                "Reject\n"
                "Reject\n"
            ),
        )

    def test_parking_lots_are_filled_sequentially(self) -> None:
        with patch('sys.stdout', new=StringIO()) as output:
            with open("test_input.txt", "w") as f:
                text_list = [
                    "4 0\n",
                    "Enter car AGP2001F 1613541902\n",
                    "Enter car BGP2002F 1613551902\n",
                    "Enter car CGP2003F 1613561902\n",
                    "Enter car DGP2004F 1613571902\n",
                    "Exit AGP2001F 1613561902\n",
                    "Enter car SDW2111W 1614571902\n",
                    "Enter car SGP1001F 1615571902\n",
                ]
                f.writelines(text_list)

            events = parse_input_file("test_input.txt")
            event_handler(events)

        self.assertEqual(
            output.getvalue(),
            (
                "Accept CarLot1\n"
                "Accept CarLot2\n"
                "Accept CarLot3\n"
                "Accept CarLot4\n"
                "CarLot1 12\n"
                "Accept CarLot1\n"
                "Reject\n"
            ),
        )


if __name__ == "__main__":
    unittest.main()
