# -*- coding: utf-8 -*-

import os
import sys
from System.Collections.Generic import *
from Autodesk.Revit.DB import ElementId
__doc__ = 'Заполнение параметра MR_Код по классификатору'
__author__ = '@unidraft'
__version__ = '0.0.0'
__title__ = "MR_Код"

from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import *
from Autodesk.Revit.DB.Analysis import *

from Autodesk.Revit.UI import *

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document


lib_path = os.path.join('\\\\fs-uni\BIM\Support\Revit\pyRevit')
sys.path.append(lib_path)
# import utility.sharedfileutil as SFU


def ParameterAdd(name, group):
    # TaskDialog.Show("Ошибка!", "func start!")
    file = doc.Application.OpenSharedParameterFile()
    param = file.Groups[group].Definitions[name]
    # _category = Category.GetCategory(doc, category)
    # _cats = doc.Application.Create.NewCategorySet()
    # _cats.Insert(_category)
    instanceBinding = doc.Application.Create.NewInstanceBinding(cats)
    bindingMap = doc.ParameterBindings
    instanceBindOK = bindingMap.Insert(
        param, instanceBinding, BuiltInParameterGroup.PG_TEXT)
    if not instanceBindOK:
        instanceBindOK = bindingMap.ReInsert(
            param, instanceBinding, BuiltInParameterGroup.PG_TEXT)
    # TaskDialog.Show("Ошибка!", str(instanceBindOK))
    return instanceBindOK


# dic with code from categories
dic = {
    ElementId(BuiltInCategory.OST_CableTray): "ИС.ЭС.1.1",
    ElementId(BuiltInCategory.OST_CableTrayFitting): "ИС.ЭС.1.1",
    ElementId(BuiltInCategory.OST_DuctCurves): "ИС.ВС.1",
    ElementId(BuiltInCategory.OST_DuctFitting): "ИС.ВС.2",
    ElementId(BuiltInCategory.OST_DuctAccessory): "ИС.ВС.3",
    ElementId(BuiltInCategory.OST_DuctTerminal): "ИС.ВС.4",
    ElementId(BuiltInCategory.OST_MechanicalEquipment): "ИС.ПО.1",
    ElementId(BuiltInCategory.OST_FlexDuctCurves): "ИС.ВС.1",
    ElementId(BuiltInCategory.OST_DuctInsulations): "ИС.ВС.5",
    ElementId(BuiltInCategory.OST_PipeAccessory): "ИС.ТС.3",
    ElementId(BuiltInCategory.OST_PipeCurves): "ИС.ТС.1",
    ElementId(BuiltInCategory.OST_PipeFitting): "ИС.ТС.2",
    ElementId(BuiltInCategory.OST_PipeInsulations): "ИС.ТС.4",
    ElementId(BuiltInCategory.OST_PlumbingFixtures): "ИС.ПО.1",
    ElementId(BuiltInCategory.OST_Sprinklers): "ИС.ПО.3.3",
    ElementId(BuiltInCategory.OST_LightingFixtures): "ИС.ЭС.4",
    ElementId(BuiltInCategory.OST_ElectricalFixtures): "ИС.ЭС.4",
    ElementId(BuiltInCategory.OST_Lights): "ИС.ЭС.4",
    ElementId(BuiltInCategory.OST_LightingDevices): "ИС.ЭС.4",
    ElementId(BuiltInCategory.OST_ElectricalEquipment): "ИС.ЭС.3",
    ElementId(BuiltInCategory.OST_Fixtures): "ИС.ЭС.4",
    ElementId(BuiltInCategory.OST_Conduit): "ИС.ЭС.1.2",
    ElementId(BuiltInCategory.OST_ConduitRun): "ИС.ЭС.1.2",
    ElementId(BuiltInCategory.OST_ConduitFitting): "ИС.ЭС.1.2",
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
    BuiltInCategory.OST_Sprinklers,
    BuiltInCategory.OST_LightingFixtures,
    BuiltInCategory.OST_ElectricalFixtures,
    BuiltInCategory.OST_ElectricalEquipment,
    BuiltInCategory.OST_Lights,
    BuiltInCategory.OST_LightingDevices,
    BuiltInCategory.OST_Fixtures,
    BuiltInCategory.OST_Conduit,
    BuiltInCategory.OST_ConduitRun,
    BuiltInCategory.OST_ConduitFitting,
]

cats = doc.Application.Create.NewCategorySet()

for c in cat:
    _category = Category.GetCategory(doc, c)
    if _category:
        cats.Insert(_category)


filename = doc.PathName

# if not filename.Contains("0489.61"):
#   TaskDialog.Show("Ошибка!", "Скрипт предназначен только для проекта 0489.61")
#   raise SystemExit

parName = "MR_Код по классификатору"
parGroup = "MR"


t = Transaction(doc, "classification ...")
t.Start()

# Insert param

# ParameterAdd(parName, parGroup)


# Classofication


for c in cat:
    elements = []

    [elements.append(i) for i in FilteredElementCollector(doc).OfCategory(c).
     WhereElementIsNotElementType().ToElements()]
    # TaskDialog.Show("Ошибка!", "elements added")

    if len(elements) < 1:
        # TaskDialog.Show("Ошибка!", "no elements in c")
        continue

    # TaskDialog.Show("Ошибка!", "starting classification")
    for el in elements:
        if el.LookupParameter("MR_Код по классификатору").AsString() == '' \
                or el.LookupParameter("MR_Код по классификатору").AsString() is None:
            el.LookupParameter("MR_Код по классификатору").Set(
                dic[el.Category.Id])

t.Commit()
