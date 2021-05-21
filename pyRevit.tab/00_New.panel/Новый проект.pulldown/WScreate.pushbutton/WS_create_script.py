# -*- coding: utf-8 -*-


__doc__ = 'Создание комплекта рабочих набров'
__author__ = '@unidraft'
__version__ = '0.0.0'
__title__ = "Создание РН"


from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import *
from Autodesk.Revit.DB.Analysis import *

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.UI import UIApplication

wsList = [
"000_Связанные файлы АР",
"000_Связанные файлы КР",
"000_Связанные файлы ИОС",
"000_Строительное задание",
"HVAC_100_Отопление",
"HVAC_200_Общеобменная вентиляция",
"HVAC_300_Теплоснабжение",
"HVAC_400_Холодоснабжение",
"HVAC_500_Противодымная вентиляция",
"HVAC_600_Холодильный центр",
"TMS_100_Тепломеханические решения",
"PL_100_Система хоз-питьевого водоснабжения",
"PL_200_Система водоотведения",
"PL_300_Насосная станция водоснабжения",
"PL_400_Система технического водопровода",
"FF_100_Автоматическая установка пожаротушения",
"FF_200_Внутренний противопожарный водопровод",
"FF_300_Насосная станция",
"EL_400_Кабеленесущие системы, кабельные трассы",
"LC_600_Кабеленесущие системы, кабельные трассы",
"BMS_400_Кабеленесущие системы, кабельные трассы",
]

t = Transaction(doc, 'SCE')
t.Start()
if doc.IsWorkshared:
	for name in wsList:
		if WorksetTable.IsWorksetNameUnique(doc, name):
			Workset.Create(doc, name)
t.Commit()

