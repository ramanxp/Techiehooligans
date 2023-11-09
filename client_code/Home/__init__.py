from ._anvil_designer import HomeTemplate
from anvil import *
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
from ..Products import Products


class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def viewProducts_click(self, **event_args):
    self.content_panel.clear()

  def view_products_button_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component((Products()))
    
    
