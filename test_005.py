from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_credence_005:
    import time
    def test_credkart_login_005(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://automation.credence.in/login")
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("Credencetest001@test.com")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Credence@1234")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        try:
            driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("Test_case is PASS")
            driver.close()
            assert True
        except:
            print("Test_case is Fail")
            driver.close()
            assert False

    def test_amountverfication(self):
        import time

        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.select import Select

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")

        # driver = webdriver.Chrome(options=chrome_options)
        driver = webdriver.Chrome()
        driver.maximize_window()
        # from selenium.webdriver.firefox.options import Options
        # options = Options()
        # options.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
        # driver = webdriver.Firefox(options=options)

        driver.get("https://automation.credence.in/login")
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Credencetest@test.com")
        driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Credence@123")
        # Click Login button
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Click on Product--Macbook
        driver.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/div/div/a[2]/h3").click()
        # Click on add to cart
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        # Click on Continue Shopping
        driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()
        # Click on Product--Headphone
        driver.find_element(By.XPATH, "//h3[normalize-space()='Headphones']").click()
        # Click on add to cart
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        # Click on Continue Shopping
        driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()
        # Click on Product--Ipad
        driver.find_element(By.XPATH, "//h3[normalize-space()='Apple iPad Retina']").click()
        # Click on add to cart
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        # Select Quality dropdown value for product 1
        # driver.implicitly_wait(20)
        time.sleep(3)
        product_quantity1 = Select(driver.find_element(By.XPATH, "//tbody/tr[1]/td[3]/select"))
        product_quantity1.select_by_index(3)
        time.sleep(2)
        # Select Quality dropdown value for product 2
        product_quantity2 = Select(driver.find_element(By.XPATH, "//tbody/tr[2]/td[3]/select"))
        product_quantity2.select_by_index(3)
        time.sleep(2)
        # Select Quality dropdown value for product 3
        product_quantity3 = Select(driver.find_element(By.XPATH, "//tbody/tr[3]/td[3]/select"))
        product_quantity3.select_by_index(2)

        l = len(driver.find_elements(By.XPATH, "//tbody/tr/td[4]"))
        # l=6
        time.sleep(2)
        Product_Price_List = []
        for r in range(1, l - 2):
            var1 = driver.find_element(By.XPATH, "//tbody/tr[" + str(r) + "]/td[4]").text
            # print(var1) Var1 = $9,899.10
            product_price = (var1[1:])
            # print(product_price)
            Product_Price_List.append(float(product_price))

        print(Product_Price_List)
        Exp_Subtotal = round((sum(Product_Price_List)), 2)
        # Exp_Subtotal-->11999.889999999998
        # Exp_Subtotal-->11999.89
        print("Exp_Subtotal-->" + str(Exp_Subtotal))
        print(Product_Price_List)

        System_Value = []

        for r in range(l - 2, l + 1):
            var2 = driver.find_element(By.XPATH, "//tbody/tr[" + str(r) + "]/td[4]").text  # $10,499.94
            var3 = var2.replace(',', '')  # $10499.94
            system_price = (var3[1:])  # 10499.94
            System_Value.append(float(system_price))

        print(System_Value)

        if Exp_Subtotal == System_Value[0]:
            print("SubTotal is matched")
            assert True
        else:
            print("Subtotal is not matched")
            assert False










