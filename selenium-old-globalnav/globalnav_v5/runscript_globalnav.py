import unittest
import globalnav_elements as GE
import globalnav_testfunctions as TF
from webdriver_config import wd   #skipIe
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# ==================================================================================================
# ==================================================================================================
testName = 'Global Nav' # Name of test will go here to populate test name fields in the test.
base_url = 'http://www.lexus.com'

# if origin.staging or staging environment is the url under test, use this as base_url to log in first:
# http://<login>:<password>@origin.staging.lexus.com
# (Input actual login and password of staging environment for <login> and <password>).
# ==================================================================================================
# ==================================================================================================
# ==================================================================================================
# This is the file that the content is written to
# fileOut = open(testName + ' Report - ' + (currentTime()) + '.txt', 'a+')
# ==================================================================================================
# ==================================================================================================

class GlobalNav(unittest.TestCase):

    def setUp(self):
        self.driver = wd
        self.driver.maximize_window()    
        self.driver.implicitly_wait(10)

        # fileOut.write('\nStart of ' + testName + ' unit test, ' + GE.timeStamp() + '\n')
        print '\nStart of ' + testName + ' unit test section, ' + TF.timeStamp() + '\n'
    
    def test_GlobalNav(self):
        driver = self.driver
        driver.get(base_url)
        
        # This checks the model dropdown menus.
        for NAME, SECTION, ELEMENT, URL in GE.MODEL_LIST:
            TF.ModelMenuNav(NAME, SECTION, ELEMENT, URL)
                
        # This checks the dropdown menus that are not part of the model section.
        for NAME, SECTION, ELEMENT, URL in GE.NON_MODEL_MENU_LIST:
            TF.NonModelMenuNav(NAME, SECTION, ELEMENT, URL)

        # This checks links in the global nav that are not in drop down menus.
        for NAME, ELEMENT, URL in GE.ONE_CLICK_BUTTONS:
            TF.OneClickMenuNav(NAME, ELEMENT, URL)

        # This checks the Lexus Search box by sending it a word or words and performing a search.
        for SEARCH_WORD in GE.LEXUS_SEARCH_WORDS:
            TF.LexusSearchNav(SEARCH_WORD)
            

    def tearDown(self):
        self.driver.quit()
        print '\n' + 'END OF unit test section: ' + TF.timeStamp() 

if __name__ == "__main__":
    unittest.main()