import bisect
import json
from math import floor
from statistics import mean

import parse
import fitbit_time
from constants import EXERCISE_FILES, COVID_DAY_0
from models.workout import Workout

if __name__ == '__main__':
    raw_workouts = parse.parse_json_files(EXERCISE_FILES)
    timespans = []
    for raw_workout in raw_workouts:
        if raw_workout["activityName"] == "Walk":
            timespans.append({
                "activityName": raw_workout["activityName"],
                "start": fitbit_time.parse_fitbit_datetime(raw_workout["startTime"]),
                "duration": raw_workout["duration"] / 1000
            })

    workouts = []
    for timespan in timespans:
        local_timezone = fitbit_time.get_local_timezone(timespan["start"])
        timespan_date = fitbit_time.utc_to_timezone(timespan["start"], local_timezone)
        heartrate_file_name = f"raw_data/physical-activity/heart_rate-{timespan_date.strftime('%Y-%m-%d')}.json"
        heartrate_events = json.load(open(heartrate_file_name))

        workout_heartrate_events = fitbit_time.get_heartrate_events_for_timespan(timespan["start"], timespan["duration"], heartrate_events)

        if(len(workout_heartrate_events) == 0):
            print(f"UTC:     {timespan['start']}")
            print(f"Eastern: {timespan_date}")

        bpm_values = [event["value"]["bpm"] for event in workout_heartrate_events]

        workout = Workout(
            activity=timespan["activityName"],
            start=timespan["start"],
            duration=timespan["duration"],
            bpm_values=bpm_values,
        )
        workouts.append(workout)

    covid_index = bisect.bisect(workouts, COVID_DAY_0, key=lambda workout: workout.start)
    pre_covid_workouts = workouts[:covid_index]
    post_covid_workouts = workouts[covid_index:]

    print("PRE COVID")
    for pre_covid_workout in pre_covid_workouts:
        print(f"{pre_covid_workout.activity}: Avg HR {pre_covid_workout.get_average_heartrate()}, Max HR {pre_covid_workout.get_max_heartrate()}")

    pre_covid_avg_heartrates = [wo.get_average_heartrate() for wo in pre_covid_workouts]
    pre_covid_max_heartrates = [wo.get_max_heartrate() for wo in pre_covid_workouts]
    print(f"Avg heartrates: Min {min(pre_covid_avg_heartrates)} Avg {floor(mean(pre_covid_avg_heartrates))} Max {max(pre_covid_avg_heartrates)}")
    print(f"Max heartrates: Min {min(pre_covid_max_heartrates)} Avg {floor(mean(pre_covid_max_heartrates))} Max {max(pre_covid_max_heartrates)}")


    print("\n\nPOST COVID")
    for post_covid_workout in post_covid_workouts:
        print(f"{post_covid_workout.activity}: Avg HR {post_covid_workout.get_average_heartrate()}, Max HR {post_covid_workout.get_max_heartrate()}")

    post_covid_avg_heartrates = [wo.get_average_heartrate() for wo in post_covid_workouts]
    post_covid_max_heartrates = [wo.get_max_heartrate() for wo in post_covid_workouts]
    print(f"Avg heartrates: Min {min(post_covid_avg_heartrates)} Avg {floor(mean(post_covid_avg_heartrates))} Max {max(post_covid_avg_heartrates)}")
    print(f"Max heartrates: Min {min(post_covid_max_heartrates)} Avg {floor(mean(post_covid_max_heartrates))} Max {max(post_covid_max_heartrates)}")