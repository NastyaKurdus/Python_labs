import json
import os


def get_json(path):
    with open(path) as data_file:
        return json.loads(json.load(data_file))


def update_json(data, path):
    """Dump data to json format and write it to json file with filename.
    :path - path to file from root directory"""
    with open(path, 'w') as outfile:
        return json.dump(json.dumps(data), outfile)


def is_user_exist(username):
    return os.path.exists('data/' + username + ".json")
