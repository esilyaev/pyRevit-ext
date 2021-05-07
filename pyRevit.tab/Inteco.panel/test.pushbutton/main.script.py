# -*- coding: utf-8 -*-

# import libraries and reference the RevitAPI and RevitAPIU
import json
import clr
import math
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *

# set the active Revit application and document
app = __revit__.Application
doc = __revit__.ActiveUIDocument.Document

filename = r'U:\__tmp\source\pyRevit-work\pyRevit.extension\pyRevit.tab\elements.json'

with open(filename) as json_file:
  data = json.load(json_file)
  data = json.loads(data)

for el in data:
  print(el['1'])


# # define a transaction variable and describe the transaction
# t = Transaction(doc, 'This is my new transaction')

# # start a transaction in the Revit database
# t.Start()

# # perform some action here...

# # commit the transaction to the Revit database
# t.Commit()

# # close the script window
# __window__.Close()
