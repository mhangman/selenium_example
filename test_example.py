from webdriver import *


class TestAmazonExample(WebDriverBase):
    HOME_CATEGORY_LOCATOR = (By.CSS_SELECTOR, "#desktop-top .as-title-block-left")
    SEARCH_BOX_LOCATOR = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON_LOCATOR = (By.CLASS_NAME, "nav-search-submit")
    SEARCHED_PRODUCTS_LOCATOR = (By.CSS_SELECTOR, ".s-result-list .a-text-normal")

    def __init__(self):
        super().__init__()
        self.init_driver()
        self.driver.get("https://www.amazon.com.tr/")
        self.test_category()
        self.test_search_product("Ayakkabı")
        self.driver.quit()

    def test_category(self):
        first_category = self.get_element(self.HOME_CATEGORY_LOCATOR)
        assert first_category.text == "Amazon'u keşfet"

    def test_search_product(self, product_name):
        search_box = self.get_element(self.SEARCH_BOX_LOCATOR)
        search_box.send_keys(product_name)
        self.get_element(self.SEARCH_BUTTON_LOCATOR).click()
        searched_product_title = self.get_element(self.SEARCHED_PRODUCTS_LOCATOR)
        assert product_name in searched_product_title.text


if __name__ == '__main__':
    TestAmazonExample()
    print("TEST OK")