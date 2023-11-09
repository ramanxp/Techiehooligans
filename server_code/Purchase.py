import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def charge_user(token, email, product_name):
  stripe_customer = anvil.stripe.new_customer(email, token)
  price = app_tables.products.get(Name=product_name)['Price'] * 100
  result = stripe_customer.charge(amount=price, currency="INR")
  print(result)
