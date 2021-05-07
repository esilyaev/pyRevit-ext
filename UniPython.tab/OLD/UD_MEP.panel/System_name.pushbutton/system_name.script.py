# -*- coding: utf-8 -*-
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import *
from Autodesk.Revit.DB.Analysis import *

from Autodesk.Revit.UI import *

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

from Autodesk.Revit.DB import ElementId

from System.Collections.Generic import *


# dic with code from categories


cat = [
  #BuiltInCategory.OST_CableTray,
  #BuiltInCategory.OST_CableTrayFitting,
  #BuiltInCategory.OST_DuctCurves,
  #BuiltInCategory.OST_DuctFitting,
  BuiltInCategory.OST_DuctAccessory,
  BuiltInCategory.OST_DuctTerminal,
  BuiltInCategory.OST_MechanicalEquipment,
  #BuiltInCategory.OST_FlexDuctCurves,
  #BuiltInCategory.OST_DuctInsulations,
  #BuiltInCategory.OST_PipeAccessory,
  BuiltInCategory.OST_PipeCurves,
  #BuiltInCategory.OST_PipeFitting,
  #BuiltInCategory.OST_PipeInsulations,
  #BuiltInCategory.OST_PlumbingFixtures,
  #BuiltInCategory.OST_Sprinklers

]

# check if model not in 0487.61 project

filename = doc.PathName

# if not filename.Contains("0489.61"):
#   TaskDialog.Show("Ошибка!", "Скрипт предназначен только для проекта 0489.61")
#   raise SystemExit

elements = []

for c in cat:
  [elements.append(i) for i in FilteredElementCollector(doc).OfCategory(c).\
    WhereElementIsNotElementType().ToElements()]

t = Transaction(doc, "system name's copying ...")
t.Start()


for el in elements:
  if el.LookupParameter("UD_Имя системы"):
    el.LookupParameter("UD_Имя системы").Set(el.get_Parameter(BuiltInParameter.RBS_SYSTEM_NAME_PARAM).AsString())
  else:
    msg = "Добавьте параметр UD_Имя системы к категории %s" % el.Category.Name
    TaskDialog.Show("Ошибка!", msg)
    raise SystemExit


t.Commit()
  
  





