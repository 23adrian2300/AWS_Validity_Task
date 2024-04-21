import json
import re


def is_json(file_path):
    try:
        with open(file_path, 'r') as f:
            json.load(f)
        return True

    except FileNotFoundError as e:
        return "FILE NOT EXIST"
    except json.JSONDecodeError as e:
        return "JSON ERROR"


def is_aws_json(file_path):
    check = is_json(file_path)
    if check == "FILE NOT EXIST" or check == "JSON ERROR":
        return check

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

            policy_name = data["PolicyName"]
            policy_document = data["PolicyDocument"]
            role = data["RoleName"]
            if 1 < len(policy_name) > 128 or not re.fullmatch(r"[\w+=,.@-]+", policy_name):
                return "INVALID POLICY NAME"

            version = policy_document["Version"]
            statement = policy_document["Statement"]

            if version is None or statement is None:
                return "NO VERSION OR STATEMENT FIELD"

            if version not in ["2012-10-17", "2008-10-17"]:
                return "INVALID VERSION"

            for key in statement:
                if "Action" not in key:
                    return "NO ACTION FIELD"
                if "Effect" in key:
                    if key["Effect"] not in ["Allow", "Deny"]:
                        return "INVALID EFFECT"
                if "Resource" not in key:
                    return "NO RESOURCE FIELD"

            return True

    except FileExistsError as e:
        return "FILE NOT EXIST"
    except json.JSONDecodeError as e:
        return "INVALID JSON FORMAT"


def check_asteriks(file_path):
    res = is_aws_json(file_path)
    if res != True:
        return res
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            for key in data["PolicyDocument"]["Statement"]:  # we know that this key exists
                if key["Resource"] == "*":
                    return False
            return True
    except FileExistsError as e:
        return "FILE NOT EXIST"
