from verify_aws_validity import is_aws_json, check_asterisk
import sys

"""
This is a file with presentation of verify_aws_validity.py functions that checks if the file is a valid AWS JSON file and if there is a single asterisk in the Resource field.
The main funtion is in verify_aws_validity.py file and name of it is check_asterisk. This function returns False if there is an asterisk, True otherwise.
"""

if __name__ == '__main__':
    path = input("Enter the path to the file: ")
    res = is_aws_json(path)
    if res == "INVALID EFFECT":
        print("There is invalid Effect field")
        sys.exit(1)
    elif res == "NOT A JSON FILE":
        print("This is not a json file")
        sys.exit(1)
    elif res == "INVALID VERSION":
        print("There is invalid Version field")
        sys.exit(1)
    elif res == "INVALID POLICY NAME":
        print("There is invalid Policy Name field")
        sys.exit(1)
    elif res == "NO ACTION FIELD":
        print("There is no Action field")
        sys.exit(1)
    elif res == "NO RESOURCE FIELD":
        print("There is no Resource field")
        sys.exit(1)
    elif res == "NO VERSION OR STATEMENT FIELD":
        print("There is no Version or Statement field")
        sys.exit(1)
    elif res == "INVALID JSON FORMAT":
        print("This is not a valid json file")
        sys.exit(1)
    elif res == "FILE NOT EXIST":
        print("File not exist")
        sys.exit(1)

    res = check_asterisk(path)

    if res == True:
        print("There are not any single asterisk in the Resource field")
    else:
        print("There is a single asterisk in the Resource field")
        sys.exit(1)
