from lazerpay import Lazerpay
import asyncio
import unittest

def async_test(async_func):
    def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(async_func(*args, **kwargs))
    return wrapper

class TestLazerpayClient(unittest.TestCase):

    lazerpay = Lazerpay(public_key=PUBLIC_KEY, secret_key=SECRET_KEY)

    @async_test
    async def test_paymentlink(self):
        transaction_payload = {
            'title': 'Njoku Test',
            'description': 'Testing this sdk',
            'logo':
            'https://assets.audiomack.com/fireboydml/bbbd8710eff038d4f603cc39ec94a6a6c2c5b6f4100b28d62557d10d87246f27.jpeg?width=340&height=340&max=true',
            'currency': 'USD',
            'type': 'standard',
            'amount': 100, 
            'redirect_url': "https://keosariel.github.io"
        }
        data = await self.lazerpay.payment_links.create_payment_link(transaction_payload)
        self.assertEqual(type(data), dict)

        if data.get("statusCode") == 201:

            # Update payment link
            transaction_payload = {
                "identifier": data["data"].get("reference"),
                "status": "inactive"
            }
            data = await self.lazerpay.payment_links.update_payment_link(transaction_payload)
            self.assertEqual(type(data), dict)

            # Get Link
            data = await self.lazerpay.payment_links.get_paymentlink(data["data"].get("reference"))
            self.assertEqual(type(data), dict)
		
    @async_test
    async def test_get_paymentlinks(self):
        data = await self.lazerpay.payment_links.get_all_paymentlinks()
        self.assertEqual(type(data), dict)

    @async_test
    async def test_payment(self):
        transaction_payload = {
            'reference': 'TEST_REFERENCE1', 
            'customer_name': 'Njoku Emmanuel',
            'customer_email': 'kalunjoku123@gmail.com',
            'coin': 'BUSD', 
            'currency': 'USD', 
            'amount': 100,
            'accept_partial_payment': True,
        }
        data = await self.lazerpay.payment.initialize_payment(transaction_payload)
        self.assertEqual(type(data), dict)

        if data.get("statusCode") == 201:
            transaction_payload = {
                'identifier': data["data"].get("address"), 
            }
            data = await self.lazerpay.payment.confirm_payment(transaction_payload)
            self.assertEqual(type(data), dict)

if __name__ == "__main__":
	unittest.main()