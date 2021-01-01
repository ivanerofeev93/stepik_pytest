import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

class TestBookShop():

    def test_addtocart_button_presence(self, browser):
        browser.get(link)
        time.sleep(5)
        button = browser.find_element_by_class_name("btn-add-to-basket")
        assert button