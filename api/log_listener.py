from typing import Any, Dict

from lib.database import Status
from lib.logs import log

from api.event import subscribe


def handle_vehicle_enter_event(data: Dict[str, Any]) -> None:
    """
    Examples:
    - Accept MotorcycleLot1
    - Accept CarLot1
    - Accept CarLot2
    - Accept CarLot3
    - Reject
    """
    lot_no = data['lot_no']
    status = data['status']

    if status == Status.ACCEPTED:
        log(f"Accept {lot_no}")

    else:
        log("Reject")


def handle_vehicle_exit_event(data: Dict[str, Any]) -> None:
    """
    Examples:
    - MotorcycleLot1 2
    - CarLot3 6
    """
    lot_no = data['lot_no']
    parking_fee = data['parking_fee']

    log(f"{lot_no} {parking_fee}")


def setup_log_event() -> None:
    subscribe("vehicle_enter", handle_vehicle_enter_event)
    subscribe("vehicle_exit", handle_vehicle_exit_event)
