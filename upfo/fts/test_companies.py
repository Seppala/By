from functional_tests import FunctionalTest, ROOT
from selenium.webdriver.common.keys import Keys
import requests
import simplejson

class TestCompanies(FunctionalTest):
        
    def test_site_layout(self):

            # Gertrude opens her browser and goes to the main page
            self.browser.get(ROOT)
            #click to login with facebook
            fb_login = self.browser.find_element_by_link_text('Log in')
            fb_login.click()
            # She finds the text "False" in the element with id = "isupfo"
            isup = self.browser.find_element_by_id('isupfo')
            self.assertEquals(isup.text, "False")
            # She finds the text "I'm up for something"
            link = self.browser.find_element_by_tag_name('button')
            self.assertEquals(link.text, "I'm up for something")
    
            # She presses the button 
            link.click()
            #And now should find that the isup text is true...
            self.assertEquals(isup.text, "True")
        