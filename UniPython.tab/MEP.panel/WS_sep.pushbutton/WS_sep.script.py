# -*- coding: utf-8 -*-

__doc__ = """Рассортировать системы по рабочим наборам"""
__author__ = '@unidraft'
__version__ = '0.0.0'
__title__ = "Сортировать по наборам"

from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import *
from Autodesk.Revit.DB.Analysis import *

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.UI import UIApplication


#словарь с ID рабочих наборов
ws_ids = {}

wsList = FilteredWorksetCollector(doc).OfKind(WorksetKind.UserWorkset).ToWorksets()
for ws in wsList:
	if ws.Name.Contains("000_Связанные файлы АР"):
		ws_ids["ar"] = ws.Id.IntegerValue
	if ws.Name.Contains("000_Связанные файлы ИОС"):
		ws_ids["ios"] = ws.Id.IntegerValue
	if ws.Name.Contains("HVAC_100_Отопление"):
		ws_ids["HVAC_100"] = ws.Id.IntegerValue
	if ws.Name.Contains("HVAC_200_Общеобменная вентиляция"):
		ws_ids["HVAC_200"] = ws.Id.IntegerValue
	if ws.Name.Contains("HVAC_300_Теплоснабжение"):
		ws_ids["HVAC_300"] = ws.Id.IntegerValue
	if ws.Name.Contains("HVAC_400_Холодоснабжение"):
		ws_ids["HVAC_400"] = ws.Id.IntegerValue
	if ws.Name.Contains("HVAC_500_Противодымная вентиляция"):
		ws_ids["HVAC_500"] = ws.Id.IntegerValue
	if ws.Name.Contains("HVAC_600_Холодильный центр"):
		ws_ids["HVAC_600"] = ws.Id.IntegerValue
	if ws.Name.Contains("PL_100_Система хоз-питьевого водоснабжения"):
		ws_ids["PL_100"] = ws.Id.IntegerValue
	if ws.Name.Contains("PL_200_Система водоотведения"):
		ws_ids["PL_200"] = ws.Id.IntegerValue
	if ws.Name.Contains("PL_300_Насосная станция водоснабжения"):
		ws_ids["PL_300"] = ws.Id.IntegerValue
	if ws.Name.Contains("PL_400_Система технического водопровода"):
		ws_ids["PL_400"] = ws.Id.IntegerValue

def elementsSeparator(elements, ws_ids = ws_ids):
	for elem in elements:
		# print elem.Id
		if elem.get_Parameter(BuiltInParameter.RBS_DUCT_SYSTEM_TYPE_PARAM):
			system = elem.get_Parameter(BuiltInParameter.RBS_DUCT_SYSTEM_TYPE_PARAM)\
				.AsValueString()
		else:
			system = elem.get_Parameter(BuiltInParameter.RBS_PIPING_SYSTEM_TYPE_PARAM)\
				.AsValueString()
		if system.Contains("Выт") or system.Contains("При") or system.Contains("Выброс"):
			elem.get_Parameter(BuiltInParameter.ELEM_PARTITION_PARAM).Set(ws_ids["HVAC_200"])

		if system.Contains("Дым") or system.Contains("Комп") or system.Contains("Подп"):
			elem.get_Parameter(BuiltInParameter.ELEM_PARTITION_PARAM).Set(ws_ids["HVAC_500"])

		if system.Contains("Т1") or system.Contains("Т2"):
			elem.get_Parameter(BuiltInParameter.ELEM_PARTITION_PARAM).Set(ws_ids["HVAC_100"])

		if system.Contains("К1") or system.Contains("К2"):
			elem.get_Parameter(BuiltInParameter.ELEM_PARTITION_PARAM).Set(ws_ids["PL_200"])
			
		if system.Contains("водоснабжени"):
			elem.get_Parameter(BuiltInParameter.ELEM_PARTITION_PARAM).Set(ws_ids["PL_100"])		

ducts = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_DuctCurves)\
		.WhereElementIsNotElementType()
ductFittings = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_DuctFitting)\
		.WhereElementIsNotElementType()
ductAccessories = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_DuctAccessory)\
		.WhereElementIsNotElementType()
MEPEquipments = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_MechanicalEquipment)\
		.WhereElementIsNotElementType()
pipeFittings = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_PipeFitting)\
		.WhereElementIsNotElementType()
pipes = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_PipeCurves)\
		.WhereElementIsNotElementType()
pipeAccessories = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_PipeAccessory)\
		.WhereElementIsNotElementType()



t = Transaction(doc, 'separation...')
t.Start()
elementsSeparator(ducts)
elementsSeparator(ductFittings)
elementsSeparator(ductAccessories)
elementsSeparator(MEPEquipments)
elementsSeparator(pipeFittings)
elementsSeparator(pipes)
elementsSeparator(pipeAccessories)
t.Commit()  