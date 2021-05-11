# -*- coding: utf-8 -*-

# import libraries and reference the RevitAPI and RevitAPIUI
import clr
import math

clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *

# set the active Revit application and document
app = __revit__.Application
doc = __revit__.ActiveUIDocument.Document


class Cheker:
  @staticmethod
  def checkRule(rule):
    """Cheking all elements in doc based on Rule
    and print msg

    Args:
        rule (Rule): Instance of Rule class from ImportFromExcel
    """
    cat = [i for i in doc.Settings.Categories if i.Name == rule.Category][0]
    col = FilteredElementCollector(doc)\
        .OfCategoryId(cat.Id)\
        .WhereElementIsNotElementType()\
        .ToElements()

    for p in rule.parList:
      print(p)

    for el in col:
      msg = "Element id: " + str(el.Id) + " "
      for p in rule.parList:
        if Cheker.checkParameter(el, p):
          msg += " +"
        else:
          msg += " -"

      print(msg)

  @staticmethod
  def checkParameter(el, p):
    if el.LookupParameter(p) is not None:
      if el.LookupParameter(p).AsString() != "" or el.LookupParameter(p).AsValueString() != "":
        return True
    else:
      type = doc.GetElement(el.GetTypeId())
      if type.LookupParameter(p) is not None:
        if type.LookupParameter(p).AsString() != "" or type.LookupParameter(p).AsValueString() != "":
          return True

    return False
