from ._anvil_designer import ProductsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ProductItem import ProductItem

class Products(ProductsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.load_products()
    self.content_panel.add_component(ProductItem(name="Name", buttonText="Buy for 100", description="description"))

  def load_products(self):
    products = anvil.server.call('get_product_details').search()
    for product in products:
      print(product['Name'])
    