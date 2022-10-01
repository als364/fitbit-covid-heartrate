import json


def parse_json_files(files):
    all_data = []
    for file in files:
        data = json.load(open(file))
        all_data.extend(data)
    return all_data