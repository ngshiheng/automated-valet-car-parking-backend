import math
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Optional

from lib.errors import VehicleNotFoundError

# Our parking lot database.
car_parking_lot = {}
motorcycle_parking_lot = {}


class NoValue(Enum):
    def __repr__(self):
        return f"<{self.__class__.__name__}.{self.name}>"


class VehicleType(NoValue):
    """
    Vehicle types available for valet car parking system.
    """

    CAR = "car"
    MOTORCYCLE = "motorcycle"


class Status(NoValue):
    """
    Vehicle registration status.
    """

    ACCEPTED = "accepted"
    REJECTED = "rejected"


@dataclass
class Vehicle:
    """
    Vehicle object of valet car parking system.
    """

    type: VehicleType
    number_plate: str
    entry_timestamp: int


def create_parking_lot(vehicle_type: VehicleType, size: int) -> Dict[str, Optional[Vehicle]]:
    """
    Create a dictionary of based on input size (first row) from `input.txt`.
    The dictionary here represents our availability of our valet car parking system.
    """

    if vehicle_type:
        return {f"{vehicle_type.value.title()}Lot{i+1}": None for i in range(size)}

    raise ValueError("Unable to create car park as VehicleType is not provided.")


def add_vehicle(vehicle_type: VehicleType, number_plate: str, entry_epoch_timestamp: int) -> Dict[str, Any]:
    """
    Create an entry in our database based on the parking lot"s availability.
    Returns parking `lot_no` and parking status.
    """

    new_vehicle = Vehicle(vehicle_type, number_plate, entry_epoch_timestamp)

    parking_lot: Dict[str, Optional[Vehicle]] = car_parking_lot if vehicle_type == VehicleType.CAR else motorcycle_parking_lot

    for lot_no, occupant in parking_lot.items():
        if occupant is None:
            parking_lot.update({lot_no: new_vehicle})
            return {
                "vehicle": new_vehicle,
                "lot_no": lot_no,
                "status": Status.ACCEPTED,
            }

    return {
        "vehicle": new_vehicle,
        "lot_no": "",
        "status": Status.REJECTED,
    }


def remove_vehicle(number_plate: str, exit_epoch_timestamp: int) -> Dict[str, Any]:
    """
    Remove a vehicle from our database.
    Returns parking `lot_no` and `parking_fee`.
    """

    data = find_vehicle(number_plate)
    vehicle = data['vehicle']
    lot_no = data['lot_no']
    parking_lot = data['parking_lot']

    parking_lot.update({lot_no: None})

    time_elapsed_hours = (exit_epoch_timestamp - vehicle.entry_timestamp) / 60 / 60
    billed_hours = math.ceil(time_elapsed_hours)

    if vehicle.type == VehicleType.MOTORCYCLE:
        rate_per_hour = 1
    else:
        rate_per_hour = 2

    parking_fee = billed_hours * rate_per_hour
    assert parking_fee >= 0, f'Invalid parking fee. Please check the entry and exit timestamp of {vehicle}!'

    return {
        "vehicle": vehicle,
        "lot_no": lot_no,
        "parking_fee": parking_fee,
    }


def find_vehicle(number_plate: str) -> Dict[str, Any]:
    """
    Find Vehicle object from all parking lots using `number_plate`.
    """

    for parking_lot in [car_parking_lot, motorcycle_parking_lot]:
        for lot_no, vehicle in parking_lot.items():
            if vehicle and vehicle.number_plate == number_plate:
                return {
                    "vehicle": vehicle,
                    "lot_no": lot_no,
                    "parking_lot": parking_lot,
                }

    raise VehicleNotFoundError(number_plate)
