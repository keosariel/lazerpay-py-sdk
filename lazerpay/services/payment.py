from dataclasses import dataclass
from ..utils import validate_params
from .._http_client import HTTPClient

@dataclass
class TransactionData:
    reference : str  
    amount    : str
    customer_name  : str
    customer_email : str
    coin      : str
    currency  : str
    accept_partial_payment : bool


class Payment:

    def __init__(self, headers, init_url, confirm_url):
        self.headers  = headers
        self.init_url = init_url
        self.confirm_url =  confirm_url
        

    async def initialize_payment(self, payload):
        """
        The initialize payment endpoint allows you to initiate payment 
        directly to Lazerpay by passing in the transaction details

        :param payload: Fields needed to initialize a payment
        :type  payload: Dict()

        More info: https://docs.lazerpay.finance/home/payments/accept-payments
        """

        validate_params(TransactionData.__dataclass_fields__.keys(), payload.keys())

        async with HTTPClient(self.init_url, headers=self.headers) as session:
            response, json_data = await session.requests("POST", json=payload)
            return json_data

        
    async def confirm_payment(self, payload):
        """ 
        Confirms/Verify's a Lazerpay transaction

        :param payload: Fields needed to verify/confirm a transaction
        :type  payload: Dict()

        More info: https://docs.lazerpay.finance/home/payments/verify-payments
        """
        
        keys = ["identifier"]
        validate_params(keys, payload.keys())

        async with HTTPClient(self.confirm_url + "/" + payload.get("identifier"), headers=self.headers) as session:
            response, json_data = await session.requests("GET", json=payload)
            return json_data
