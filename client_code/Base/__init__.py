from ._anvil_designer import BaseTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
from ..Home import Home
from ..MyProducts import MyProducts


class Base(BaseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.content_panel.add_component(Home())
  def change_sign_in_text(self):
    user = anvil.users.get_user()
    if user:
      email = user["email"]
      self.sign_in.text = email
    else:
      self.sign_in.text = "Sign In"
    self.toggle_my_cart_link()
    
  def title_click(self, **event_args):
    self.go_to_home()

  def go_to_home(self):
    self.content_panel.clear()
    self.content_panel.add_component(Home())

  def sign_in_click(self, **event_args):
    user = anvil.users.get_user()
    if user:
      logout = confirm("Would you like to logout ?")
      if logout:
        anvil.users.logout()
        self.go_to_home()
    else:
      anvil.users.login_with_form()
    self.change_sign_in_text()

  def toggle_my_cart_link(self):
    self.my_cart.visible = anvil.users.get_user() != None

  def my_cart_click(self, **event_args):
    self.init_components(**properties)
    self.content_panel.add_component(MyProducts())
    
      

    
