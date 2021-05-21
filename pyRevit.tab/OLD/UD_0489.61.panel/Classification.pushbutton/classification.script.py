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
dic = {
  ElementId(BuiltInCategory.OST_CableTray) : "ИС.ЭС.1.1",
  ElementId(BuiltInCategory.OST_CableTrayFitting) : "ИС.ЭС.1.1",
  ElementId(BuiltInCategory.OST_DuctCurves) : "ИС.ВС.1",
  ElementId(BuiltInCategory.OST_DuctFitting) : "ИС.ВС.2",
  ElementId(BuiltInCategory.OST_DuctAccessory) : "ИС.ВС.3",
  ElementId(BuiltInCategory.OST_DuctTerminal) : "ИС.ВС.4",
  ElementId(BuiltInCategory.OST_MechanicalEquipment) : "ИС.ПО.1",
  ElementId(BuiltInCategory.OST_FlexDuctCurves) : "ИС.ВС.1",
  ElementId(BuiltInCategory.OST_DuctInsulations) : "ИС.ВС.5",
  ElementId(BuiltInCategory.OST_PipeAccessory) : "ИС.ТС.3",
  ElementId(BuiltInCategory.OST_PipeCurves) : "ИС.ТС.1",
  ElementId(BuiltInCategory.OST_PipeFitting) : "ИС.ТС.2",
  ElementId(BuiltInCategory.OST_PipeInsulations) : "ИС.ТС.4",
  ElementId(BuiltInCategory.OST_PlumbingFixtures) : "ИС.ПО.1",
  ElementId(BuiltInCategory.OST_Sprinklers) : "ИС.ПО.3.3"
}

cat = [
  BuiltInCategory.OST_CableTray,
  BuiltInCategory.OST_CableTrayFitting,
  BuiltInCategory.OST_DuctCurves,
  BuiltInCategory.OST_DuctFitting,
  BuiltInCategory.OST_DuctAccessory,
  BuiltInCategory.OST_DuctTerminal,
  BuiltInCategory.OST_MechanicalEquipment,
  BuiltInCategory.OST_FlexDuctCurves,
  BuiltInCategory.OST_DuctInsulations,
  BuiltInCategory.OST_PipeAccessory,
  BuiltInCategory.OST_PipeCurves,
  BuiltInCategory.OST_PipeFitting,
  BuiltInCategory.OST_PipeInsulations,
  BuiltInCategory.OST_PlumbingFixtures,
  BuiltInCategory.OST_Sprinklers

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

t = Transaction(doc, "classification ...")
t.Start()


for el in elements:
  if el.LookupParameter("UD_Классификатор"):
    el.LookupParameter("UD_Классификатор").Set(dic[el.Category.Id])
  else:
    msg = "Добавьте параметр UD_Классификатор к категории %s" % el.Category.Name
    TaskDialog.Show("Ошибка!", msg)
    raise SystemExit


t.Commit()
  
  





