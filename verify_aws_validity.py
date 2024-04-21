import json


def is_json(file_path):
    try:
        with open(file_path, 'r') as f:
            try:
                json.load(f)
            except json.JSONDecodeError as e:
                return "NOT JSON"
            return True
    except FileNotFoundError as e:
        return False


def is_aws_json(file_path):
    if not is_json(file_path) or is_json(file_path) == "NOT JSON":
        return False
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if "PolicyDocument" in data:
                if "Version" in data["PolicyDocument"] and "Statement" in data["PolicyDocument"]:
                    for key in data["PolicyDocument"]["Statement"]:
                        if "Resource" in key:
                            return True
            return False
    except FileExistsError as e:
        return "File not found"


def check_asteriks(file_path):
    if not is_aws_json(file_path):
        return False
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            for key in data["PolicyDocument"]["Statement"]:  # we know that this key exists
                if key["Resource"] == "*":
                    return False
            return True
    except FileExistsError as e:
        return False
