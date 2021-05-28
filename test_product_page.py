from .pages.product_page import ProductPage
import pytest
import time

urls = [
    '?promo=offer0', '?promo=offer1', '?promo=offer2',
    '?promo=offer3', '?promo=offer4', '?promo=offer5',
    '?promo=offer6', pytest.param('?promo=offer7', marks=pytest.mark.xfail),
    '?promo=offer8', '?promo=offer9'
]

@pytest.mark.parametrize('url', urls)
def test_guest_can_add_product_to_basket(browser, url):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{url}"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_product_added_to_basket()
    page.should_disappear_message()
    page.should_be_message_basket_total()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_disappear_message()