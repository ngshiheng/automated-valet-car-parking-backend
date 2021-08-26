from typing import Tuple

from lib.database import Status
from lib.logs import log

from api.event import subscribe


def handle_vehicle_enter_event(data: Tuple[str, Status]) -> None:
    """
    Examples:
    - Accept MotorcycleLot1
    - Accept CarLot1
    - Accept CarLot2
    - Accept CarLot3
    - Reject
    """
    lot_no, status = data

    if status == Status.ACCEPTED:
        log(f"Accept {lot_no}")

    else:
        log("Reject")


def handle_vehicle_exit_event(data: Tuple[str, int]) -> None:
    """
    Examples:
    - MotorcycleLot1 2
    - CarLot3 6
    """
    lot_no, parking_fee = data
    log(f"{lot_no} {parking_fee}")


def setup_log_event() -> None:
    subscribe("vehicle_enter", handle_vehicle_enter_event)
    subscribe("vehicle_exit", handle_vehicle_exit_event)
