from typing import List

from api.log_listener import setup_log_event
from api.vehicle import record_vehicle_entry, record_vehicle_exit
from lib.database import VehicleType, car_parking_lot, create_parking_lot, motorcycle_parking_lot


def parse_input_file(file_path: str) -> List[str]:
    """
    Read events from a text-based input file.
    Initialize our database with parking lots with no occupant.
    Returns a list of events from out input file.
    """

    with open(file_path, "r") as f:
        data = f.readlines()

        car_parking_lot_size, motorcycle_parking_lot_size = data[0].split(" ", maxsplit=2)

        # Populate our database.
        car_parking_lot.update(create_parking_lot(VehicleType.CAR, int(car_parking_lot_size)))
        motorcycle_parking_lot.update(create_parking_lot(VehicleType.MOTORCYCLE, int(motorcycle_parking_lot_size)))

        return data[1:]


def event_handler(events: List[str]) -> None:
    """
    Main event handler function.
    """

    # Initialize events.
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
    """
    Main entry point of our automated valet car parking system.
    """
    events = parse_input_file("input.txt")
    event_handler(events)


if __name__ == "__main__":
    main()
