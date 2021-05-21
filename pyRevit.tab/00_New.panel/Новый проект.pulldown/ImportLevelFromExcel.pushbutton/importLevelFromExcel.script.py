# -*- coding: utf-8 -*-

__doc__ = 'Экспорт уровней из файла xls'
__author__ = '@unidraft'
__version__ = '0.0.0'
__title__ = "Экспорт уровней"

import clr

clr.AddReference('System.Windows.Forms')
clr.AddReference('Microsoft.Office.Interop.Excel')


from System.Windows.Forms import *
import Microsoft.Office.Interop.Excel as Excel

# Revit dependancy section

from Autodesk.Revit.DB import *


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

elevations = sheet.UsedRange.Columns[1].Cells.Value2
names = sheet.UsedRange.Columns[2].Cells.Value2

ex.Quit()

finalDic = {}

for elevation, name in zip(elevations, names):
  if type(elevation) == float:
    finalDic[elevation] = name


curLevels = FilteredElementCollector(doc).OfClass(Level)
curLevelsName = [i.Name for i in curLevels]

t = Transaction(doc, "level creation")
t.Start()
for k, v in finalDic.items():
  level = Level.Create(doc, k * 0.00328084)
  if v in curLevelsName:
    level.Name = v + "_new"
  else:
    level.Name = v
t.Commit()


