__all__ = ["subscribe", "post_event"]

subscribers = dict()


def subscribe(event_type: str, fn) -> None:
    if event_type not in subscribers:
        subscribers[event_type] = []
    subscribers[event_type].append(fn)


def post_event(event_type: str, data) -> None:
    if event_type not in subscribers:
        return

    for fn in subscribers[event_type]:
        fn(data)
