from datetime import datetime
from pytz import BaseTzInfo, timezone, utc
from .config import settings


def now() -> datetime:
    """
    Return an aware or naive datetime.datetime, depending on settings.USE_TZ.
    """
    dt = datetime.now()

    if not settings.use_tz:
        return dt

    utc_now = datetime.now(utc)
    tz_now = utc_now.astimezone(timezone(settings.time_zone))
    return tz_now.replace(tzinfo=None)


def get_utc_now() -> datetime:
    return datetime.utcnow()

