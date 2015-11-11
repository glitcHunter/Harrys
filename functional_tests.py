from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):
    pass

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()

    def test_can(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('lista', self.browser.title)
        header_text =self.browser.find_element_by_tag_name("h1").text
        self.assertIn('lista',header_text)

        inputbox = self.browser.find_element_by_id('id_new_item') #znajdź inpuy by ud
        self.assertEqual(inputbox.get_attribute('placeholder'),'wpisz rzeczy do zrobienia') #sprawdź czy w formie znajdujie się
        #atrybut placeholder z wartością wpisz...

        inputbox.send_keys('buy')# wyślij buy

        inputbox.send_keys(Keys.ENTER) # wyślij enter

        table = self.browser.find_element_by_id('id_list_table') #znajdź table o id list_table
        rows = table.find_elements_by_tag_name('tr')#znajdź rows wedlug taga tr
        self.assertTrue(any(row.text =='1: buy' for row in rows),'nie ma w tabeli')#przeszukaj any wiersz i znjadź 1:buy albo zwróć błędu

        #self.fail('zalończenie testu')

if __name__ == '__main__':
    unittest.main()