from functional_tests import FunctionalTest, ROOT
from selenium.webdriver.common.keys import Keys

class testPollsAdmin(FunctionalTest):
    
    def test_can_create_new_poll_via_admin_site(self):

        # Gertrude opens her web browser, and goes to the admin page
        self.browser.get(ROOT + '/admin/')

        # She sees the familiar 'Django administration' heading
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        # She types in her username and passwords and hits return
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')

        password_field = self.browser.find_element_by_name('password')
        print("got the browser field")
        password_field.send_keys('adm1n')
        password_field.send_keys(Keys.RETURN)

        # She now sees a couple of hyperlinks that says "Companys" and clicks it
        companies_links = self.browser.find_element_by_link_text('Users')
        #self.assertEquals(len(companies_links), 1)
        #companies_links.click()
        
        # Sees a link to 'add' polls and clicks on it
        #new_company_link = self.browser.find_element_by_link_text('Add company')
        #new_company_link.click()
        
        # She sees the fields for name and permalink
        body = self.browser.find_element_by_tag_name("body")
        #self.assertIn('Name', body.text)
        #self.assertIn('Permalink', body.text)
        
        #She types in a new company
        name_field = self.browser.find_element_by_name('name')
        name_field.send_keys("Qestu")
        permalink_field = self.browser.find_element_by_name('permalink')
        permalink_field.send_keys("qestu")
        
        #and presses the save button
        save_button = self.browser.find_element_by_css_selector("input[value='Save']")
        save_button.click()
        
        #She is returned to the company listing page and can now see the new poll
        new_company_links = self.browser.find_elements_by_link_text(
            "Qestu"
        )
        self.assertEquals(len(new_company_links), 1)
     