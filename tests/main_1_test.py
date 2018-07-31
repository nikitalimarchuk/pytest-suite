import pytest
import allure


class TestMain_1(object):
    @allure.step
    def test_case_1(self):
        assert True

    @allure.step
    def test_case_2(self):
        assert 5 < 6, "6 COULD NOT BE LESS THEN 5"

    @allure.step
    def test_case_3(self):
        assert 5 > 6, "5 COULD NOT BE GREATER THEN 6"
