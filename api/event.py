__all__ = ["subscribe", "post_event"]

from typing import Any

subscribers = {}


def subscribe(event_type: str, fn) -> None:
    """
    Subscribe function used by listners.
    """
    if event_type not in subscribers:
        subscribers[event_type] = []
    subscribers[event_type].append(fn)


def post_event(event_type: str, data: Any) -> None:
    """
    Post an event. Used by API.
    """
    if event_type not in subscribers:
        return

    for fn in subscribers[event_type]:
        fn(data)
