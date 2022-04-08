# Lazerpay v1 Python SDK

## How to use

`pip install lazerpay-sdk`

```py
from lazerpay import Lazerpay

lazerpay = Lazerpay(LAZER_PUBLIC_KEY, LAZER_SECRET_KEY)
```

Use TEST API keys for testing, and LIVE API keys for production

## Lazerpay Methods exposed by the sdk

1. **Payment**
   * Initialize Payment
   * Confirm Payment
  
2. **Payout**
   * Crypto Payout
   * Bank Payout ~ This is coming to V2
  
3. **Payment Links**
   * Create payment links
   * Get all payment links
   * Get a single payment link
   * Update a payment Link
  
4. **Misc**
   * Get all accepted coins

## Payment

**`Initialize Payment`**

This describes to allow your customers to initiate a crypto payment transfer.

```py
from lazerpay import Lazerpay

lazerpay = Lazerpay(LAZER_PUBLIC_KEY, LAZER_SECRET_KEY)

async def payment_tx():
   transaction_payload = {
      'reference': 'YOUR_REFERENCE', # Replace with a reference you generated
      'customer_name': 'Njoku Emmanuel',
      'customer_email': 'kalunjoku123@gmail.com',
      'coin': 'BUSD', # BUSD, DAI, USDC or USDT
      'currency': 'USD', # NGN, AED, GBP, EUR
      'amount': 100,
      'accept_partial_payment': True, # By default it's false
   }

   response = await lazerpay.payment.initialize_payment(transaction_payload)
   print(response)
```

**`Confirm Payment`**

This describes to allow you confirm your customers transaction after payment has been made.

```py
  
  async def confirm_tx ():
      transaction_payload = {
        'identifier': '0xa523F92BBF59bB19FCc7020A7e9004A05B697C25', 
      }
      response = await lazerpay.payment.confirm_payment(transaction_payload)
      print(response)
```

## Payment Links

**`Create a payment link`**

This describes to allow you create a Payment link programatically

```py

async def test_create_link():
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

    response = await lazerpay.payment_links.create_payment_link(transaction_payload)
    print(response)   
```

**`Update a payment link`**

This describes disabling or enabling a payment link by updating it

```py
async def update_paymentLink ():
    transaction_payload = {
        "identifier": "pq9pgb",
        "status": "inactive"
    }
    
    response = await lazerpay.payment_links.update_payment_link(transaction_payload)
    print(response)
```

**`Get all payment links`**

This describes to allow you get all Payment links created

```py
async def get_all_paymentlinks():
    response = await lazerpay.payment_links.get_all_paymentlinks()
    print(response)
```

**`Get a single payment link`**

This describes to allow you get a Payment link by it's identifier

```py
async def get_paymentlink ():
    identifier = 'pq9pgb'
    
    response = await lazerpay.payment_links.get_paymentlink(identifier)
    print(response)
```

## Misc

**`Get Accepted Coins`**

This gets the list of accepted cryptocurrencies on Lazerpay

```py
async def get_accepted_coins ():
    response = await lazerpay.misc.test_get_links()
    print(response)
```
