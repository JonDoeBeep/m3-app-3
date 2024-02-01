from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  num = ""
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
      """This method is called when the button is clicked"""
      self.num = self.num + 1
      self.text_box_1.text = self.num

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
      self.num = self.num + 2
      self.text_box_1.text = self.num
    
  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
      self.num = self.num + 3
      self.text_box_1.text = self.num
    
  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
      self.num = self.num + "*"
      self.text_box_1.text = self.num
    
  




  
    
    
    
