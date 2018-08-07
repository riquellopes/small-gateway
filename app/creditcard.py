# coding: utf-8
import re
import luhnpy
from enum import Enum


class Brands(Enum):
    VISA = "Visa"
    MASTERCARD = "Mastercard"
    UNKNOWN = "Unknown"


class Visa:

    @staticmethod
    def is_(number):
        return re.match(r"^4(?!38935|51416|576|011)\d+", number) is not None


class MasterCard:

    @staticmethod
    def is_(number):
        return re.match(r"^5(?!0)\d+", number) is not None


class CreditCard:
    """
        credit_card = CreditCard("4114047196786871")
        credit_card.is_valid()
        credit_card.brand()
    """

    def __init__(self, number):
        self._number = re.sub(r"[^\d+]", "", number or "")

    def is_valid(self):
        return (
            self._number.isdigit() and
            (len(self._number) > 0 and int(self._number) > 0) and

            # https://github.com/mfuentesg/luhnpy
            luhnpy.verify(self._number)
        )

    def brand(self):
        if self.is_valid() is False:
            return Brands.UNKNOWN

        if Visa.is_(self._number):
            return Brands.VISA

        if MasterCard.is_(self._number):
            return Brands.MASTERCARD
        return Brands.UNKNOWN
