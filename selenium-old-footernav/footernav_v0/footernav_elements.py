'''
Footer Nav list variables and functions for use in Footer Nav Selenium Webdriver Python script. 
Needs to be in the same path as the main script (footernav_v<version-number>) and the webdriver_config.py
script.

'''

# XPATH globals
XPATH_START = ".//*[@id='content']/footer/div[1]/div/div"
NUM_1 = "[1]"
NUM_2 = "[2]"
NUM_3 = "[3]"
NUM_4 = "[4]"
NUM_5 = "[5]"

# INFORMATION section
ABOUT = ['About', XPATH_START + NUM_1 + "/ul/li[1]/a", '/about/']
CONTACT = ["Contact", XPATH_START + NUM_1 + "/ul/li[2]/a", "/contact/"]
CAREERS = ["Careers", XPATH_START + NUM_1 + "/ul/li[3]/a", "https://tmm.taleo.net/careersection/10020/jobsearch.ftl?lang=en&portal=760160078"]
YOUR_PRIVACY_RIGHTS = ["Your Privacy Rights", XPATH_START + NUM_1 + "/ul/li[4]/a", "/privacy/"]
LEGAL_TERMS = ["Legal Terms", XPATH_START + NUM_1 + "/ul/li[5]/a", "/privacy/legal_terms.html"]
RECALLS = ["Safety Recalls & Service Campaigns", XPATH_START + NUM_1 + "[1]/ul/li[6]/a", "http://www.toyota.com/recall"]

INFORMATION = [ABOUT, CONTACT, CAREERS, YOUR_PRIVACY_RIGHTS, LEGAL_TERMS, RECALLS]


# SHOPPING TOOLS section
SPECIAL_OFFERS = ["Special Offers", XPATH_START + NUM_2 + "/ul[1]/li[1]/a", "http://www.yourlexusdealer.com/Los_Angeles_California/index.html"]
ACCESSORIES = ["Accessories", XPATH_START + NUM_2 + "/ul[1]/li[2]/a", "/accessories/"]
FINANCIAL_SERVICES = ["Financial Services", XPATH_START + NUM_2 + "/ul[1]/li[3]/a", "https://www.lexusfinancial.com/"]

SHOPPING_TOOLS = [SPECIAL_OFFERS, ACCESSORIES, FINANCIAL_SERVICES]


# SERVICES section
WARRANTY_PROTECTION = ["Warranty & Protection", XPATH_START + NUM_2 + "/ul[2]/li[1]/a", "/warranty"]
SERVICE_MAINT = ["Service & Maintenance", XPATH_START + NUM_2 + "/ul[2]/li[2]/a", "/service"]
OWNER_RESOURCES = ["Owner's Resources", XPATH_START + NUM_2 + "/ul[2]/li[3]/a", "https://secure.drivers.lexus.com/lexusdrivers/home"]

SERVICES = [WARRANTY_PROTECTION, SERVICE_MAINT, OWNER_RESOURCES]


# ADDITIONAL SITES section
CPO = ["Certified Pre-Owned", XPATH_START + NUM_3 + "/ul/li[1]/a", "/cpo/"]
LUXURY_AWAITS = ["Luxury Awaits", XPATH_START + NUM_3 + "/ul/li[2]/a", "http://www.luxuryawaits.com"]
VIDA_LEXUS = ["Vida Lexus", XPATH_START + NUM_3 + "/ul/li[3]/a", "http://www.vidalexus.com/"]
L_STUDIO = ["L Studio", XPATH_START + NUM_3 + "/ul/li[4]/a", "http://www.lstudio.com/"]
LEXUS_MERCH = ["Lexus Merchandise", XPATH_START + NUM_3 + "/ul/li[5]/a", "http://www.thelexuscollection.com/ecommerce/secure/merchandise_landing.do?menu_id=114637&p=PcKVTUMWXvA%3D"]

ADDITIONAL_SITES = [CPO, LUXURY_AWAITS, VIDA_LEXUS, L_STUDIO, LEXUS_MERCH]


