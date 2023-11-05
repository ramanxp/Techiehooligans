from ._anvil_designer import BaseTemplate
from anvil import *
import anvil.server
from ..Home import Home


class Base(BaseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.content_panel.add_component(Home())

  def link_1_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(Home())