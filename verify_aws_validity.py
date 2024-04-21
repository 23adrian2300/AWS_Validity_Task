import json
import os
import re


# Check if the keys are valid
def check_keys(data):
    valid_keys = ["PolicyName", "PolicyDocument", "Version", "Statement", "Action", "Effect", "Resource", "Sid",
                  "Principal",
                  "Condition"]
    for key in data.keys():
        if key not in valid_keys:
            return False
    return True

# Check if the JSON file is valid
def is_aws_json(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension != ".json":
        return "NOT A JSON FILE"
    try:
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError as e:
                return "INVALID JSON FORMAT"

            if not check_keys(data):
                return "INVALID JSON FORMAT"

            policy_name = data["PolicyName"]
            policy_document = data["PolicyDocument"]

            if 1 < len(policy_name) > 128 or not re.fullmatch(r"[\w+=,.@-]+", policy_name):
                return "INVALID POLICY NAME"

            version = policy_document["Version"]
            statement = policy_document["Statement"]

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

# main function of the task - False if there is an asterisk, True otherwise
def check_asterisk(file_path):
    res = is_aws_json(file_path)
    if res != True:
        return res
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            for key in data["PolicyDocument"]["Statement"]:  # we know that this key exists
                if not isinstance(key["Resource"], list):
                    if key["Resource"] == "*":
                        return False
                else:
                    for resource in key["Resource"]:
                        if resource == "*":
                            return False
            return True
    except FileExistsError as e:
        return "FILE NOT EXIST"  # this should never happen
