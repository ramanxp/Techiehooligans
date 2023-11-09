from ._anvil_designer import CheckoutTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Checkout(CheckoutTemplate):
  def __init__(self, id_name, back_button_callback, **properties):
    
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.update_form(id_name)
    self.back_button_callback = back_button_callback
    # Any code you write here will run before the form opens.

  def update_form(self, id_name):
    product = anvil.server.call('get_product_details', id_name)
    self.name_label.text = product['Name']
    self.description_label.text = product['Description']
    self.price_label.text = f"₹{product['Price']}"
    self.image_content.source = product['Image']

  def buy_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def back_button_click(self, **event_args):
    self.back_button_callback()
