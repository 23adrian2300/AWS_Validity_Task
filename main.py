from verify_aws_validity import is_json, is_aws_json, check_asteriks
import sys
if __name__ == '__main__':
    path = input("Enter the path to the file: ")
    if is_json(path) == "NOT JSON":
        print("This is not a json file")
        sys.exit(1)
    elif is_json(path):
        print("This is a json file")
    else:
        print("File not exist")
        sys.exit(1)
    if is_aws_json(path):
        print("This is a valid AWS json file")
    else:
        print("This is not a valid AWS json file")
        sys.exit(1)
    if check_asteriks(path):
        print("There is no single * in the Resource field")
    else:
        print("There is * in the Resource field")
        sys.exit(1)
    print("End of program")
