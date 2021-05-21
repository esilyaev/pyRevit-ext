# -*- coding: utf-8 -*-
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import *
from Autodesk.Revit.DB.Analysis import *

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.UI import UIApplication

PATH = r"\\Fs-uni\projects\0489.61 - Metropolia-2\03-DESIGN\00-MODEL\RVT" + '\\'
#PATH = r'D:\\'[:-1]

#links_list = [i.Name.split(":")[0].split(".")[0] \
#	for i in FilteredElementCollector(doc).OfClass(RevitLinkInstance)]

def loadAR(nameSec):  
	#загружает все АР модели из словаря, с первой модели получает координаты
	result = loadLink(dicAR[nameSec][0], ar_ws, 'o')
	if result != 1:
		doc.AcquireCoordinates(result.Id)
	if len(dicAR[nameSec]) > 1:
		for name in dicAR[nameSec][1:]:
			loadLink(name, ar_ws, 's')
	

def loadKR(nameSec):
	#загружает все КР модели из словаря
	for name in dicKR[nameSec]:
			loadLink(name, ar_ws, 's')


def loadLink(name, workset, arg):
	# функция загрузки связанного файл, с селектором координат и назначением ворксета
	lopt = RevitLinkOptions(False)
	path = FilePath(PATH + name)
	result = RevitLinkType.Create(doc, path, lopt)
	# загружаем в зависимости от arg по общим координатам или в оригин
	if arg == 's':
		result = RevitLinkInstance.Create(doc, result.ElementId, ImportPlacement.Shared)
	elif arg == 'o':
		result = RevitLinkInstance.Create(doc, result.ElementId, ImportPlacement.Origin)
	else:
		return 1
	# назначаем ворксет
	doc.GetElement(result.Id).get_Parameter(BuiltInParameter.ELEM_PARTITION_PARAM).Set(workset)
	return result


# собираем ID ворксетов "000_Связанные файлы АР" и "000_Связанные файлы ИОС"
wsList = FilteredWorksetCollector(doc).OfKind(WorksetKind.UserWorkset).ToWorksets()

for ws in wsList:
	if ws.Name.Contains("000_Связанные файлы АР"):
		ar_ws = ws.Id.IntegerValue
	if ws.Name.Contains("000_Связанные файлы ИОС"):
		ios_ws = ws.Id.IntegerValue
# словарь моделей АР
dicAR = {
	'0489.61.S1-2':['VLGP02_AR_SPEECH_R19_S1-5.rvt'],
	'0489.61.S3-4-5':['VLGP02_AR_SPEECH_R19_S1-5.rvt'],
	'0489.61.S6-7-8':['VLGP02_AR_SPEECH_R19_S6-11.rvt', 'VLGP02_AR_SPEECH_R19_S7.rvt'],
	'0489.61.S9-10-11':['VLGP02_AR_SPEECH_R19_S6-11.rvt', 'VLGP02_AR_SPEECH_R19_S10.rvt'],
	'0489.61.Sb01':[],
	'0489.61.Sb02':[]
}
# словарь моделей КР
dicKR = {
	'0489.61.S1-2':['VLGP02_KR_MBPB_R19_S1.rvt', 'VLGP02_KR_MBPB_R19_S2-3.rvt'],
	'0489.61.S3-4-5':['VLGP02_KR_MBPB_R19_S2-3.rvt', 'VLGP02_KR_MBPB_R19_S4.rvt',\
	 'VLGP02_KR_MBPB_R19_S5-6.rvt'],
	'0489.61.S6-7-8':['VLGP02_KR_MBPB_R19_S5-6.rvt', 'VLGP02_KR_MBPB_R19_S7.rvt',\
	 'VLGP02_KR_MBPB_R19_S8-9.rvt'],
	'0489.61.S9-10-11':['VLGP02_KR_MBPB_R19_S8-9.rvt', 'VLGP02_KR_MBPB_R19_S10.rvt',\
	 'VLGP02_KR_MBPB_R19_S11.rvt'],
	'0489.61.Sb01':[],
	'0489.61.Sb02':[]
}

_index = doc.PathName.find('0489.61.S')
if _index != -1:
	_index2 = doc.PathName.rfind('_')
	nameSec = doc.PathName[_index:_index2]
	if dicAR.ContainsKey(nameSec):
		t = Transaction(doc, 'Load AR')
		t.Start()
		loadAR(nameSec)
		loadKR(nameSec)
		t.Commit()

