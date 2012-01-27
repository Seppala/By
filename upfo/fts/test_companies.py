from functional_tests import FunctionalTest, ROOT
from selenium.webdriver.common.keys import Keys
import requests
import simplejson

class TestCompanies(FunctionalTest):
		
	def test_site_layout(self):

	        # Gertrude opens her browser and goes to the main page
	        self.browser.get(ROOT)

	        # She finds the text "Populate database"
	        link = self.browser.find_element_by_tag_name('a')
	        self.assertEquals(link.text, 'Populate database')
		