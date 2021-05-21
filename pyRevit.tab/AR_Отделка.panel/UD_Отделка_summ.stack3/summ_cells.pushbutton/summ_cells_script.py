# -*- coding: utf-8 -*-

__doc__ = """Суммировать все потолки и записать их в помещения"""
__author__ = '@unidraft'
__version__ = '0.0.0'
__title__ = "Суммировать потолки"

from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import *
from Autodesk.Revit.DB.Analysis import *

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.UI import UIApplication

import sys
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)
from itertools import groupby
from operator import itemgetter

def GetFinishCeilingName(elem):
	name = elem.LookupParameter('UD_ARCH_ОТ_Наименование').AsString()
	return name
	
def GetFinishName(wall):
	name = " "
	name1 = wall.LookupParameter("UD_ARCH_ОТ_Наименование").AsString()
	name2 = wall.LookupParameter("UD_ARCH_ОТ_Завод-изготовитель").AsString()
	name3 = wall.LookupParameter("UD_ARCH_ОТ_Цвет").AsString()
	if name1 :
		name = name1
	if name2:
		name = name + " " + name2
	if name3:
		name = name + " " + name3
	return name	
ceilings = [i for i in FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Ceilings).WhereElementIsNotElementType()\
if i.LookupParameter("ADSK_Примечание") and i.LookupParameter("ADSK_Примечание").AsString() != 'Не найдено']

wallsFinish = [i for i in FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType() \
if i.Name.Contains("_потолок_") and i.LookupParameter("ADSK_Примечание")\
and i.LookupParameter("ADSK_Примечание").AsString() != 'Не найдено']

interimList = [[i.LookupParameter("ADSK_Примечание").AsString(),float(i.get_Parameter(BuiltInParameter.HOST_AREA_COMPUTED).AsDouble()* 0.09290304),GetFinishCeilingName(i),i] for i in ceilings]
[interimList.append([i.LookupParameter("ADSK_Примечание").AsString(),float(i.get_Parameter(BuiltInParameter.HOST_AREA_COMPUTED).AsDouble()* 0.09290304),GetFinishName(i),i]) for i in wallsFinish]

rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType()
dictGroup = {}
for room in rooms:
	num = room.get_Parameter(BuiltInParameter.ROOM_NUMBER).AsString()	
	list1 = [i for i in interimList if num == i[0]]
	if list1 != []:
		dictGroup[num] = list1
dictFinal = {}
for keyRoom in dictGroup:
	dict = {}
	for key, group in groupby(dictGroup[keyRoom], itemgetter(2)):		
		dict[key] = [i for i in dictGroup[keyRoom] if i[2] == key]
	dictFinal[keyRoom] = dict
t = Transaction(doc, 'SCE')
t.Start()
	
for room in rooms:
	if room.LookupParameter("UD_ARCH_Автоматический расчет").AsInteger() == 1:
		num = room.get_Parameter(BuiltInParameter.ROOM_NUMBER).AsString()
		if dictFinal.ContainsKey(num):		
			finalArea = 0.0
			finishName = ""
			for index,item in enumerate(dictFinal[num], 1):
				finish = item
				if item == None:
					finish = "None"
				if dictFinal[num].Count > 1:			
					sumArea = sum([i[1] for i in dictFinal[num][item]])				
					finalArea = finalArea + sumArea
					finishName = finishName + str(index) + ". " + finish + " - " + str(round(sumArea,2)).replace('.', ',') + " кв. м\n"
					
				else:
					sumArea = sum([i[1] for i in dictFinal[num][item]])
					finalArea = sumArea
					finishName = finish 
	#		print finishName
			room.LookupParameter("Отделка потолка").Set(finishName)		
			#room.LookupParameter("Площадь отделки потолка").Set(str(finalArea))
			room.LookupParameter("Площадь отделки потолка текстовый").Set(str(round(finalArea,2)).replace('.', ','))
t.Commit()