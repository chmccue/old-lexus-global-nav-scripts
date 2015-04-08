from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# ==================================================================================================
# ==================================================================================================
# To set certain option settings in Chrome Driver.
'''
chrome_options = Options()
chrome_options.add_argument("--test-type")
chrome_options.add_argument("--disable-extensions")
# wd = webdriver.Chrome()
wd = webdriver.Chrome(chrome_options=chrome_options)
'''
# ==================================================================================================
# ==================================================================================================
# Firefox preference controls
'''
profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", "<enter proxy here>")
profile.set_preference("network.proxy.http_port", 80)
profile.set_preference("network.proxy.no_proxies_on", "")
profile.update_preferences()
wd = webdriver.Firefox(firefox_profile=profile)
'''
# ==================================================================================================
# ==================================================================================================

wd = webdriver.Firefox()
# wd_Chrome = webdriver.Chrome()
# wd_Firefox = webdriver.Firefox()
# wd_IE = webdriver.Ie()

'''
# controls for Selenium Grid, using Desired Capabilities.  They need to be better structured.
wd = webdriver.Remote(
command_executor='http://127.0.0.1:4443/wd/hub',
desired_capabilities=DesiredCapabilities.FIREFOX)
'''
