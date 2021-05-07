# -*- coding: utf-8 -*-

__doc__ = """Назначить материалы для фиттингов MR_Материал_текст"""
__author__ = '@unidraft'
__version__ = '0.0.0'
__title__ = "MR_Материал_текст"


import clr

clr.AddReference('System.Windows.Forms')
clr.AddReference('Microsoft.Office.Interop.Excel')


from System.Windows.Forms import *
import Microsoft.Office.Interop.Excel as Excel

# Revit dependancy section

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *


uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

PATH = r"c:\\"

fd = OpenFileDialog()
fd.InitialDirectory = PATH
fd.Filter = "All files (*.*)|*.*"
fd.FilterIndex = 2
fd.RestoreDirectory = False
if fd.ShowDialog() == DialogResult.OK:
  file = fd.FileName
else:
  raise SystemExit


ex = Excel.ApplicationClass()
book = ex.Workbooks.Open(file, ReadOnly = True)
sheet = book.Sheets[1]

pipe_systems = sheet.UsedRange.Columns[1].Cells.Value2
materials = sheet.UsedRange.Columns[2].Cells.Value2

ex.Quit()

finalDic = {}

for pipe_system, material in zip(pipe_systems, materials):
    finalDic[pipe_system] = material

# print finalDic

def ParameterAdd(name, group):
  # TaskDialog.Show("Ошибка!", "func start!")
  file = doc.Application.OpenSharedParameterFile()
  param = file.Groups[group].Definitions[name]
  _category = Category.GetCategory(doc, BuiltInCategory.OST_PipeFitting)
  _cats = doc.Application.Create.NewCategorySet()
  _cats.Insert(_category)
  instanceBinding = doc.Application.Create.NewInstanceBinding(_cats)
  bindingMap = doc.ParameterBindings
  instanceBindOK = bindingMap.Insert(param, instanceBinding, BuiltInParameterGroup.PG_TEXT)
  if not instanceBindOK:
    instanceBindOK = bindingMap.ReInsert(param, instanceBinding, BuiltInParameterGroup.PG_TEXT)
  # TaskDialog.Show("Ошибка!", str(instanceBindOK))
  return instanceBindOK

t = Transaction(doc, "setting matirials...")
t.Start()

ParameterAdd("MR_Материал_текст", "MR")

er_count = 0

fittings = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_PipeFitting).WhereElementIsNotElementType().ToElements()
for f in fittings:
	sys_type = f.get_Parameter(BuiltInParameter.ROUTING_PREFERENCE_PARAM).AsValueString()
	if sys_type in finalDic:
		f.LookupParameter("MR_Материал_текст").Set(finalDic[sys_type])
	else:
		f.LookupParameter("MR_Материал_текст").Set("Не назначен материал для данного Типа трубопровода")
		er_count += 1

t.Commit()

msg = "Необработанно элементов : "
msg += str(er_count)

TaskDialog.Show("Отчет", msg)