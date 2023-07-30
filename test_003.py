from selenium import webdriver

class Test_credence_003:
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
