# -*- coding: utf-8 -*-


__doc__ = 'Анализ параметров и заполнения FSK'
__author__ = '@unidraft'
__version__ = '0.0.0'
__title__ = "FSK классификатор"


from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import *
from Autodesk.Revit.DB.Analysis import *

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.UI import TaskDialogCommonButtons
from Autodesk.Revit.UI import TaskDialogResult
from Autodesk.Revit.UI import UIApplication


""" Export Levels state from Excel file """ 
import clr

clr.AddReference('System.Windows.Forms')
clr.AddReference('Microsoft.Office.Interop.Excel')

from System.Collections.Generic import *
from System.Windows.Forms import *
import Microsoft.Office.Interop.Excel as Excel

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

Param = list(sheet.UsedRange.Columns[1].Cells.Value2)
names = list(sheet.UsedRange.Columns[2].Cells.Value2)

ex.Quit()



ParamDic = zip(Param, names)






cat = [
  BuiltInCategory.OST_CableTray,
  BuiltInCategory.OST_CableTrayFitting,
  BuiltInCategory.OST_DuctCurves,
  BuiltInCategory.OST_DuctFitting,
  BuiltInCategory.OST_DuctAccessory,
  BuiltInCategory.OST_DuctTerminal,
  BuiltInCategory.OST_MechanicalEquipment,
  BuiltInCategory.OST_FlexDuctCurves,
  BuiltInCategory.OST_DuctInsulations,
  BuiltInCategory.OST_PipeAccessory,
  BuiltInCategory.OST_PipeCurves,
  BuiltInCategory.OST_PipeFitting,
  BuiltInCategory.OST_PipeInsulations,
  BuiltInCategory.OST_PlumbingFixtures,
  BuiltInCategory.OST_ElectricalEquipment,
  BuiltInCategory.OST_Sprinklers
  ]


def Handler(el):
  phrase = []
  for i in range(len(Param)):
    string1 = ""
    string2 = ""
    string3 = ""
    string4 = ""
    try:
      string1 = el.LookupParameter(Param[i]).AsString()
      string2 = el.LookupParameter(Param[i]).AsValueString()
      
      #print el.LookupParameter(Param[i]).AsString()
    except AttributeError:
      pass
    try:
      Type = doc.GetElement(el.GetTypeId())
      string3 = Type.LookupParameter(Param[i]).AsString()
      string4 = Type.LookupParameter(Param[i]).AsValueString()
    except AttributeError:
      pass
    
    if string1 != "" and string1 is not None:
      phrase.append(names[i])
      # phrase.append(" : ")
      phrase.append(string1)
      # phrase.append(", ")
    elif string2 != "" and string2 is not None:
      phrase.append(names[i])
      # phrase.append(" : ")
      phrase.append(string2)
      # phrase.append(", ")
    elif string3 != "" and string3 is not None:
      phrase.append(names[i])
      # phrase.append(" : ")
      phrase.append(string3)
      # phrase.append(", ")
    elif string4 !="" and string4 is not None:
      phrase.append(names[i])
      # phrase.append(" : ")
      phrase.append(string4)
      # phrase.append(", ")
    else:
      continue
  phrase = [i for i in phrase if type(i)== str]
  #print " ".join(phrase)
  #print ' '.join(phrase)
  el.LookupParameter("ФСК_Описание").Set(' '.join(phrase))

# Запускает обработку

elements = []

for c in cat:
  [elements.append(i) for i in FilteredElementCollector(doc).OfCategory(c).\
    WhereElementIsNotElementType().ToElements()]

t = Transaction(doc, "elements handle...")
t.Start()

for el in elements:
  Handler(el)
#for k in ParamDic:
#  print k

t.Commit()






