from ._anvil_designer import Form1Template
from anvil import *
import numpy as np

class Form1(Form1Template):
  num = ''
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  