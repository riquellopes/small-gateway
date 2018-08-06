from app.schemas.request import CardSchema


def test_get_3_errors_when_data_is_empty():
    result = (CardSchema()).load({})

    assert result.errors['number']
    assert result.errors['expiration_date']
    assert result.errors['cvv']


def test_the_errors_should_be_empty_when_all_fields_is_fill():
    result = (CardSchema()).load({
        "number": "4114047196786871",
        "expiration_date": "10/2070",
        "cvv": "378",
        "holder_name": "Henrique Lopes"
    })

    assert result.errors == {}


def test_get_error_when_set_a_invalid_expiration_date():
    result = (CardSchema()).load({
        "number": "4114047196786871",
        "expiration_date": "10/20",
        "cvv": "378",
        "holder_name": "Henrique Lopes"
    })

    assert result.errors['expiration_date'][0] == "The expiration_date isn't valid date."


def test_get_error_when_holder_name_is_filled_in_just_with_first_name():
    result = (CardSchema()).load({
        "number": "4114047196786871",
        "expiration_date": "10/2050",
        "cvv": "378",
        "holder_name": "Henrique"
    })

    assert result.errors['holder_name']
