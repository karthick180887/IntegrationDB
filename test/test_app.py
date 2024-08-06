import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:5000')

    def test_add_user(self):
        driver = self.driver
        name_field = driver.find_element(By.ID, 'name')
        age_field = driver.find_element(By.ID, 'age')

        name_field.send_keys('Karthick Selvam')
        age_field.send_keys('36')
        age_field.send_keys(Keys.RETURN)

        time.sleep(2)  # Wait for the page to load

        driver.get('http://localhost:5000/display')
        time.sleep(2)

        users = driver.find_elements(By.TAG_NAME, 'td')
        self.assertIn('John Doe', [user.text for user in users])
        self.assertIn('30', [user.text for user in users])

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
