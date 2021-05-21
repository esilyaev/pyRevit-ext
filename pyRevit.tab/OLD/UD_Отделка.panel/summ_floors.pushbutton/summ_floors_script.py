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

def GetFinishName(elem):
	elemType = elem.GetTypeId()
	type = doc.GetElement(elemType)
	name = type.LookupParameter('UD_ARCH_Пирог').AsString().split('\n')[0]
	name = name.split(' ')
	name.pop(0)
	name = ' '.join(name)
	return name

floors = [i for i in FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Floors).WhereElementIsNotElementType() \
	 if i.Name.Contains("_пол_") and i.LookupParameter("ADSK_Примечание") \
	 and i.LookupParameter("ADSK_Примечание").AsString() != 'Не найдено']

numberRoomsFloors = [i.LookupParameter("ADSK_Примечание").AsString() for i in floors]
nameFloors = [GetFinishName(i) for i in floors]
areaFloors = [float(floor.get_Parameter(BuiltInParameter.HOST_AREA_COMPUTED).AsValueString().Replace(',', '.')) for floor in floors]

finalList = zip(numberRoomsFloors,nameFloors,areaFloors)
dic = {}
for key, group in groupby(finalList, itemgetter(0)):	
	dic[key] = [i for i in finalList if i[0] == key]
finalDic = {}
for keyRoom in dic:
	dicTemp = {}
	finalDic[keyRoom] = dicTemp
	for key, group in groupby(dic[keyRoom], itemgetter(1)):
		finalDic[keyRoom][key] = [i for i in dic[keyRoom] if i[1] == key]

# rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType()
# t = Transaction(doc, 'SCE')
# t.Start()
# for room in rooms:
# 	num = room.get_Parameter(BuiltInParameter.ROOM_NUMBER).AsString()
# 	if	finalList.ContainsKey(num):
# 		item = finalList[num]
# 		#print item[0],item[1]
# 		room.get_Parameter(BuiltInParameter.ROOM_FINISH_FLOOR).Set(item[0])
# 		room.LookupParameter("Площадь отделки пола").Set(item[1])
# t.Commit()

rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType()
t = Transaction(doc, 'SCE')
t.Start()
for room in rooms:
	if room.LookupParameter("UD_ARCH_Автоматический расчет").AsInteger() == 1:
		num = room.get_Parameter(BuiltInParameter.ROOM_NUMBER).AsString()
		if finalDic.ContainsKey(num):
			finishNameAll = ""
			totalArea = []
			for index, groupFloorName in enumerate(finalDic[num]):
				groupFloor = finalDic[num][groupFloorName]
				finishName = groupFloorName
				area = sum([i[2] for i in groupFloor])
				finishNameAll = finishNameAll + str(index+1) + ". " + finishName + " - " + str(area) + " кв. м\n"
				totalArea.append(area)		
			room.get_Parameter(BuiltInParameter.ROOM_FINISH_FLOOR).Set(finishNameAll.Trim())
			room.LookupParameter("Площадь отделки пола").Set(str(sum(totalArea)))
t.Commit()

