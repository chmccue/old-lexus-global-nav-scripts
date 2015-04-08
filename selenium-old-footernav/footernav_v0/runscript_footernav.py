import unittest
import footernav_elements as FE
from webdriver_config import wd

# ==================================================================================================
# ==================================================================================================
testName = 'Footer Nav' # Name of test will go here to populate test name fields in the test.
base_url = 'http://www.lexus.com'

# if origin.staging or staging environment is the url under test, use this as base_url to log in first:
# http://<login>:<password>@origin.staging.lexus.com
# (Input actual login and password of staging environment for <login> and <password>).
# ==================================================================================================
# ==================================================================================================

class FooterNav(unittest.TestCase):
    
    def setUp(self):
        self.driver = wd
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        # fileOut.write('\nStart of ' + testName + ' unit test, ' + timeStamp() + '\n')
        print '\nStart of ' + testName + ' unit test section, ' + FE.timeStamp() + '\n'
        
    def test_FooterNav(self):
        driver = self.driver
        driver.get(base_url)

        for NAME, ELEMENT, URL in FE.INFORMATION:
            FE.LOOP_COMMANDS(NAME, ELEMENT, URL)
            
        for NAME, ELEMENT, URL in FE.SHOPPING_TOOLS:
            FE.LOOP_COMMANDS(NAME, ELEMENT, URL)
            
        for NAME, ELEMENT, URL in FE.SERVICES:
            FE.LOOP_COMMANDS(NAME, ELEMENT, URL)
            
        for NAME, ELEMENT, URL in FE.ADDITIONAL_SITES:
            FE.LOOP_COMMANDS(NAME, ELEMENT, URL)
            
        for NAME, ELEMENT, URL in FE.SHARE_OPTIONS:
            FE.LOOP_COMMANDS(NAME, ELEMENT, URL)
                
        for NAME, ELEMENT, URL in FE.OTHER_LINKS:
            FE.LOOP_COMMANDS(NAME, ELEMENT, URL)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()