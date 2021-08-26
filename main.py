from typing import List

from api.log_listener import setup_log_event
from api.vehicle import record_vehicle_entry, record_vehicle_exit
from lib.database import VehicleType


def parse_events(file_path: str) -> List[str]:
    """
    Read events from a text-based input file.
    """

    with open(file_path, "r") as f:
        data = f.readlines()
        return data[1:]


def event_handler(events: List[str]) -> None:
    """
    Main event handler function.
    """

    # Initialize event.
    setup_log_event()

    for event in events:
        if "Enter" in event:
            _, vehicle_type, number_plate, timestamp = event.split(" ")

            vehicle_type = VehicleType.MOTORCYCLE if vehicle_type == VehicleType.MOTORCYCLE.value else VehicleType.CAR
            record_vehicle_entry(vehicle_type, number_plate, timestamp)

        elif "Exit" in event:
            _, number_plate, timestamp = event.split(" ")
            record_vehicle_exit(number_plate, timestamp)

        else:
            raise ValueError("Invalid event type.")


def main() -> None:
    events = parse_events("input.txt")
    event_handler(events)


if __name__ == "__main__":
    main()