FACEBOOK = ["Facebook", XPATH_START + NUM_4 + "/ul[1]/li[1]/a", "https://www.facebook.com/lexus"]
TWITTER = ["Twitter", XPATH_START + NUM_4 + "/ul[1]/li[2]/a", "https://twitter.com/lexus"]
YOUTUBE = ["Youtube", XPATH_START + NUM_4 + "/ul[1]/li[3]/a", "http://www.youtube.com/user/LexusVehicles"]
INSTAGRAM = ["Instagram",  XPATH_START + NUM_4 + "/ul[1]/li[4]/a", "http://instagram.com/lexususa"]
GOOGLE = ["Google+", XPATH_START + NUM_4 + "/ul[1]/li[5]/a", 'https://plus.google.com/+Lexus/posts']

SHARE_OPTIONS = [FACEBOOK, TWITTER, YOUTUBE, INSTAGRAM, GOOGLE]


REQUEST_BROCHURE = ["Request a Printed Brochure", XPATH_START + NUM_4 + "/ul[2]/li[1]/a", 'https://ssl.lexus.com/request-brochure']
SIGN_UP = ["Sign Up", XPATH_START + NUM_4 + "/ul[2]/li[2]/a", 'https://ssl.lexus.com/request-newsletter']
AD_CHOICES = ["Ad Choices", XPATH_START + NUM_4 + "/ul[3]/li/a", 'http://info.evidon.com/pub_info/1762?v=1&nt=1&nw=false']

OTHER_LINKS = [REQUEST_BROCHURE, SIGN_UP, AD_CHOICES]


# ==================================================================================================
# ==================================================================================================
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
import datetime
# returns the current date and time for creating the file to print data to.
def currentTime():
    return datetime.datetime.now().strftime('%m-%d-%y, %H%M%S')

# returns the current date and time in a more readable format to be printed in the file.
def timeStamp():
    return datetime.datetime.now().strftime('%m/%d/%y, %H:%M:%S')
# ==================================================================================================
# ==================================================================================================
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException, NoSuchWindowException
from webdriver_config import wd
from runscript_footernav import base_url
from selenium.webdriver.support.ui import WebDriverWait

def LOOP_COMMANDS(x, y, z):
    driver = wd
    waitTime = 10
    timeSleep = 5
    wait = WebDriverWait(driver, waitTime)
    # This command scrolls the page down to the Y (2nd number listed) coordinate below, via 
    # executing javascript on the page.  The command instructs the browser to go to the bottom 
    # of the page.
    driver.execute_script("window.scrollTo(0, 1000)")
    MENU_CLICK = wait.until(EC.element_to_be_clickable((By.XPATH, y))) # ELEMENT should go here
    MENU_CLICK.click()
    try:
        time.sleep(timeSleep)
        aw = driver.window_handles
        # This switches the selenium controls from the main (default) window to the newly opened 
        # window, only if a new window was opened from the menu click.
        driver.switch_to_window(aw[1])
        print ' Button Name: ' + x # NAME should go here
        print 'Actual Title: ' + driver.title
        print 'Expected URL: ' +  z # URL should go here
        print '  Actual URL: ' + driver.current_url
        print '   URL Match: ' + matchIt(z, driver.current_url) + '\n'  # URL should go here
        time.sleep(1)
        driver.close()
        # This switches selenium controls back to the main (default) window.
        driver.switch_to_window(aw[0])
        
    except (IndexError, TimeoutException, NoSuchWindowException):
        time.sleep(timeSleep)
        print ' Button Name: ' + x  # NAME should go here
        print 'Actual Title: ' + driver.title
        print 'Expected URL: ' + real_url(base_url)  + z # URL should go here
        print '  Actual URL: ' + driver.current_url
        print '   URL Match: ' + matchIt(real_url(base_url)  + z, driver.current_url) + '\n'  # URL should go here
        driver.get(base_url)
