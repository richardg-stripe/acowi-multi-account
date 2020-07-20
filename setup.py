
from dotenv import load_dotenv
import os
import stripe
import time

load_dotenv(dotenv_path='./env.env')

PRIMARY_STRIPE_SECRET_KEY = os.getenv("PRIMARY_STRIPE_SECRET_KEY")
SECONDARY_STRIPE_SECRET_KEY = os.getenv("SECONDARY_STRIPE_SECRET_KEY")

print(PRIMARY_STRIPE_SECRET_KEY)


account = stripe.Account.create(
  type="custom",
  country="GB",
  requested_capabilities=["card_payments", "transfers"],
  tos_acceptance={
    'date': int(time.time()),
    'ip': "1.1.1.1",
    'user_agent': "Chrome"
  },
  business_type="individual",
  business_profile={
    'product_description': "prod desc",
		'mcc': '7623'
  },
  individual={
		'email': 'jane@doe.com',
		'phone': '+447742123123',
    'address': {
      'line1': "address_full_match",
      'city': "London",
      'country': "GB",
      'postal_code': "E14 5AA"
    },
    'dob': {
      'day': 1,
      'month': 1,
      'year': 1901
    },
    'first_name': "Account",
    'last_name': "One"
  },
  external_account = {
    'object': "bank_account",
    'country': "GB",
    'currency': "GBP",
    'account_number': "00012345",
		'routing_number': '108800'
  },
  api_key=PRIMARY_STRIPE_SECRET_KEY,
)

print(account)



account = stripe.Account.create(
  type="custom",
  country="GB",
  requested_capabilities=["card_payments", "transfers"],
  tos_acceptance={
    'date': int(time.time()),
    'ip': "1.1.1.1",
    'user_agent': "Chrome"
  },
  business_type="individual",
  business_profile={
    'product_description': "prod desc",
		'mcc': '7623'
  },
  individual={
		'email': 'jane@doe.com',
		'phone': '+447742123123',
    'address': {
      'line1': "address_full_match",
      'city': "London",
      'country': "GB",
      'postal_code': "E14 5AA"
    },
    'dob': {
      'day': 1,
      'month': 1,
      'year': 1901
    },
    'first_name': "Account",
    'last_name': "One"
  },
  external_account = {
    'object': "bank_account",
    'country': "GB",
    'currency': "GBP",
    'account_number': "00012345",
		'routing_number': '108800'
  },
  api_key=SECONDARY_STRIPE_SECRET_KEY,
)
