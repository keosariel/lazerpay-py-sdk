from lazerpay import Lazerpay
import asyncio


lazerpay = Lazerpay(public_key=public_key, secret_key=secret_key)

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

print(lazerpay)

async def test_create_link():
    # pq9pgb
    data = await lazerpay.payment_links.create_payment_link(transaction_payload)
    print(data)

async def test_get_links():
    data = await lazerpay.payment_links.get_all_paymentlinks()
    print(data)

async def test_update_links():
    transaction_payload = {
        "identifier": "pq9pgb",
        "status": "active"
    }
    data = await lazerpay.payment_links.update_payment_link(transaction_payload)
    print(data)

async def test_get_link():
    data = await lazerpay.payment_links.get_paymentlink('pq9pgb')
    print(data)

async def test_init_pay():
    transaction_payload = {
      'reference': 'dsvjvdds', 
      'customer_name': 'Njoku Emmanuel',
      'customer_email': 'kalunjoku123@gmail.com',
      'coin': 'BUSD', 
      'currency': 'USD', 
      'amount': 100,
      'accept_partial_payment': True,
    }
    data = await lazerpay.payment.initialize_payment(transaction_payload)
    print(data)

async def test_verify_pay():
    transaction_payload = {
      'identifier': '0xa523F92BBF59bB19FCc7020A7e9004A05B697C25', 
    }
    data = await lazerpay.payment.confirm_payment(transaction_payload)
    print(data)


# 0xa523F92BBF59bB19FCc7020A7e9004A05B697C25

async def test_misc():
    data = await lazerpay.misc.test_get_links()
    print(data)


if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.run_until_complete(test_misc())