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
    self.name_label.text = name
    self.description_label.text = description
    self.buy.text = button_text
    self.image_content.source = image

  def button_callback()

    # Any code you write here will run before the form opens.

  def cart_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.button_callback()
