from time import sleep


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_translations(browser, language, sleep_time):
    browser.get(url=link)
    sleep(sleep_time)   # 30 seconds by default, but this can be overridden in command line parameter
    button_text = browser.find_element_by_class_name(name="btn-add-to-basket").text

    if language == "en":
        assert button_text == "Add to basket"
    if language == "es":
        assert button_text == "Añadir al carrito"
    if language == "fr":
        assert button_text == "Ajouter au panier"
    if language == "ru":
        assert button_text == "Добавить в корзину"
#
