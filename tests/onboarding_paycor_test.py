import os
import json
import unittest
import sys
import csv
import app
from unittest.mock import patch, Mock
from nose.tools import assert_is_none, assert_list_equal, assert_true, assert_equals


class OnboardingPaycorTest(object):
    @classmethod
    def setup_class(cls):
        cls.mock_get_patcher_get_employee = patch(
            'core.onboarding_paycor.OnboardingPaycor.get_employees')
        cls.mock_get_get_employee = cls.mock_get_patcher_get_employee.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_get_patcher_get_employee.stop()

    def test_get_employee(self):
        employee = {}
        with open('/src/tests/fixtures/onboarding.json', 'r') as open_file:
            employee = json.load(open_file)
        self.mock_get_get_employee.return_value = Mock()
        self.mock_get_get_employee.return_value = employee
        instance = app.OnboardingPaycorTest()
        result_json = instance.get_employees()
        assert_equals(employee, result_json)
