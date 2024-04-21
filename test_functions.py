import unittest

from verify_aws_validity import *


class TestClass(unittest.TestCase):
    def test_invalid_json(self):
        self.assertEqual(is_json("test_cases\\invalid_json.json"), "JSON ERROR")

    def test_valid_json(self):
        self.assertEqual(is_json("test_cases\\valid_json_one_asterisk.json"), True)

    def test_invalid_type(self):
        self.assertEqual(is_json("test_cases\\invalid_type.txt"), "JSON ERROR")

    def test_file_not_exist(self):
        self.assertEqual(is_json("test_cases\\invalid12_json.json"), "FILE NOT EXIST")

    def test_aws_json(self):
        self.assertEqual(is_aws_json("test_cases\\valid_json_one_asterisk.json"), True)

    def test_invalid_aws_json(self):
        self.assertEqual(is_aws_json("test_cases\\invalid_aws_json.json"), "INVALID EFFECT")

    def test_aws_invalid_json(self):
        self.assertEqual(is_aws_json("test_cases\\invalid_json.json"), "JSON ERROR")

    def test_aws_invalid_type(self):
        self.assertEqual(is_aws_json("test_cases\\invalid_type.txt"), "JSON ERROR")

    def test_check_asteriks_one_asterisk(self):
        self.assertEqual(check_asteriks("test_cases\\valid_json_one_asterisk.json"), True)

    def test_check_asteriks_single_asterisk(self):
        self.assertEqual(check_asteriks("test_cases\\valid_json_single_asterisk.json"), False)

    def test_check_asteriks_invalid_json(self):
        self.assertEqual(check_asteriks("test_cases\\invalid_json.json"), "JSON ERROR")

    def test_check_asteriks_invalid_type(self):
        self.assertEqual(check_asteriks("test_cases\\invalid_type.txt"), "JSON ERROR")

    def test_check_asteriks_more_asterisk(self):
        self.assertEqual(check_asteriks("test_cases\\valid_json_more_asterisk.json"), True)

    def test_valid_effect(self):
        self.assertEqual(is_aws_json("test_cases\\invalid_effect_json.json"), "INVALID EFFECT")

    def test_valid_version(self):
        self.assertEqual(is_aws_json("test_cases\\invalid_version_json.json"), "INVALID VERSION")

    def test_valid_policy_name(self):
        self.assertEqual(is_aws_json("test_cases\\invalid_policy_name_json.json"), "INVALID POLICY NAME")

    def test_not_action_field(self):
        self.assertEqual(is_aws_json("test_cases\\invalid_not_action_field_json.json"), "NO ACTION FIELD")


if __name__ == '__main__':
    unittest.main()
