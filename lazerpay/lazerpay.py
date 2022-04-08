from .services import Payment, PaymentLinks, Misc
from .utils import (
    API_URL_INIT_TRANSACTION,
    API_URL_CONFIRM_TRANSACTION,
    API_URL_GET_ACCEPTED_COINS,
    API_URL_TRANSFER_FUNDS,
    API_URL_PAYMENT_LINK  
)

class Lazerpay:
    
    def __init__(self, public_key, secret_key, headers={}):
        """
        Instantiate the client.
        :param public_key: Your Lazerpay PUBLIC-KEY.
        :type  public_key: String
        :param secret_key: Your Lazerpay SECRET-KEY.
        :type  secret_key: String
        """

        if not public_key:
            raise Exception("Lazerpay `public_key`  is required")
        
        if not secret_key:
            raise Exception("Lazerpay `secret_key` is required")

        self.public_key = public_key
        self.secret_key = secret_key

        self._headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            **headers,
        }

        self.payment = Payment(self.headers, init_url=API_URL_INIT_TRANSACTION, confirm_url=API_URL_CONFIRM_TRANSACTION)
        self.payment_links = PaymentLinks(self.headers, payment_link_url=API_URL_PAYMENT_LINK)
        self.misc = Misc(headers, API_URL_GET_ACCEPTED_COINS)
        
    @property
    def _get_auth_headers(self):
        """Helper method to get auth headers."""

        headers =  {
            "x-api-key": self.public_key,
            "Authorization": f"Bearer {self.secret_key}",
        }
        return headers
    
    @property
    def headers(self):
        return {
            **self._headers,
            **self._get_auth_headers
        }