import json
import os
import uuid
from datetime import datetime

start_time = ""
now = ""


def main():
    with open("TPCi_TeamCity_data_form.json", "r") as infile:
        build_data = json.load(infile)

    with open("schemaMapping.json", "r") as map_file:
        mapping = json.load(map_file)

    for key, value in mapping.items():
        result = "ERROR: value never assigned"
        if value[0]:
            result = search_env_variable(value[0])

        if value[1]:
            method = value[1]
            if globals()[method]:
                # result = getattr(main, method)()
                result = globals()[method]()
            else:
                result = "method not found!!!"

        build_data[key] = result

    print(json.dumps(build_data))


def get_guid():
    return str(uuid.uuid4())


def get_start_time():
    global start_time
    start_str = search_env_variable("BUILD_START_DATE") + search_env_variable("BUILD_START_TIME")
    start_time = datetime.strptime(start_str, '%Y%m%d%H%M%S')
    return str(start_time)


def get_stop_time():
    global now
    now = datetime.now()
    return now.strftime("%m/%d/%Y %H:%M:%S")


def get_total_time():
    diff_time = now - start_time
    days, seconds = diff_time.days, diff_time.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    diff_display = f"D:HH:MM:SS {days}:{hours}:{minutes}:{seconds}"
    return diff_display


def search_env_variable(field_name):
    try:
        found_value = os.environ[field_name]
    except KeyError:
        found_value = f"{field_name} not found!!!"

    return found_value


if __name__ == '__main__':
    main()
