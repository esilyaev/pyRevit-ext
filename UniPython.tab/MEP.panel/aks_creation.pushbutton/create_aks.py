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

class AksCreator(object):
	"""docstring for AksCreator"""
	def __init__(self, config):
		
		# self.collPipeSystems = FilteredElementCollector(doc).\
		# 	OfCategory(BuiltInCategory.OST_PipingSystem).ToElements()
		self.collDuctSystems = FilteredElementCollector(doc).\
			OfCategory(BuiltInCategory.OST_DuctSystem)\
			.WhereElementIsNotElementType()\
			.ToElements()
		self.DSNameList = []
		if config.systemCommon:
			self.DSNameList += [i.Name for i in self.collDuctSystems\
					if not i.Name.Contains("Д")]
		if config.systemPDV:
			self.DSNameList += [i.Name for i in self.collDuctSystems\
					if i.Name.Contains("Д")]
		if config.FilterByName:
			self.DSNameList = [i for i in self.DSNameList\
					if i.Contains(config.SystemNameFilter)]
		if config.FilterByNameNotContains:
			self.DSNameList = [i for i in self.DSNameList\
					if not i.Contains(config.SystemNameFilterNotContains)]


		self.vfType = [i for i in FilteredElementCollector(doc).\
			OfClass(ViewFamilyType).ToElements()\
			if i.ViewFamily.ToString() == "ThreeDimensional"]
		self.vfType = self.vfType[0].Id

		self.categories = List[ElementId]()
		#Добавление категорий в фильтр вентиляции
		self.categories.Add(ElementId(BuiltInCategory.OST_DuctCurves))
		self.categories.Add(ElementId(BuiltInCategory.OST_DuctFitting))
		self.categories.Add(ElementId(BuiltInCategory.OST_DuctAccessory))
		self.categories.Add(ElementId(BuiltInCategory.OST_DuctTerminal))
		self.categories.Add(ElementId(BuiltInCategory.OST_MechanicalEquipment))
		self.categories.Add(ElementId(BuiltInCategory.OST_FlexDuctCurves))
		self.categories.Add(ElementId(BuiltInCategory.OST_DuctInsulations))
		


	def Run(self):
		#filters and views creation...
		if self.DSNameList == []:
			return "Ни одна система не проходит фильтры"
		try:
			vt200 = [i for i in FilteredElementCollector(doc).\
				OfClass(View).ToElements() if i.IsTemplate and i.Name == "P-A-200"][0].Id
		except Exception as e:
			# TaskDialog.Show("Script error", "В проекте отсутствует шаблон вида P-A-200")
			return "В проекте отсутствует шаблон вида P-A-200"
		try:
			vt500 = [i for i in FilteredElementCollector(doc).\
				OfClass(View).ToElements() if i.IsTemplate and i.Name == "P-A-500"][0].Id
		except Exception as e:
			# TaskDialog.Show("Script error", "В проекте отсутствует шаблон вида P-A-500")
			return "В проекте отсутствует шаблон вида P-A-500"

		systemsCount =0
		for name in self.DSNameList:
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
				vFilter = ParameterFilterElement.Create\
						(doc, name, self.categories, rules).Id
				newView = View3D.CreateIsometric(doc, self.vfType)
				newView.Name = name
				newView.ViewTemplateId = vt
				newView.AddFilter(vFilter)
				newView.SetFilterVisibility(vFilter, False)
				systemsCount +=1
		if int(systemsCount.ToString()[-1]) == 0:
			return "Создано " + systemsCount.ToString() + " видов " \
					+ "и фильтров систем"
		elif int(systemsCount.ToString()[-1]) == 1:
			return "Создан " + systemsCount.ToString() + " вид " \
					+ "и фильтр систем"
		elif int(systemsCount.ToString()[-1]) == 2:
			return "Создано " + systemsCount.ToString() + " вида " \
					+ "и фильтра систем"
		elif int(systemsCount.ToString()[-1]) > 2:
			return "Создано " + systemsCount.ToString() + " видов " \
					+ "и фильтров систем"
		else:
			return "Что-то не так"

