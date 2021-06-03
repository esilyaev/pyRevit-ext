# -*- coding: utf-8 -*-

# import libraries and reference the RevitAPI and RevitAPIUI
import clr
import math
import json
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
clr.AddReference('Microsoft.Office.Interop.Excel')
from Autodesk.Revit.DB import *
import Microsoft.Office.Interop.Excel as Excel

# set the active Revit application and document
app = __revit__.Application
doc = __revit__.ActiveUIDocument.Document

PATHTOEXCEL = r"U:\__tmp\source\pyRevit.extension\pyRevit.tab\Export_rev1.xlsx"
PATHTOJSON = r"U:\__tmp\source\pyRevit.extension\pyRevit.tab\elements.json"

with open(PATHTOJSON) as json_file:
  data = json.load(json_file)
  data = json.loads(data)

ex = Excel.ApplicationClass()
book = ex.Workbooks.Open(PATHTOEXCEL)
print ("Opened")
sheet = book.Sheets[1]


# Position for start write data
# set 2 coz table have headers and index running from 1 in excel
i = 2

for line in data:

  print ('Line, %s') % (i)
  sheet.Cells[i, 1].Value2 = line["1"]
  sheet.Cells[i, 2].Value2 = line["2"]
  i += 1

book.Close()
ex.Quit()
