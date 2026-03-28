from abc import ABC, abstractmethod


# =========================
# Abstraction
# =========================
class PaymentMethod(ABC):
    """
    Abstract Base Class
    Defines the interface that all payment methods must implement.
    """

    def __init__(self, amount: float):
        self._amount = amount  # protected attribute

    @abstractmethod
    def pay(self) -> None:
        pass

    @abstractmethod
    def refund(self) -> None:
        pass


# =========================
# Encapsulation
# =========================
class CardDetails:
    """
    Encapsulates sensitive card data.
    Direct access is restricted.
    """

    def __init__(self, card_number: str, cvv: str):
        self.__card_number = card_number  # private
        self.__cvv = cvv                  # private

    def get_masked_card(self) -> str:
        return f"**** **** **** {self.__card_number[-4:]}"


# =========================
# Inheritance + Polymorphism
# =========================
class CreditCardPayment(PaymentMethod):
    def __init__(self, amount: float, card_details: CardDetails):
        super().__init__(amount)
        self.card_details = card_details

    def pay(self) -> None:
        print(
            f"[CreditCard] Charging ₹{self._amount} "
            f"using card {self.card_details.get_masked_card()}"
        )

    def refund(self) -> None:
        print(
            f"[CreditCard] Refunding ₹{self._amount} "
            f"to card {self.card_details.get_masked_card()}"
        )


class UPIPayment(PaymentMethod):
    def __init__(self, amount: float, upi_id: str):
        super().__init__(amount)
        self.upi_id = upi_id

    def pay(self) -> None:
        print(f"[UPI] Paying ₹{self._amount} via UPI ID {self.upi_id}")

    def refund(self) -> None:
        print(f"[UPI] Refunding ₹{self._amount} to UPI ID {self.upi_id}")


class CryptoPayment(PaymentMethod):
    def __init__(self, amount: float, wallet_address: str):
        super().__init__(amount)
        self.wallet_address = wallet_address

    def pay(self) -> None:
        print(
            f"[Crypto] Transferring ₹{self._amount} "
            f"to wallet {self.wallet_address}"
        )

    def refund(self) -> None:
        print(
            f"[Crypto] Refunds not supported for wallet {self.wallet_address}"
        )


# =========================
# Polymorphic Function
# =========================
def process_payment(payment: PaymentMethod) -> None:
    """
    Works with ANY payment type.
    This is polymorphism in action.
    """
    payment.pay()


# =========================
# Usage Example
# =========================
if __name__ == "__main__":
    card = CardDetails("1234567812345678", "123")

    payments = [
        CreditCardPayment(2500.0, card),
        UPIPayment(1500.0, "user@upi"),
        CryptoPayment(5000.0, "0xA1B2C3D4"),
    ]

    for payment in payments:
        process_payment(payment)
        payment.refund()
        print("-" * 40)
