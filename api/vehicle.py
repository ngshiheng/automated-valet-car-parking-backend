from lib.database import VehicleType, add_vehicle, remove_vehicle

from api.event import post_event


def record_vehicle_entry(vehicle_type: VehicleType, number_plate: str, epoch_timestamp: str) -> None:
    """
    API to create Vehicle object in database.
    """

    data = add_vehicle(vehicle_type, number_plate, int(epoch_timestamp))
    post_event("vehicle_enter", data)


def record_vehicle_exit(number_plate: str, epoch_timestamp: str) -> None:
    """
    API to remove Vehicle object from database.
    """

    data = remove_vehicle(number_plate, int(epoch_timestamp))
    post_event("vehicle_exit", data)
