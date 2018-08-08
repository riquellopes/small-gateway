from .factories import CreditCardPaymentFactory, BoletoPaymentFactory


def test_when_boleto_payment_code_get_the_boleto_number(boleto):
    pay = BoletoPaymentFactory(
        type=boleto,

        id=1,
    )

    assert pay.code == "000001"


def test_when_creditcard_payment_code_get_is_none(credit_card):
    pay = CreditCardPaymentFactory(
        type=credit_card
    )

    assert pay.code is None
