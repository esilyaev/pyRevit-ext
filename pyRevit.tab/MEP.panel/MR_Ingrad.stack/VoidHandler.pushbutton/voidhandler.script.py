# -*- coding: utf-8 -*-

__doc__ = """Обработка задания на отверстия для Ingrad"""
__author__ = '@unidraft'
__version__ = '0.0.0'
__title__ = "Обработка заданий"


from datetime import date
from System.Collections.Generic import *
from Autodesk.Revit.UI import UIApplication
from Autodesk.Revit.UI import TaskDialogResult
from Autodesk.Revit.UI import TaskDialogCommonButtons
from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import *
from Autodesk.Revit.DB.Analysis import *

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document


today = date.today()

OwnerDict = {
		"BMS": "АК",
		"PL": "ВК",
		# "" : "ДУ",
		"HVAC": "ОВ",
		# "EL" : "ПД",
		"FF": "ВК",
		"LC": "СС",
		"TMS": "ТМ",
		"EL": "ЭМ",
		"VK": "ВК",
		"DU": "ДУ",
		"PD": "ПД",
		"PT": "ПТ",
		"OT": "ОТ",
		"KV": "КВ",
		"LC": "СС",
		"HVAC+VK": "ОВ, ВК",
		"HVAC+DU": "ОВ, ДУ",
		"HVAC+PD": "ОВ, ПД",
		"PD+HVAC": "ПД, ОВ", 
		"DU+HVAC": "ДУ, ОВ",
		"PD+OT": "ПД, ОТ",
		"DU+OT": "ДУ, ОТ", 
		"PD+VK": "ПД, ВК",
		"DU+VK": "ДУ, ВК",
		"VK+HVAC": "ВК, ОВ",
		"HVAC+OT": "ОВ, ОТ",
		"OT+HVAC": "ОТ, ОВ",
		"OT+VK": "ОТ, ВК",
		"VK+OT": "ВК, ОТ",
		"VK+KV": "ВК, КВ",
		"VK+PT": "ВК, ПТ",
		"PD+OT+VK+LC": "ПД, ОТ, ВК, СС",
		"HVAC+VK+KV": "ОВ, ВК, ОВ",
		"HVAC+VK+OT": "ОВ, ВК, ОТ",
		"HVAC+VK+EL": "ОВ, ВК, ЭМ",
		"HVAC+VK+KV+EL": "ОВ, ВК, КВ, ЭМ",
		"HVAC+PT": "ОВ, ПТ",
		"DU+PD": "ДУ, ПД",
		"DU+PT": "ДУ, ПТ",
		"FF+EOM": "ПТ, ЭМ",
		"VK+KV+EOM+SS": "ВК, КВ, ЭМ, СС",
		"VK+PD+PT": "ВК, ПД, ПТ",
		"VK+HVAC+PT+OT+PD": "ВК, ОВ, ПТ, ОТ, ПД",
		"HVAC+EL": "ОВ, ЭМ",
		"KV+EL": "КВ, ЭМ",
		"OT+EL": "ОТ, ЭМ",
		"EL+OT": "ЭМ, ОТ",
		"KV+VK": "КВ, ВК",
		"KV+VK+EL": "КВ, ВК, ЭМ",
}


def orient(elem):
		vector = elem.HandOrientation

		if vector.X == 1 or vector.X == -1:
				_bool = True
		else:
				_bool = False
		return _bool


def ElevationDecorator(elev):
		elev = str(int(float(elev)))
		if elev >= 0:
				elev = "+" + elev
		if len(elev) < 4:
				elev = elev[0] + "00" + elev[1:]
		if len(elev) < 5:
				elev = elev[0] + "0" + elev[1:]

		return elev[:-3] + ',' + elev[-3:]


def OwnerTranslator(string):
		owner = []
		string = string.split('+')
		owner.append(OwnerDict[string[0]])
		if len(string) > 1:
			for i in string[1:]:
				owner.append(OwnerDict[i])
		return ", ".join(owner)



def VoidHandler(void):
		if void.LookupParameter("Center Direction Z Instance").AsDouble():
				void.LookupParameter("UD_Ось направления").Set("V")
				if orient(void):
						height = void.LookupParameter("magi_width_instance").AsDouble()
						width = void.LookupParameter("magi_height_instance").AsDouble()
				else:
						height = void.LookupParameter("magi_height_instance").AsDouble()
						width = void.LookupParameter("magi_width_instance").AsDouble()
		else:
				void.LookupParameter("UD_Ось направления").Set("H")
				height = void.LookupParameter("magi_height_instance").AsDouble()
				width = void.LookupParameter("magi_width_instance").AsDouble()
		length = void.LookupParameter("magi_length_instance").AsDouble()
		owner = void.LookupParameter("magi_owner").AsString()
		BottomElevation = void.LookupParameter(
				"MC Bottom Elevation").AsValueString()
		BottomElevationAbs = void.LookupParameter("MC Bottom Elevation abs")\
				.AsValueString()
		void.LookupParameter("ADSK_Отверстие_Высота").Set(height)
		if void.LookupParameter("UD_Задание.Дата").AsString() == "":
				void.LookupParameter("UD_Задание.Дата").Set(today.strftime("%d.%m.%Y"))

		void.LookupParameter("ADSK_Отверстие_Ширина").Set(width)
		void.LookupParameter("ADSK_Отверстие_Глубина").Set(length)
		void.LookupParameter("ADSK_Отверстие_Функция").Set(OwnerTranslator(owner))
		void.LookupParameter("О_Отметка расположения")\
				.Set(ElevationDecorator(BottomElevationAbs))
		void.LookupParameter("О_Отметка от чистого пола")\
				.Set(ElevationDecorator(BottomElevation))
		try:
				void.LookupParameter("UD_Parent_ID").Set(void.Id.ToString())
		except:
				pass


col = FilteredElementCollector(doc).OfCategory(
		BuiltInCategory.OST_GenericModel)
col = col.WhereElementIsNotElementType().ToElements()
voids = [i for i in col if i.Name.Contains("MagiCAD_ProvisionForVoid")]

t = Transaction(doc)
t.Start("voids handle")

for void in voids:
		VoidHandler(void)


t.Commit()

