from selenium import webdriver
from fixture.session import SessionHelper

class Application:
    def __init__(self, browser, base_url):
            if browser == "firefox":
                self.wd = webdriver.Firefox(capabilities={"marionette": False})
            elif browser == "chrome":
                self.wd = webdriver.Chrome()
            elif browser == "IE":
                self.wd = webdriver.Ie()
            else:
                raise ValueError("Unrecognized browser %s" % browser)
            self.base_url = base_url
            self.session = SessionHelper(self)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url()
            return True
        except:
            return False