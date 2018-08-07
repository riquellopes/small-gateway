from app.creditcard import CreditCard, Brands


def test_get_true_for_visa_card():
    credit_card = CreditCard("4114047196786871")

    assert credit_card.is_valid()
    assert credit_card.brand() == Brands.VISA


def test_get_true_even_with_blank_space():
    credit_card = CreditCard("411 4047 1967 868 71")

    assert credit_card.is_valid()
    assert credit_card.brand() == Brands.VISA


def test_get_false_and_unknow_for_any_number():
    credit_card = CreditCard("xxxxaa")

    assert credit_card.is_valid() is False
    assert credit_card.brand() == Brands.UNKNOWN


def test_get_false_when_setting_none_number():
    credit_card = CreditCard(None)

    assert credit_card.is_valid() is False
    assert credit_card.brand() == Brands.UNKNOWN


def test_get_true_for_mastercard():
    credit_card = CreditCard("5558078345914460")

    assert credit_card.is_valid()
    assert credit_card.brand() == Brands.MASTERCARD


def test_brand_method_should_get_unknown_for_brands_without_support():
    credit_card = CreditCard("6062829888053968")

    assert credit_card.is_valid()
    assert credit_card.brand() == Brands.UNKNOWN
