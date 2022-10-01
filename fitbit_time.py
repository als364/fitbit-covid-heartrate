import bisect
from datetime import datetime, timedelta, timezone

from constants import TIMEZONES

"""
    Performs a binary search over the ~15k heartrate events captured per day.

        Parameters:
                start (datetime): The UTC time at which to start finding events.
                duration (int): The duration in seconds of the timespan.
                time_series_json (json): A JSON list of heartrate events of the following shape:
                    {
                        "dateTime": datetime_value,
                        "value": {
                            "bpm": int_value,
                            "confidence": int_value,
                        },
                    }
                    This is in JSON because instantiating 15k objects is really expensive and I only have so much RAM

        Returns:
                heartrate_events (list): All events that fall within the specified timespan.
"""
def get_heartrate_events_for_timespan(start, duration, time_series_json):
    start_index = bisect.bisect(time_series_json, start, key=lambda event: parse_fitbit_datetime(event["dateTime"]))
    end = start + timedelta(seconds=duration)

    heartrate_events = []
    for event in time_series_json[start_index:]:
        event_time = parse_fitbit_datetime(event["dateTime"])
        if event_time >= end:
            break
        else:
            heartrate_events.append(event)
    return heartrate_events


def parse_fitbit_datetime(datetime_string):
    return datetime.strptime(datetime_string, '%m/%d/%y %H:%M:%S')


def utc_to_timezone(utc_datetime, target_timezone):
    return utc_datetime.replace(tzinfo=timezone.utc).astimezone(target_timezone)


def get_local_timezone(time):
    for tz_info in TIMEZONES:
        # 'Vacation' case
        if (
            "left_timezone_at" in tz_info
            and "entered_timezone_at" in tz_info
            and tz_info["entered_timezone_at"] < time < tz_info["left_timezone_at"]
        ):
            return tz_info["timezone"]
        # 'Start' case
        if "left_timezone_at" in tz_info and time < tz_info["left_timezone_at"]:
            return tz_info["timezone"]
        # 'End' case
        if "entered_timezone_at" in tz_info and tz_info["entered_timezone_at"] < time:
            return tz_info["timezone"]
        # Only one timezone case
        return tz_info["timezone"]
