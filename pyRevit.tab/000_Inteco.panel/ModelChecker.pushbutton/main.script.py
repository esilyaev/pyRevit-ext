# -*- coding: utf-8 -*-

# import libraries and reference the RevitAPI and RevitAPIUI
import clr
import math
import sys
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *

# import other libraries
from ImportFromExcel import GetRulesOfChecks

from Cheker import Cheker


# set the active Revit application and document
app = __revit__.Application
doc = __revit__.ActiveUIDocument.Document

RuleList = GetRulesOfChecks()
testRule = RuleList["03.03.01.01"]
print(testRule)
Cheker.checkRule(testRule)


# define a transaction variable and describe the transaction
# t = Transaction(doc, 'This is my new transaction')

# start a transaction in the Revit database
# t.Start()

# perform some action here...


# commit the transaction to the Revit database
# t.Commit()

# close the script window
# __window__.Close()
