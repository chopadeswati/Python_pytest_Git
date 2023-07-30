# config interpreter
# pip install selenium
# pip install pytest - for test run
# pip install pytest-html - to generate report
# pip install pytest-xdist - to run parallel
# Select pytest as default runner in python (Go to setting --> Tools-->integrated Tools

# from selenium import webdriver


# file name should start with test_
# class name should start with Test_
# testcases should start with  test_

# To run the test files from terminal--> pytest
# For more details on lib/ plugins--> pytest -v
# For printing the output on console --> pytest -s
# To run specific file in project dir --> pytest filename.py (eg. pytest test_file_001.py)
# To run testcases parallel --> pytest -n=number (eg. pytest -n=2) number--> worker processor
# To generate html report --> (pytest --html=Reports/report.html)




class Test_Credence_001:

    def test_sum_001(self):
        a = 3
        b = 7
        sum = a + b
        print("Sum of a and b is :" + str(sum))
        if sum == 10:
            assert True
        else:
            assert False