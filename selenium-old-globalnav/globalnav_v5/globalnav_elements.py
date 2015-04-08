'''
This file is for stored variables and lists to be used with the runscript_globalnav.py file.
This is only a supporting file; to run the script, please run via runscript_globalnav.py file 
with this file in the same directory.
'''

# ==================================================================================================
# ==================================================================================================
# ==================================================================================================
# Content for the specific models in nav.
# <MODEL> = List of items: 
# 1st item is model/unofficial button name.
# 2nd item is XPATH for the broader section that the model belongs to (eg: SEDANS, SUVS, HYBRIDS, etc).
# 2nd item must be encased in a driver.find_element(By.XPATH, <content in 2nd item>).
# 3rd item is the CSS SELECTOR element data for the specific model. 
# 3rd item must be encased in a driver.find_element(By.CSS_SELECTOR, <content in 3rd item>).
# 4th item is plain text of  model URL to be combined with base_url 
# (eg:  base_url + <MODEL>_URL) to display expected URL to compare against the actual URL.


# Sedans section
SEDANS = '//span[contains(text(), "Sedans")]'  #XPATH locator
IS = ['Lexus IS', SEDANS, "img[alt=\'Lexus IS\']", "/models/IS"]
ES = ['Lexus ES', SEDANS, "img[alt=\'Lexus ES\']", "/models/ES"]
GS = ['Lexus GS', SEDANS, "img[alt=\'Lexus GS\']", "/models/GS"]
LS = ['Lexus LS', SEDANS, "img[alt=\'Lexus LS\']", "/models/LS"]


'''
# This is an alternative sedan list where the sub menu sections are located by XPATH.
# Sedans section
SEDANS = ".//*[@id='categories']/li[1]/span"  #XPATH locator
IS = ['Lexus IS', SEDANS, ".//*[@id='category_Sedans']/a[1]/div/img", "/models/IS"]
ES = ['Lexus ES', SEDANS, ".//*[@id='category_Sedans']/a[2]/div/img", "/models/ES"]
GS = ['Lexus GS', SEDANS, ".//*[@id='category_Sedans']/a[3]/div/img", "/models/GS"]
LS = ['Lexus LS', SEDANS, ".//*[@id='category_Sedans']/a[4]/div/img", "/models/LS"]
'''
# SUVs section
SUVS = '//span[contains(text(), "SUVs")]'  #XPATH locator
RX = ['Lexus RX', SUVS, "img[alt=\'Lexus RX\']", "/models/RX"]
GX = ['Lexus GX', SUVS, "img[alt=\'Lexus GX\']", "/models/GX"]
LX = ['Lexus LX', SUVS, "img[alt=\'Lexus LX\']", "/models/LX"]
# Convertibles section
CONVERTIBLES = '//span[contains(text(), "Convertibles")]'  #XPATH locator
ISC = ['Lexus IS C', CONVERTIBLES, "img[alt=\'Lexus IS C\']", "/models/ISC"]
# Hybrids section
HYBRIDS = '//span[contains(text(), "Hybrids")]'  #XPATH locator
CTh = ['Lexus CT Hybrid', HYBRIDS, "img[alt=\'Lexus CT HYBRID\']", "/models/CT-hybrid"]
RXh = ['Lexus RX Hybrid', HYBRIDS, "img[alt=\'Lexus RX HYBRID\']", "/models/RX-hybrid"]
ESh = ['Lexus ES Hybrid', HYBRIDS, "img[alt=\'Lexus ES HYBRID\']", "/models/ES-hybrid"]
GSh = ['Lexus GS Hybrid', HYBRIDS, "img[alt=\'Lexus GS HYBRID\']", "/models/GS-hybrid"]
LSh = ['Lexus LS Hybrid', HYBRIDS, "img[alt=\'Lexus LS HYBRID\']", "/models/LS-hybrid"]
# F Performance section
F_PERFORMANCE = '//span[contains(text(), "F Performance")]'  #XPATH locator
ISF = ['Lexus IS F', F_PERFORMANCE, "img[alt=\'Lexus IS F\']", "/models/ISF"]
LFA = ['Lexus LFA',  F_PERFORMANCE, "img[alt=\'Lexus LFA\']", "/models/LFA/"]
F_FSPORT = ['Lexus F/F Sport', F_PERFORMANCE, "img[alt=\'Lexus F/F SPORT\']", "/performance/#/performance/overview/"]
# Future section
FUTURE = '//span[contains(text(), "Future")]'  #XPATH locator
LFLC = ['Lexus LF-LC', FUTURE, "img[alt=\'Lexus LF-LC\']", "/concept/"]
NX = [  'Lexus NX',    FUTURE, "img[alt=\'Lexus NX\']", "/concept/NX/"]
RC = [  'Lexus RC',    FUTURE, "img[alt=\'Lexus RC\']", "/concept/RC/index.html"]
RCF = [ 'Lexus RC F',  FUTURE, "img[alt=\'Lexus RC F\']", "/concept/RCF/index.html"]
CRAFTED_LINE = ['Lexus THE CRAFTED LINE', FUTURE, "img[alt=\'Lexus THE CRAFTED LINE\']", "/craftedline/"]

MODEL_LIST = [IS, ES, GS, LS, RX, GX, LX, ISC, CTh, 
              RXh, ESh, GSh, LSh, ISF, LFA, F_FSPORT, LFLC, NX, 
              RC, RCF, CRAFTED_LINE]

