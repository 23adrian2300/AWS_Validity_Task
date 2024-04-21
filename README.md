# AWS::IAM:ROLE Policy Checker
This is a solution to a recruitment task for Remility company.

## Task
Write a method verifying the input JSON data. Input data format is defined as AWS::IAM::Role Policy - definition and example (AWS IAM Role JSON definition and example). Input JSON might be read from a file. 
Method shall return logical false if an input JSON Resource field contains a single asterisk and true in any other case. 

## How to run
First, you need to download the repository with the solution using the command:

`git clone https://github.com/23adrian2300/aws_checker`

Then, you need to navigate to the folder with the downloaded code:

`cd aws_checker`

To install the required libraries, you need to use:

`pip install -t requirements.txt`

To run the main file, you need to use:

`python main.py`

To run the test, use the following command:

`python test_functions.py`

## Valid JSON Format
```json
{
    "PolicyName": "root",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "IamListAccess",
                "Effect": "Allow",
                "Action": [
                    "iam:ListRoles",
                    "iam:ListUsers"
                ],
                "Resource": "*"
            }
        ]
    }
}
```
