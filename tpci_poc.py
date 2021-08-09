import json
import os
import uuid
from datetime import datetime, timezone
import argparse

start_time = ""
now = ""

parser = argparse.ArgumentParser()
parser.add_argument("exampleOutput", default="TPCi_TeamCity_data_form.json", help="Final format of the output file")
parser.add_argument("translationSpec", default="schemaMapping.json", help="Specifies the translation of environment variables and modified data to output format")
parser.add_argument("outputFile", default="S3_storage.json", help="S3 output file name")
args = parser.parse_args()
# print(args.exampleOutput)
# print(args.translationSpec)
inFile = args.exampleOutput
translationSpec = args.translationSpec
# outputFile = args.outputFile


def main():
    with open(inFile, "r") as infile:
        build_data = json.load(infile)

    with open(translationSpec, "r") as map_file:
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

    if args.outputFile:
        outputFile = args.outputFile
        with open(outputFile, "w") as out_file:  # truncate file first
            json.dump(build_data, out_file)
    else:
        print(json.dumps(build_data))


def get_guid():
    return str(uuid.uuid4())


def get_start_time():
    global start_time
    start_str = search_env_variable("BUILD_START_DATE") + search_env_variable("BUILD_START_TIME")
    start_time = datetime.strptime(start_str, '%Y%m%d%H%M%S')
    return start_time.now(tz=timezone.utc).replace(microsecond=0).isoformat()


def get_stop_time():
    global now
    now = datetime.utcnow()
    return now.now(tz=timezone.utc).replace(microsecond=0).isoformat()


def get_total_time():
    diff_time = now - start_time
    days, seconds = diff_time.days, diff_time.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    diff_display = f"HH:MM:SS {hours:02}:{minutes:02}:{seconds:02}"
    return diff_display


def search_env_variable(field_name):
    try:
        found_value = os.environ[field_name]
    except KeyError:
        found_value = f"{field_name} not found!!!"

    return found_value


if __name__ == '__main__':
    main()
