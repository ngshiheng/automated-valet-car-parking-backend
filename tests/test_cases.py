import os
import sys
import unittest
from io import StringIO

from main import event_handler, parse_events


class TestAutomatedValetParkingSystems(unittest.TestCase):
    def setUp(self) -> None:
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

            self.events = text_list[1:]

        return super().setUp()

    def tearDown(self) -> None:
        os.remove("test_input.txt")
        return super().tearDown()

    def test_parse_events(self) -> None:
        events = parse_events("test_input.txt")
        self.assertEqual(events, self.events)

    def test_event_handler(self) -> None:
        captured_output = StringIO()
        sys.stdout = captured_output
        event_handler(self.events)
        sys.stdout = sys.__stdout__

        self.assertEqual(
            captured_output.getvalue(),
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


if __name__ == "__main__":
    unittest.main()