# ==================================================================================================
# ==================================================================================================
# ==================================================================================================
# Content for the specific dropdown sections in nav.
# <SECTION> = List of items: 
# 1st item is plain text of button name.
# 2nd item is ID locator for the section (eg: OWNERS_RESOURCES, etc).
# 2nd item must be encased in a driver.find_element(By.ID, <content in 2nd item>).
# 3rd item is the CSS SELECTOR element data for the specific button. 
# 3rd item must be encased in a driver.find_element(By.CSS_SELECTOR, <content in 3rd item>).
# 4th item is plain text of  model URL to be combined with base_url 
# (eg:  base_url + <MODEL>_URL) to display expected URL to compare against the actual URL. Exceptions may apply.

# Owner's Resources section
OWNERS_RESOURCES = "ownersDropButton"  #ID locator

MY_LEXUS = ["My Lexus", OWNERS_RESOURCES, "a[title=\'my lexus\']", "https://secure.drivers.lexus.com/lexusdrivers/my-lexus/home.do"]
OWNER_BENEFITS = ['Owner Benefits', OWNERS_RESOURCES, "a[title=\'owner benefits\']", "https://secure.drivers.lexus.com/lexusdrivers/benefits/home.do"]
PAY_MY_BILL = ['Pay My Bill', OWNERS_RESOURCES, "a[title=\'pay my bill\']", 'https://www.lexusfinancial.com/pub/home/']
LEXUS_ENFORM = ['Lexus Enform', OWNERS_RESOURCES, "a[title=\'lexus enform\']", 'https://secure.drivers.lexus.com/lexusdrivers/lexusenform/home.do'] 
SCHED_MAINT = ['Scheduled Maintenance', OWNERS_RESOURCES, "a[title=\'scheduled maintenance\']", 'https://secure.drivers.lexus.com/lexusdrivers/info/my-lexus/service/maintenance-schedule.do']
KNOWLEDGE_CENTER = ['Knowledge Center', OWNERS_RESOURCES, "a[title=\'knowledge center\']", '/contact/knowledge_center.html']
LEXUS_MAG = ['Lexus Magazine', OWNERS_RESOURCES, "a[title=\'lexus magazine\']", 'https://secure.drivers.lexus.com/lexusdrivers/magazine/home.do']
LEXUS_NAVIGATION = ['Lexus Navigation', OWNERS_RESOURCES, "a[title=\'lexus navigation\']", 'http://www.lexusnavigation.com/']

# ==================================================================================================
# ==================================================================================================
# Certified Pre-Owned section
CPO = "navCPODropButton"  #ID locator

VEHICLE_SEARCH = ['Vehicle Search', CPO, "a[title=\'vehicle search\']", '/cpo/index.html']
CPO_OVERVIEW = ['CPO Overview', CPO, "a[title=\'cpo overview\']", '/cpo/overview/index.html']
VEHICLE_LIBRARY = ['Vehicle Library', CPO, "a[title=\'vehicle library\']", '/cpo/model_library/index.html']

# ==================================================================================================
# ==================================================================================================
# Shopping Tools section
SHOPPING_TOOLS = "shoppingTools"  #ID locator

FINANCIAL_SERVICES = ['Financial Services', SHOPPING_TOOLS, "a[title=\'financial services\']", 'https://www.lexusfinancial.com/pub/home/']
ACCESSORIES = ['Accessories', SHOPPING_TOOLS, "a[title=\'accessories\']", '/accessories/']
SPECIAL_OFFERS = ['Special Offers', SHOPPING_TOOLS, "a[title=\'special offers\']", 'http://www.yourlexusdealer.com/Los_Angeles_California/index.html']
SIGN_UP = ['Sign Up', SHOPPING_TOOLS, "a[title=\'sign up\']", 'https://ssl.lexus.com/request-newsletter']

NON_MODEL_MENU_LIST = [MY_LEXUS, OWNER_BENEFITS, PAY_MY_BILL, LEXUS_ENFORM, SCHED_MAINT, 
                       KNOWLEDGE_CENTER, LEXUS_MAG, LEXUS_NAVIGATION, VEHICLE_SEARCH, 
                       CPO_OVERVIEW, VEHICLE_LIBRARY, FINANCIAL_SERVICES, ACCESSORIES, 
                       SPECIAL_OFFERS, SIGN_UP]

# ==================================================================================================
# ==================================================================================================
# ==================================================================================================
# These are one click links on the page (a menu or dropdown doesn't need to be opened to access them).

# Content for the specific dropdown sections in nav.
# <SECTION> = List of items: 
# 1st item is plain text of button name.
# 2nd item is the element locator for the specific button. 
# 2nd item must be encased in a driver.find_element(By.<Locator type>, <content in 2nd item>).
# 3rd item is plain text of  model URL to be combined with base_url 
# (eg:  base_url + <MODEL>_URL) to display expected URL to compare against the actual URL. Exceptions may apply.

# Lexus logo that should always go to Lexus home page when clicked on.
# XPATH locator
LEXUS_LOGO =  ["Lexus logo", ".//*[@id='logo']/a", "/"]
# Build Your Lexus should go to http://www.lexus.com/models/allVehicles/
# XPATH locator
BYL = ["Build Your Lexus" ,'//a[contains(text(), "Build Your Lexus")]', "/models/allVehicles/index.html?BYL=1"]
# Find a Dealer should go to http://www.lexus.com/dealers
# XPATH locator
FAD = ['Find a Dealer' ,'//a[contains(text(), "Find a Dealer")]', '/dealers']
# All Vehicles should go to http://www.lexus.com/models
# XPATH locator
ALL_VEHICLES = ['All Vehicles', '//a[contains(text(), "All Vehicles")]', '/models']

ONE_CLICK_BUTTONS = [LEXUS_LOGO, BYL, FAD, ALL_VEHICLES]

# These are words that will be input into the search box and searched for on the site.
LEXUS_SEARCH_WORDS = ['Search this text', 'lexus IS', 'test this text', "owners"]

