# -*- coding: utf-8 -*-
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import *
from Autodesk.Revit.DB.Analysis import *

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.UI import UIApplication

doors = [i for i in FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Doors)\
	.WhereElementIsNotElementType()\
	 if i.get_Parameter(BuiltInParameter.ELEM_FAMILY_PARAM).AsValueString() == "GKS_Дверь_Проектируемая"]

t = Transaction(doc, 'SCE')
t.Start()

for door in doors:
	#print door.Id
	if not doc.GetElement(door.GetTypeId()).LookupParameter('GKS_DR_ГОСТ'):
		continue
	phrase = []
	phrase.append("Дверь")

	# ГОСТ
	GOST = doc.GetElement(door.GetTypeId()).LookupParameter('GKS_DR_ГОСТ').AsString()
	if GOST == "ГОСТ 475-2016":
		phrase.append(" деревянная")
	elif GOST == "ГОСТ 23747-2015":
		phrase.append(" алюминиевая")
	elif GOST == "ГОСТ 57327-2016":
		phrase.append(" стальная противопожарная")
	elif GOST == "ГОСТ Р 53780-2010":
		phrase.append(" стальная аварийная лифтовой шахты")
	elif GOST == "Серия 5.904-4":
		phrase.append(" стальная")
	elif GOST == "ГОСТ 30970-2014":
		phrase.append(" влагостойкая поливинилхлоридная")
	elif GOST == "Индивидуальное изготовление":
		if mats[i]:
			phrase.append(" материал полотна %s" % mats[i])
	else:
		phrase.append(" !!!ПРОВЕРЬ ГОСТ!!! ")

	# Внутренняя или наружная
	if door.LookupParameter('GKS_DR_Внутренняя').AsInteger() == 1:
		phrase.append(", внутренняя")
	else:
		phrase.append(", наружная")
	# Класс
	if door.LookupParameter('GKS_DR_Класс').AsString():
		phrase.append(", %s" % door.LookupParameter('GKS_DR_Класс').AsString())
	# Глухая
	if door.LookupParameter('Глухая').AsInteger() == 1:
		phrase.append(", глухая")
	# Утепленная
	if door.LookupParameter('GKS_DR_Утепление').AsInteger() == 1:
		phrase.append(", утепленная")

	# цвет RAL
	if door.LookupParameter('GKS_DR_RAL').AsString():
		phrase.append(", цвет RAL %s" % door.LookupParameter('GKS_DR_RAL').AsString())
	#phrase.append(", в комплекте: ")
	# Доводчик
	if door.LookupParameter('GKS_DR_Доводчик').AsInteger() == 1:
		phrase.append(", с доводчиком")
	# с уплотнением в притворах
	if door.LookupParameter('GKS_DR_Уплотнение в притворах').AsInteger() == 1:
		phrase.append(", с уплотнением в притворах")
	# # огнестойкая
	# if door.LookupParameter('GKS_DR_Огнестойкость').AsString():
	# 	phrase.append(", огнестойкая")
	# порог
	if door.LookupParameter('GKS_DR_Порог').AsString():
		phrase.append(", порог %s" % door.LookupParameter('GKS_DR_Порог').AsString())
	# усиление
	if door.LookupParameter('GKS_DR_Усиление').AsString():
		phrase.append(", усиление %s" % door.LookupParameter('GKS_DR_Усиление').AsString())
	# СКУД
	if door.LookupParameter('GKS_DR_СКУД').AsInteger() == 1:
		phrase.append(", СКУД")
	# гермодверь
	if door.LookupParameter('GKS_DR_Гермодверь').AsInteger() == 1:
		phrase.append(", гермодверь")
	# вентиляционная решетка
	if door.LookupParameter('Решетка').AsInteger() == 1:
		phrase.append(", предусмотреть вентиляционную решетку в нижней части двери")
	# наличники
	if door.LookupParameter('GKS_DR_Наличники').AsString():
		phrase.append(", наличники %s" % door.LookupParameter('GKS_DR_Наличники').AsString())
	# ручка
	if door.LookupParameter('GKS_DR_Ручка').AsString():
		phrase.append(", ручка %s" % door.LookupParameter('GKS_DR_Ручка').AsString())
	# замок
	if door.LookupParameter('GKS_DR_Замок').AsString():
		phrase.append(", замок %s" % door.LookupParameter('GKS_DR_Замок').AsString())
	# цилиндр
	if door.LookupParameter('GKS_DR_Цилиндр').AsString():
		phrase.append(", цилиндр %s" % door.LookupParameter('GKS_DR_Цилиндр').AsString())
	# завертка
	if door.LookupParameter('GKS_DR_Завертка').AsString():
		phrase.append(", завертка %s" % door.LookupParameter('GKS_DR_Завертка').AsString())
	# накладка на цилиндр
	if door.LookupParameter('GKS_DR_Накладка на цилиндр').AsString():
		phrase.append(", накладка на цилиндр %s"\
		 % door.LookupParameter('GKS_DR_Накладка на цилиндр').AsString())
	# дверной упор
	if door.LookupParameter('GKS_DR_Дверной упор').AsString():
		phrase.append(", %s" % door.LookupParameter('GKS_DR_Дверной упор').AsString())
	# петли
	if door.LookupParameter('GKS_DR_Петли').AsString():
		phrase.append(", петли %s" % door.LookupParameter('GKS_DR_Петли').AsString())
	# отделка
	if door.LookupParameter('GKS_DR_Отделка').AsString():
		phrase.append(", %s" % door.LookupParameter('GKS_DR_Отделка').AsString())

	# Габариты
	UD_DR_gabarits = []
	width = int(door.LookupParameter('GKS_DR_Ширина').AsValueString())
	height = int(door.LookupParameter('GKS_DR_Высота').AsValueString())
	kr_up_width = int(doc.GetElement(door.GetTypeId()).LookupParameter('Ширина коробки сверху')\
		.AsValueString())
	kr_width = int(doc.GetElement(door.GetTypeId()).LookupParameter('Ширина коробки')\
		.AsValueString())
	pr_width = int(doc.GetElement(door.GetTypeId()).LookupParameter('GKS_DR_Заужение проема')\
		.AsValueString())
	pr_derpth = int(doc.GetElement(door.GetTypeId()).LookupParameter('GKS_DR_Заглубление полотна')\
		.AsValueString())
	# kr_down_width = int(doc.GetElement(door.GetTypeId()).LookupParameter('Зазор полотна снизу')\
	# 	.AsValueString())
	rigth_side = int(door.LookupParameter('Ширина правой створки').AsValueString())
	left_side = int(door.LookupParameter('Ширина левой створки').AsValueString())
	two_side = doc.GetElement(door.GetTypeId()).LookupParameter('GKS_DR_Двустворчатая').AsInteger()

	if (height and width  and kr_width and kr_up_width and pr_width and pr_derpth):
		if two_side != 1:
			h = height
			w = width
			h1 = h - kr_width
			h2 = h - kr_up_width - pr_derpth
			w1 = width - (kr_width * 2)
			w2 = w1 - pr_width
			UD_DR_gabarits.append("h = %s\nw= %s\nh1 = %s\nh'= %s\nw1 = %s\nw'= %s"\
			 % (int(h), int(w), int(h1), int(h2), int(w1), int(w2)))
			
		else:
			h = height
			w = width
			h1 = h - kr_width
			h2 = h - kr_up_width - pr_derpth
			if left_side > rigth_side:
				w1 = left_side
				w3 = rigth_side
			else:
				w3 = left_side
				w1 = rigth_side
			
			w2 = w1 - pr_width
			UD_DR_gabarits.append("h = %s\nw= %s\nh1 = %s\nh' = %s\nw1= %s\nw2 = %s\nw'= %s"\
			 % (int(h), int(w), int(h1), int(h2), int(w1), int(w2), int(w3)))
			
	else:
		UD_DR_gabarits.append("Заполни габариты")
	
	door.LookupParameter('UD_ARCH_DR_Описание').Set(''.join(phrase))
	door.LookupParameter('UD_ARCH_DR_Габариты').Set(''.join(UD_DR_gabarits))


t.Commit()	


