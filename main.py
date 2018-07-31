import glob
import pytest
import os

class Runner(object):
    def run(self):
        pytest.main(["rmdir /s allure-reports", "mkdir allure-reports", "-s", "-v", "tests", "--alluredir=allure-reports"])

if __name__ == "__main__":

    files = glob.glob('allure-reports*')
    for f in files:
        os.remove(f)
    Runner().run()
