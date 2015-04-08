from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchWindowException, NoSuchElementException
from webdriver_config import wd
from runscript_globalnav import base_url
import time




# This function compares the output to the content in the list and throws a pass/fail if the content matches or not.
def matchIt(x, y):
    if x != y:
        return "FAIL//////////\\\\\\\\\\!!!!!!!!!!//////////\\\\\\\\\\!!!!!!!!!!//////////\\\\\\\\\\!!!!!!!!!!//////////\\\\\\\\\\!!!!!!!!!!"
    elif x == y:
        return "PASS"
# ==================================================================================================
# ==================================================================================================
# If base_url has "Staging" in it, we need to remove the authentication info to compare the expected 
# and actual URLs.  This function does that for us.
def real_url(x):
    if "staging" in x:
        return x[0:7] + x[27:]
    else:
        return x
# ==================================================================================================
# ==================================================================================================
# returns the current date and time for creating the file to print data to.
import datetime
def currentTime():
    return datetime.datetime.now().strftime('%m-%d-%y, %H%M%S')

# returns the current date and time in a more readable format to be printed in the file.
def timeStamp():
    return datetime.datetime.now().strftime('%m/%d/%y, %H:%M:%S')


# ==================================================================================================
# ==================================================================================================
# ==================================================================================================
# ==================================================================================================
waitTime = 15
timeSleep = 4
driver = wd
wait = WebDriverWait(driver, waitTime)
# ==========================================================================
# commands to handle iPerceptions pop up, if needed.  If this is to be implemented into the code, it needs to be wrapped 
# in a try/except, since it only appears one time during each test.
# This is for the pop up that appears after a couple loads of the site.  I refactored the code so this is no longer 
# in it, because it slowed the tests considerably.  However, as is, the code only works in Firefox, because Chrome 
# throws an error if this survey appears on the page.
# SURVEY_POPUP_NO_BUTTON = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='IPEinvL']/map/area[2]")))
# SURVEY_POPUP_NO_BUTTON.click()
# print "Survey pop up displayed and \nthe 'No' button was clicked."
# ==========================================================================

def ModelMenuNav(w,x,y,z):
    MENU_SECTION = wait.until(EC.element_to_be_clickable((By.XPATH, x))) # SECTION should go here
    MENU_SECTION.click()

    # attempting to execute javascript to resolve IE issue with dropdowns disappearing 
    # too quickly and forcing test 1 to fail.
    # driver.execute_script('id="category_Sedans"')
    
    # Below is another possible fix being investigated for IE dropdown issue using ActionChains module import. 
    # This attempts to hover the mouse over the element.
    # hover = ActionChains(driver).move_to_element(MENU_SECTION)
    # hover.perform()
    MENU_NAV = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, y))) # ELEMENT should go here
    
    # Part of ActionChains module import for IE dropdown issue fix.
    # hover = ActionChains(driver).move_to_element(MENU_NAV)
    # hover.perform()
    
    MENU_NAV.click()
    
    # It's not good to use time.sleep() in selenium scripts, however in this instance it appears to be 
    # an acceptable execution, as it is allowing the below print statments to be triggered after the 
    # above click.  Without a time delay, the print statements were occasionally printing the content 
    # before the menu click was fully executed, thus not providing accurate info.
    time.sleep(timeSleep)
    print '  Model Name: ' + w  # NAME should go here
    print 'actual Title: ' + driver.title
    print 'expected URL: ' + real_url(base_url)  + z  # URL should go here
    print '  actual URL: ' + driver.current_url
    print '   URL Match: ' + matchIt(real_url(base_url) + z, driver.current_url) + '\n'  # URL should go here
    driver.get(base_url)

    '''
    try:
    except NoSuchElementException, TimeoutException:
        print "Error found while checking " + w
        print "Investigate web page and check script for possible errors."
    '''

def NonModelMenuNav(w,x,y,z):
    MENU_SECTION = wait.until(EC.element_to_be_clickable((By.ID, x))) # SECTION should go here
    MENU_SECTION.click()
    MENU_NAV = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, y))) # ELEMENT should go here
    MENU_NAV.click()
    
    try:
        time.sleep(timeSleep)
        aw = driver.window_handles
        # wait.until((EC.title_contains, NAME(aw[1])))
        
        # This switches the selenium controls from the main (default) window to the newly opened 
        # window, only if a new window was opened from the menu click.
        driver.switch_to_window(aw[1])
        print ' Button Name: ' + w  # NAME should go here
        print 'Actual Title: ' + driver.title
        print 'Expected URL: ' +  z  # URL should go here
        print '  Actual URL: ' + driver.current_url
        print '   URL Match: ' + matchIt(z, driver.current_url) + '\n'  # URL should go here
        time.sleep(1)
        driver.close()
        # This switches selenium controls back to the main (default) window.
        driver.switch_to_window(aw[0])
        #driver.switch_to_default_content()
        
    except (IndexError, TimeoutException, NoSuchWindowException):
        time.sleep(timeSleep)
        print ' Button Name: ' + w # Name should go here
        print 'Actual Title: ' + driver.title
        print 'Expected URL: ' + real_url(base_url)  + z  # URL should go here
        print '  Actual URL: ' + driver.current_url
        print '   URL Match: ' + matchIt(real_url(base_url)  + z, driver.current_url) + '\n'  # URL should go here
        driver.get(base_url)
    
    # finally:
        # driver.get(base_url)


def OneClickMenuNav(x, y, z):
    MENU_NAV = wait.until(EC.element_to_be_clickable((By.XPATH, y)))  # ELEMENT should go here
    MENU_NAV.click()
    time.sleep(timeSleep)
    print ' Button Name: ' + x  # NAME should go here
    print 'Actual Title: ' + driver.title
    print 'Expected URL: ' + real_url(base_url)  + z  # URL should go here
    print '  Actual URL: ' + driver.current_url
    print '   URL Match: ' + matchIt(real_url(base_url)  + z, driver.current_url) + '\n'  # URL should go here
    driver.get(base_url)


def LexusSearchNav(search_word):
    NAME = 'Lexus Nav Search Field'
    ELEMENT = 'nav_search_field'
    URL1 = '/solr/search_lexus.jsp?qt='
    URL2 = '&col=lexus'

    SEARCH_BOX = wait.until(EC.element_to_be_clickable((By.ID, ELEMENT)))
    SEARCH_BOX.click()
    SEARCH_BOX.send_keys(search_word)
    SEARCH_BOX.send_keys(Keys.RETURN)
    time.sleep(timeSleep)
    # This makes the search word appear correctly in the search results URL so it 
    # can be matched with the actual URL correctly.
    SEARCH_WORD_v2 = search_word.replace(' ', '+')
    print "Lexus Search Field under test."
    print "Text entered into search: " + search_word
    print ' Button Name: ' + NAME
    print 'Actual Title: ' + driver.title
    print 'Expected URL: ' + real_url(base_url)  + URL1 + SEARCH_WORD_v2 + URL2
    print '  Actual URL: ' + driver.current_url
    print '   URL Match: ' + matchIt(real_url(base_url)  + URL1 + SEARCH_WORD_v2 + URL2, driver.current_url) + '\n'            
    driver.get(base_url)
