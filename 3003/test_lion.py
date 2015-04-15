__author__ = 'whitefoxnsk'

from unittest import TestCase
from lion import Lion
import unittest


class LionTest(TestCase):
    leo_dict = {
        ('hunter', 'fed'): ('Run,status change to hungry', 'hungry')
    }

    def test_init(self):
        leo = Lion(self.leo_dict, "fed")
        self.assertEqual("fed", leo.status, 'Status is not correct')
        self.assertEqual("", leo.action, 'Action is not correct')
        self.assertEqual(self.leo_dict, leo.l_dict, 'Dict is not correct')

    def test_init_exception_status(self):
        self.assertRaises(Exception, Lion, self.leo_dict, "")

    def test_init_exception_dict(self):
        self.assertRaises(Exception, Lion, {}, "fed")

    def test_result(self):
        leo = Lion(self.leo_dict, "fed")
        leo.result("hunter")
        self.assertEqual("hungry", leo.status, 'Status is not correct')
        self.assertEqual("Run,status change to hungry", leo.action, 'Action is not correct')

    def test_result_exception(self):
        leo = Lion(self.leo_dict, "fed")
        self.assertRaises(Exception, leo.result, "Sosiska")


if __name__ == '__main__':
    unittest.main()