# -*- coding: utf-8 -*-
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
ceilings = [i for i in FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Ceilings).WhereElementIsNotElementType()]
wallsFinish = [i for i in FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType() \
          if i.Name.Contains("_потолок_")]
final = ceilings
[final.append(i) for i in wallsFinish]
t = Transaction(doc, 'SCE')
t.Start()

for elem in final:
	#пропускаем элементы с заполненым ADSK_Примечание
	if elem.LookupParameter("ADSK_Примечание").AsString() != '':
		continue
	gopt = Options()
	gelem = elem.get_Geometry(gopt)
	solid = GetSolidsOfElement(gelem)[0]
	point = solid.ComputeCentroid()
	offset = 3.28
	room = doc.GetRoomAtPoint(point.Subtract(XYZ(0,0,offset)))
	if room:
		number = room.get_Parameter(BuiltInParameter.ROOM_NUMBER).AsString()  
		elem.LookupParameter("ADSK_Примечание").Set(number)
	else:
		room = doc.GetRoomAtPoint(point.Subtract(XYZ(0,0,offset+offset)))
		if room:
			number = room.get_Parameter(BuiltInParameter.ROOM_NUMBER).AsString()  
			elem.LookupParameter("ADSK_Примечание").Set(number)
		else:
			elem.LookupParameter("ADSK_Примечание").Set('Не найдено')
t.Commit()