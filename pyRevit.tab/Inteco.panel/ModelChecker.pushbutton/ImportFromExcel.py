# -*- coding: utf-8 -*-

import clr
clr.AddReference('Microsoft.Office.Interop.Excel')
clr.AddReference('System.Windows.Forms')
import Microsoft.Office.Interop.Excel as Excel
from System.Windows.Forms import *

from collections import defaultdict


class Rule:
  def __init__(self, name):
    self.Name = name
    self.parList = []
    self.Category = ""
    self.ModelNamePart = ""
    self.Code = ""


def createListOfRules(List):
  """create dictionare of Rule with paramList contains Name of Parameters for checking

  Args:
      List (list): list readed from xls file 

  Returns:
      RuleList: dictionare of Rule
  """
  RuleList = defaultdict(dict)
  paramsName = List[0]
  for i in List[1:]:
    if i[0] is not None and i[0] != "INVALID":
      rule = Rule(i[3])
      print("Создано правило с именем:\t" + rule.Name)
      rule.Category = i[0]
      rule.ModelNamePart = i[2]
      rule.Code = i[1]

      # parametrs setup

      for j in range(len(i[4:])):
        if i[j] is not None:
          rule.parList.append(paramsName[j + 4])
      RuleList[rule.Code] = rule

  return RuleList


def GetRulesOfChecks():
  """Load rule of checks from excel

  Returns:
      [type]: [description]
  """

  PATH = "U:\__tmp\Аудит LOD_LOI.xlsx"

  # fd = OpenFileDialog()
  # fd.InitialDirectory = PATH
  # fd.Filter = "All files (*.*)| *.*"
  # fd.FilterIndex = 2
  # fd.RestoreDirectory = False
  # if fd.ShowDialog() == DialogResult.OK:
  #   file = fd.FileName
  # else:
  #   raise SystemExit

  ex = Excel.ApplicationClass()
  book = ex.Workbooks.Open(PATH, ReadOnly=True)

  sheet = book.Sheets[1]

  Array = sheet.UsedRange.Value2

  ex.Quit()

  List = []

  for i in range(Array.GetLength(0)):
    List.append([])
    for j in range(Array.GetLength(1)):
      List[i].append(Array[i, j])

  RulesList = []

  return createListOfRules(List)


if __name__ == "__main__":
  main()
