from dataclasses import dataclass
from ..utils import validate_params
from .._http_client import HTTPClient


@dataclass
class PaymentLinkData:
    title : str
    description  :str
    logo  :str
    redirect_url :str
    amount    :str
    currency  :str
    type :str


class PaymentLinks:

    def __init__(self, headers, payment_link_url):
        self.headers = headers
        self.payment_link_url = payment_link_url

    async def create_payment_link(self, payload):
        """
        Creates a new Lazerpay payment link

        :param payload: Fields needed to create a payment link
        :type  payload: Dict()

        More info: https://docs.lazerpay.finance/home/payments/payment-links
        """

        validate_params(PaymentLinkData.__dataclass_fields__.keys(), payload.keys())

        async with HTTPClient(self.payment_link_url, headers=self.headers) as session:
            response, json_data = await session.requests("POST", json=payload)
            return json_data

        
    async def update_payment_link(self, payload):
        """ 
        Confirms/Verify's a Lazerpay transaction

        :param payload: Fields needed to verify/confirm a transaction
        :type  payload: Dict()

        More info: https://docs.lazerpay.finance/home/payments/verify-payments
        """
        keys = ["identifier", "status"]

        async with HTTPClient(self.payment_link_url+"/"+payload.get("identifier"), headers=self.headers) as session:
            response, json_data = await session.requests("PUT", json=payload)
            return json_data  

    async def get_all_paymentlinks(self):
        """Gets all payment links from your account"""

        async with HTTPClient(self.payment_link_url, headers=self.headers) as session:
            response, json_data = await session.requests("GET")
            return json_data  

    async def get_paymentlink(self, identifier):
        """
        Gets the payment link with the specified
        `identifier`
        
        :type identifier: string
        """
        
        async with HTTPClient(self.payment_link_url+"/"+identifier, headers=self.headers) as session:
            response, json_data = await session.requests("GET")
            return json_data        