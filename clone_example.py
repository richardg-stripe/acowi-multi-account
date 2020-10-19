from dotenv import load_dotenv
import os
import stripe

load_dotenv(dotenv_path='./env.env')

PRIMARY_STRIPE_SECRET_KEY = os.getenv("PRIMARY_STRIPE_SECRET_KEY")
SECONDARY_STRIPE_SECRET_KEY = os.getenv("SECONDARY_STRIPE_SECRET_KEY")
SECONDARY_STRIPE_ACCOUNT_ID = os.getenv("SECONDARY_STRIPE_ACCOUNT_ID")

print(PRIMARY_STRIPE_SECRET_KEY)

payment_method = stripe.PaymentMethod.create(
  type="card",
  billing_details = {
    "address": {
      "postal_code": "E14 5AA"
    }
  },
  card = {
    "number": "4242424242424242",
    "cvc": "123",
    "exp_month": "08",
    "exp_year": "23"
  },
  api_key=PRIMARY_STRIPE_SECRET_KEY,
)

print('payment_method: ', payment_method)
input("Press Enter to continue...")

customer = stripe.Customer.create(
  description="Customer 1",
  metadata={'name': 'customer 1'},
  payment_method=payment_method.id,
  api_key=PRIMARY_STRIPE_SECRET_KEY,
)

customer = stripe.Customer.retrieve(customer.id, api_key=PRIMARY_STRIPE_SECRET_KEY)

print('primary customer: ', customer)
input("Press Enter to continue...")

payment_methods = stripe.PaymentMethod.list(
  customer=customer.id,
  type="card",
  api_key=PRIMARY_STRIPE_SECRET_KEY,
)

print('primary payment_method: ', payment_methods.data[0])
input("Press Enter to continue...")

customer_payment_method = payment_methods.data[0]
payment_intent = stripe.PaymentIntent.create(
  return_url= "https://something.com",
  payment_method=customer_payment_method.id,
  customer=customer.id,
  amount=1000,
  currency="GBP",
  confirm=True,
  transfer_data={
    'destination': 'acct_1H5vOFEnc0lv44J2'
  },
  api_key=PRIMARY_STRIPE_SECRET_KEY,
)


print('primary payment_intent: ', payment_intent)
input("Press Enter to continue...")


cloned_payment_method = stripe.PaymentMethod.create(
  customer=customer.id,
  payment_method=customer_payment_method.id,
  stripe_account=SECONDARY_STRIPE_ACCOUNT_ID,
  api_key=PRIMARY_STRIPE_SECRET_KEY,
)

print('Cloned payment method!: ', cloned_payment_method)
input("Press Enter to continue...")

print(cloned_payment_method)

payment_intent = stripe.PaymentIntent.create(
  return_url= "https://something.com",
  payment_method=cloned_payment_method.id,
  amount=1000,
  currency="GBP",
  confirm=True,
  transfer_data={
    'destination': 'acct_1H5voeLz0gGpGd9R'
  },
  api_key=SECONDARY_STRIPE_SECRET_KEY,
)

