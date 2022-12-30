from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import data
import pytest
import time

class Test_Prem:
    url = "https://opensource-demo.orangehrmlive.com"
    
    # Booting Method for running the Python Tests
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()
    
    def test_get_title(self, booting_function):
        self.driver.get(self.url)
        assert self.driver.title == 'OrangeHRM'
        print("SUCCESS # Web Title Captured Successfully")
    
    def test_pimadd(self, booting_function):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=data.Prem_Selectors.input_box_username).send_keys(data.Prem_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Prem_Selectors.input_box_password).send_keys(data.Prem_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.login_xpath).click()
        time.sleep(3)
        assert self.driver.title == 'OrangeHRM'
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.pim_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.addemployee_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=data.Prem_Selectors.input_box_firstname).send_keys(data.Prem_Data.firstName)
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=data.Prem_Selectors.input_box_lastname).send_keys(data.Prem_Data.lastName)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.save_xpath).click()
        time.sleep(6)
        print("ADD EMPLOYEE SUCCESSFULLY")