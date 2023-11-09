from ._anvil_designer import ProductItemTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ProductItem(ProductItemTemplate):
  def __init__(self, name, description, button_text, image, button_callback, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.name_label.content = name
    self.description_label.text = description
    self.cart.text = button_text
    self.image_content.source = image
    self.button_callback = button_callback

  def cart_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.button_callback(self.name_label.content)
