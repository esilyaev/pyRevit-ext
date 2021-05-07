# -*- coding: utf-8 -*-
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import *
from Autodesk.Revit.DB.Analysis import *

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.UI import UIApplication

hatchs = [i for i in FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_DetailComponents).WhereElementIsNotElementType()]

t = Transaction(doc, 'SCE')
t.Start()
for el in hatchs: 
	el.LookupParameter('UD_ARCH_Площадь').Set(el.get_Parameter(BuiltInParameter.HOST_AREA_COMPUTED).AsDouble())
t.Commit()

