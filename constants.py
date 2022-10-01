from datetime import datetime

import pytz

"""
    Put the locations of your exercise files here. Generally, these are in directory physical-activity/ and named
    exercise-###.json.
"""
EXERCISE_FILES = [
    "my/fitbit/data/location/physical-activity/exercise-0.json",
    "my/fitbit/data/location/physical-activity/exercise-1.json",
]

"""
    Put the date you tested positive for COVID here.
    Do not prefix months, days, hours, or minutes with a 0.
"""
COVID_DAY_0 = datetime(YYYY, M, DD)

"""
    Record the time zones where you were using your fit bit, in chronological order.
    Do not prefix months, days, hours, or minutes with a 0.
    Pytz uses the tz database, a list of which can be found at https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    
    If you never changed time zones during the periods you're analyzing, put a dict with just timezone:
        {"timezone": pytz.timezone('US/Eastern')}
        
    If you changed timezone once:
        {"left_timezone_at": datetime(YYYY, M, D, H, M), "timezone": pytz.timezone('US/Eastern')},
        {"entered_timezone_at": datetime(YYYY, M, D, H, M), "timezone": pytz.timezone('US/Eastern')}
        
    If you changed timezone twice:
        {"left_timezone_at": datetime(YYYY, M, D, H, M), "timezone": pytz.timezone('US/Eastern')},
        {"entered_timezone_at": datetime(YYYY, M, D, H, M), "left_timezone_at": datetime(YYYY, M, D, H, M), "timezone": pytz.timezone('US/Central')},
        {"entered_timezone_at": datetime(YYYY, M, D, H, M), "timezone": pytz.timezone('US/Eastern')}
"""
TIMEZONES = [
    {"left_timezone_at": datetime(YYYY, M, D, H, M), "timezone": pytz.timezone('US/Eastern')},
    {"entered_timezone_at": datetime(YYYY, M, D, H, M), "left_timezone_at": datetime(YYYY, M, D, H, M), "timezone": pytz.timezone('US/Central')},
    {"entered_timezone_at": datetime(YYYY, M, D, H, M), "timezone": pytz.timezone('US/Eastern')},
]