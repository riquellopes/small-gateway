from .factories import PaymentFactory, BoletoPaymentFactory


def test_when_boleto_payment_code_get_the_boleto_number(boleto):
    pay = BoletoPaymentFactory.create(
        type=boleto,

        id=1,
        amount=50,
    )

    assert pay.code == "000001"


def test_when_creditcard_payment_code_get_is_none(credit_card):
    pay = PaymentFactory.create(
        type=credit_card,

        id=2,
        amount=50,
    )

    assert pay.code is None
