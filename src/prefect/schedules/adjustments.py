"""
Schedule adjustments are functions that accept a `datetime` and modify it in some way.

Adjustments have the signature `Callable[[datetime], datetime]`.
"""
from datetime import datetime, timedelta
from typing import Callable

import pendulum

import prefect.schedules.filters


def add(interval: timedelta) -> Callable[[datetime], bool]:
    """
    Adjustment that adds a specified interval to the date.

    Args:
        - interval (timedelta): the amount of time to add

    Returns:
        - Callable[[datetime], bool]: the adjustment function
    """

    def _adjustment_fn(dt: datetime) -> datetime:
        return pendulum.instance(dt) + interval

    return _adjustment_fn


def next_weekday(dt: datetime) -> datetime:
    """
    Adjustment that advances a date to the next weekday. If the date is already a weekday,
    it is returned unadjusted.

    Args:
        - dt (datetime): the datetime to adjust

    Returns:
        - datetime: the adjusted datetime
    """
    while not prefect.schedules.filters.is_weekday(dt):
        dt = dt.add(days=1)
    return dt
