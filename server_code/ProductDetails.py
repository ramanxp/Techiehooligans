import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


@anvil.server.callable
def get_all_products():
   return app_tables.products.client_readable()


@anvil.server.callable
def get_product_details(product_name):
  return app_tables.products.get(id_name=product_name)
  
   


