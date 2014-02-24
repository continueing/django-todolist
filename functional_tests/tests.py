__author__ = 'continueing'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        #self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    # helper method, validation method
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        str_todo_item ='Buy peacock feathers'
        str_todo = 'To-Do'

        self.browser.get(self.live_server_url)

        self.assertIn(str_todo,  self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn(str_todo, header_text)

        inputBox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputBox.get_attribute('placeholder'), 'Enter a to-do item')

        inputBox.send_keys(str_todo_item)
        inputBox.send_keys(Keys.ENTER)

        inputBox = self.browser.find_element_by_id('id_new_item')
        inputBox.send_keys('Use peacock feathers to make a fly')
        inputBox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.check_for_row_in_list_table('1: '+str_todo_item)
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        self.fail('Finish the test!')


