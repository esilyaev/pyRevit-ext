# -*- coding: utf-8 -*-

__doc__ = """Найти стены отделки в помещениях 
		и заполнить параметр ADSK_Примечание"""
__author__ = '@unidraft'
__version__ = '0.0.0'
__title__ = "Найти стены"

from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import *
from Autodesk.Revit.DB.Analysis import *

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.UI import UIApplication

def GetSolidsOfElement(geoElem):
  solids = []
  for  geoObj in geoElem:
    if geoObj.ToString() == 'Autodesk.Revit.DB.GeometryInstance':
      geomIns = geoObj
      instGeoElement = geomIns.GetSymbolGeometry()
      for i in instGeoElement:
        if i.ToString() == 'Autodesk.Revit.DB.Solid':
          if i.Volume == 0:
            pass
          else:
            solids.append(i)
    else:
      if geoObj.ToString() == 'Autodesk.Revit.DB.Solid':
        solids.append(geoObj)
  return solids

t = Transaction(doc, 'SCE')
t.Start()
walls = [i for i in FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType() if i.Name.Contains("_Отделка_")]
coff = 3
for elem in walls:
	#print elem.Id
	#пропускаем те стены у кого "ADSK_Примечание" заполнено
	if elem.LookupParameter("ADSK_Примечание").AsString() != '' and elem.LookupParameter("ADSK_Примечание").AsString() is not None:
		continue
	gopt = Options()
	gelem = elem.get_Geometry(gopt)
	solid = GetSolidsOfElement(gelem)[0]	
	_point = solid.ComputeCentroid()
	point = XYZ(_point.X, _point.Y,elem.Location.Curve.GetEndPoint(0).Z + 3.28)
	offset = elem.WallType.get_Parameter(BuiltInParameter.WALL_ATTR_WIDTH_PARAM).AsDouble()
	room = doc.GetRoomAtPoint(point.Add(XYZ(offset*coff,0,0)))	
	if room:
		number = room.get_Parameter(BuiltInParameter.ROOM_NUMBER).AsString()	
		elem.LookupParameter("ADSK_Примечание").Set(number)
	else:
		room = doc.GetRoomAtPoint(point.Add(XYZ(0,offset*coff,0)))
		if room:
			number = room.get_Parameter(BuiltInParameter.ROOM_NUMBER).AsString()	
			elem.LookupParameter("ADSK_Примечание").Set(number)
		else:
			room = doc.GetRoomAtPoint(point.Subtract(XYZ(offset*coff,0,0)))
			if room:
				number = room.get_Parameter(BuiltInParameter.ROOM_NUMBER).AsString()	
				elem.LookupParameter("ADSK_Примечание").Set(number)
			else:
				room = doc.GetRoomAtPoint(point.Subtract(XYZ(0,offset*coff,0)))
				if room:
					number = room.get_Parameter(BuiltInParameter.ROOM_NUMBER).AsString()	
					elem.LookupParameter("ADSK_Примечание").Set(number)
				else:
					elem.LookupParameter("ADSK_Примечание").Set("Не найдено")			
t.Commit()