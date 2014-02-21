__author__ = 'continueing'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        #self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()


    def test_can_start_a_list_and_retrieve_it_later(self):
        str_todo_item ='Buy peacock feathers'


        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do',  self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputBox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputBox.get_attribute('placeholder'), 'Enter a to-do item')

        inputBox.send_keys(str_todo_item)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: '+ str_todo_item for row in rows), 'New to-do item did not appear in table.')

        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings = 'ignore')



