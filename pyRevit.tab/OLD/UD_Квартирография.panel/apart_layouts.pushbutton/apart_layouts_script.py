# -*- coding: utf-8 -*-
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import *
from Autodesk.Revit.DB.Analysis import *

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.UI import UIApplication



rooms = [i for i in FilteredElementCollector(doc).\
	OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType()]

t = Transaction(doc, 'SCE')
t.Start()

finalList = {}
for room in rooms:
	num = room.LookupParameter("ADSK_Номер квартиры").AsString()
	numR = room.get_Parameter(BuiltInParameter.ROOM_NUMBER).AsString()
	if not finalList.ContainsKey(num):
		finalList.Add(num, [0.0, 0.0, 0.0])
		# 0 - ADSK_Площадь квартиры жилая
		# 1 - ADSK_Площадь квартиры
		# 2 - ADSK_Площадь квартиры общая
	parAptTip = room.LookupParameter("ADSK_Тип помещения").AsInteger()
	coeff = room.LookupParameter("ADSK_Коэффициент площади").AsDouble()

	area = float(room.get_Parameter(BuiltInParameter.ROOM_AREA)\
		.AsValueString().Replace(',', '.').split(' ')[0]) * coeff
	area = round(area * 100)/100
	room.LookupParameter("ADSK_Площадь с коэффициентом").Set(area / 0.09290304)

	if parAptTip == 1:
		finalList[num][0] = finalList[num][0] + area
		finalList[num][1] = finalList[num][1] + area
		finalList[num][2] = finalList[num][2] + area
	elif parAptTip == 3 or parAptTip == 4:
		finalList[num][2] = finalList[num][2] + area
	else:
		finalList[num][1] = finalList[num][1] + area
		finalList[num][2] = finalList[num][2] + area
#	if num == "2-3-1":
#		print numR, coeff, area, finalList[num] 



for room in rooms:
	num = room.LookupParameter("ADSK_Номер квартиры").AsString()
	numR = room.get_Parameter(BuiltInParameter.ROOM_NUMBER).AsString()
	if not finalList.ContainsKey(num):
		pass
#	if num == "2-3-1":
#		print numR, finalList[num]
	room.LookupParameter("ADSK_Площадь квартиры жилая").Set(finalList[num][0] / 0.09290304)
	room.LookupParameter("ADSK_Площадь квартиры").Set(finalList[num][1] / 0.09290304)
	room.LookupParameter("ADSK_Площадь квартиры общая").Set(finalList[num][2] / 0.09290304)

t.Commit()



