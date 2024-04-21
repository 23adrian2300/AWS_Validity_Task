from verify_aws_validity import is_json, is_aws_json, check_asteriks
import sys

if __name__ == '__main__':
    path = input("Enter the path to the file: ")
    if is_json(path) == "ERROR":
        print("This is not a valid json file")
        sys.exit(1)
    elif is_json(path) == "FILE NOT EXIST":
        print("File not exist")
        sys.exit(1)
    res = is_aws_json(path)
    if res == "INVALID EFFECT":
        print("There is invalid Effect field")
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

    res = check_asteriks(path)
    if res == "JSON ERROR":
        print("This is not a valid json file")
        sys.exit(1)
    elif res == "FILE NOT EXIST":
        print("File not exist")
        sys.exit(1)
    elif res == True:
        print("There are not any single asterisk in the Resource field")
    else:
        print("There is a single asterisk in the Resource field")
        sys.exit(1)
