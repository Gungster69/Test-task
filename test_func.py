from Locators import Locators

class tests:
    def check_name_less_than_6(name):
        Locators.LOCATOR_USERNAME.send_keys("abcde")
        return Locators.LOCATOR_USERNAME
        a = input()

    def check_name_more_than_32(self):
        self = "abcdefghijklmnopqrstuvwxyzabcdefg"
        Locators.LOCATOR_USERNAME.send_keys(self)
        return self 
