# -*- coding: utf-8 -*-
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import *
from Autodesk.Revit.DB.Analysis import *

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.UI import TaskDialogCommonButtons
from Autodesk.Revit.UI import TaskDialogResult
from Autodesk.Revit.UI import UIApplication

from System.Collections.Generic import *

collPipeSystems = FilteredElementCollector(doc).\
	OfCategory(BuiltInCategory.OST_PipingSystem).ToElements()

# DS now and late = Duct System
collDuctSystems = FilteredElementCollector(doc).\
	OfCategory(BuiltInCategory.OST_DuctSystem).WhereElementIsNotElementType().ToElements()
DSNameList = [i.Name for i in collDuctSystems]

newDialog = TaskDialog("Warning!")
newDialog.MainContent = "Найдено " + DSNameList.Count.ToString() + " систем воздуховодов.\
						\nПродолжить?"
buttons = TaskDialogCommonButtons.Yes | TaskDialogCommonButtons.No
newDialog.CommonButtons = buttons
result = newDialog.Show()
if result == TaskDialogResult.No:
	TaskDialog.Show("Warning!", "Отменено")
	raise SystemExit


vfType = [i for i in FilteredElementCollector(doc).\
	OfClass(ViewFamilyType).ToElements() if i.ViewFamily.ToString() == "ThreeDimensional"]
vfType = vfType[0].Id



#view template ID for 200

try:
	vt200 = [i for i in FilteredElementCollector(doc).\
		OfClass(View).ToElements() if i.IsTemplate and i.Name == "P-A-200"][0].Id
except Exception as e:
	TaskDialog.Show("Script error", "В проекте отсутствует шаблон вида P-A-200")
	raise SystemExit

#view template ID for 500

try:
	vt500 = [i for i in FilteredElementCollector(doc).\
		OfClass(View).ToElements() if i.IsTemplate and i.Name == "P-A-500"][0].Id
except Exception as e:
	TaskDialog.Show("Script error", "В проекте отсутствует шаблон вида P-A-500")
	raise SystemExit



categories = List[ElementId]()
#Добавление категорий в фильтр вентиляции
categories.Add(ElementId(BuiltInCategory.OST_DuctCurves))
categories.Add(ElementId(BuiltInCategory.OST_DuctFitting))
categories.Add(ElementId(BuiltInCategory.OST_DuctAccessory))
categories.Add(ElementId(BuiltInCategory.OST_DuctTerminal))
categories.Add(ElementId(BuiltInCategory.OST_MechanicalEquipment))
categories.Add(ElementId(BuiltInCategory.OST_FlexDuctCurves))
categories.Add(ElementId(BuiltInCategory.OST_DuctInsulations))

t = Transaction(doc, 'filters and views creation...')
t.Start()

#filters and views creation...
systemsCount =0
for name in DSNameList:
	rules = []
	rules.Add(ParameterFilterRuleFactory.CreateNotEqualsRule\
			(ElementId(BuiltInParameter.RBS_SYSTEM_NAME_PARAM), name,False))
	#print "Правило создано"
	if name.Contains("Д"):
		name = "P-A-500(" + name + ")"
		vt = vt500
	else:
		name = "P-A-200(" + name + ")"
		vt = vt200
	if ParameterFilterElement.IsNameUnique(doc, name):
		#print "Добавляем фильтр" если он уникальный
		vFilter = ParameterFilterElement.Create(doc, name, categories, rules).Id
		newView = View3D.CreateIsometric(doc, vfType)
		newView.Name = name
		newView.ViewTemplateId = vt
		newView.AddFilter(vFilter)
		newView.SetFilterVisibility(vFilter, False)
		systemsCount +=1
t.Commit()
TaskDialog.Show("Result","Создано "+systemsCount.ToString()+" 3D видов систем")
