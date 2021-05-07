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

filename = r'D:\sin_work\pyrevit\MyExtensions.extension\pyRevit.tab\elements.json'

with open(filename) as json_file:
  data = json.load(json_file)
  data = json.loads(data)


# define a transaction variable and describe the transaction
t = Transaction(doc, 'Set Work Code to elements ...')

# start a transaction in the Revit database
t.Start()

# perform some action here...

for el in data:

  Element = doc.GetElement(ElementId(int(el["1"])))
  WorkStr = ""
  if Element.LookupParameter("ИНТ_КодРаботы").AsString() is not None\
     and Element.LookupParameter("ИНТ_КодРаботы").AsString() != "":
    WorkStr += Element.LookupParameter("ИНТ_КодРаботы").AsString() + " "
  WorkStr += el["2"]
  Element.LookupParameter("ИНТ_КодРаботы").Set(WorkStr)


# commit the transaction to the Revit database
t.Commit()

# close the script window
# __window__.Close()
