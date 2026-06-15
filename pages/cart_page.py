from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):

    def check_no_product_in_cart(self):
        assert self.is_not_element_present(
            *CartPageLocators.CONTAINER_PRODUCTS), "появился блок товаров, хотя быть не должно"

    def check_present_message_basket_is_empty(self):
        assert self.is_element_present(
            *CartPageLocators.MESSAGE_BASKET_IS_EMPTY), "отсутсвует сообщение о пустой корзине"

    def check_message_basket_is_empty(self):
        message = self.browser.find_element(*CartPageLocators.MESSAGE_BASKET_IS_EMPTY).text
        assert "Your basket is empty." in message, "в сообщении о пустой корзине нет Your basket is empty."
