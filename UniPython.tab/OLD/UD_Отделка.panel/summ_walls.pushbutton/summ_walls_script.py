# -*- coding: utf-8 -*-
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


walls = [i for i in FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType() if i.Name.Contains("_Отделка_") and i.LookupParameter("ADSK_Примечание") and i.LookupParameter("ADSK_Примечание").AsString() != "Не найдено"]
numberRoomsWalls = [i.LookupParameter("ADSK_Примечание").AsString() for i in walls]
nameWalls = [GetFinishName(i) for i in walls]
areaWalls = [float(wall.get_Parameter(BuiltInParameter.HOST_AREA_COMPUTED).AsValueString().Replace(',', '.')) for wall in walls]	
finalList = zip(numberRoomsWalls,nameWalls,walls,areaWalls)

dic = {}
for key, group in groupby(finalList, itemgetter(0)):	
	dic[key] = [i for i in finalList if i[0] == key]
finalDic = {}
for keyRoom in dic:
	dicTemp = {}
	finalDic[keyRoom] = dicTemp
	for key, group in groupby(dic[keyRoom], itemgetter(1)):
		finalDic[keyRoom][key] = [i for i in dic[keyRoom] if i[1] == key]


rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType()
t = Transaction(doc, 'SCE')
t.Start()
for room in rooms:
	if room.LookupParameter("UD_ARCH_Автоматический расчет").AsInteger() == 1:
		num = room.get_Parameter(BuiltInParameter.ROOM_NUMBER).AsString()
		if finalDic.ContainsKey(num):
			finishNameAll = ""
			totalArea = []
			for index, groupWallName in enumerate(finalDic[num]):
				groupWall = finalDic[num][groupWallName]
				finishName = groupWallName
				area = sum([i[3] for i in groupWall])
				finishNameAll = finishNameAll + str(index+1) + ". " + finishName + " - " + str(area) + " кв. м\n"
				totalArea.append(area)		
			room.get_Parameter(BuiltInParameter.ROOM_FINISH_WALL).Set(finishNameAll.Trim())
			room.LookupParameter("Площадь отделки стен").Set(str(sum(totalArea)))
t.Commit()		