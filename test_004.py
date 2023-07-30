import pytest
from selenium import webdriver

class Test_Credence_001:

    def test_sum_001(self):
        a = 5
        b = 5
        sum = a + b
        print("Sum of a and b is :" + str(sum))
        if sum == 10:
            assert True
        else:
            assert False

    def test_sub_002(self):
        a = 8
        b = 3
        sub = a-b
        print("Sub of a and b is :" + str(sub))
        if sub == 4:
            assert True
        else:
            assert False

    def test_CredenceUrl_003(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title == "Credence":
            print("You are at credence.in")
            assert True
            driver.close()
        else:
            print("You are at Wrong url")
            driver.close()
            assert False
