# -*- coding: utf-8 -*-
__doc__ = 'Export points by *.txt file'
__author__ = '@evgeny.silyaev'
__version__ = '0.0.0'
__title__ = 'export points cloud'

import math

from Autodesk.Revit.DB import FilteredElementCollector, FamilySymbol, XYZ, BuiltInParameter
from Autodesk.Revit.DB.Structure import StructuralType
from rpw import revit, db


from rpw.ui.forms import select_file, Alert
from rpw.ui.forms import FlexForm, Label, TextBox, Separator, Button

components = [
    Label("Смещение по Х:"),
    TextBox('x_transorm', Text="x..."),

    Label("Смещение по Y:"),
    TextBox('y_transorm', Text="y..."),

    Label("Угол поворота:"),
    TextBox('angle', Text="angle"),

    Separator(),
    Button('Погнали'),

]


form = FlexForm('Экспорт облака точек', components)
form.show()

try:
    X_COEF = float(form.values['x_transorm'])
except:
    X_COEF = 15444.0073

try:
    Y_COEF = float(form.values['y_transorm'])
except:
    Y_COEF = 250.8947

try:
    R_COEF = float(form.values['angle'])
except:
    R_COEF = 0.4857


Z_COEF = 0

filepath = select_file('Text files (*.txt) | *txt')
if (filepath != ''):
    print(filepath)

with open(filepath, 'r') as file:
    lines = file.readlines()

points = []


print("X = ", X_COEF, " Y = ", Y_COEF, " Z = ", Z_COEF, "R_COEF = ", R_COEF)

collection = FilteredElementCollector(
    revit.doc).OfClass(FamilySymbol).ToElements()
red = [x for x in collection if x.FamilyName == 'INT_Point'
       and x.get_Parameter(BuiltInParameter.ALL_MODEL_TYPE_NAME).AsString() == "Red"][0]
green = [x for x in collection if x.FamilyName == 'INT_Point'
         and x.get_Parameter(BuiltInParameter.ALL_MODEL_TYPE_NAME).AsString() == "Green"][0]

with db.Transaction('Insert points'):
    if not red.IsActive:
        red.Activate()

    if not green.IsActive:
        green.Activate()

    for line in lines:
        coords = line.split(';')
        trX = (float(coords[1]) - X_COEF) * 3.28084
        trY = (float(coords[0]) - Y_COEF) * 3.28084
        trZ = float(coords[2]) * 3.28084

        localY = (trX * math.cos(R_COEF) -
                  trY * math.sin(R_COEF))
        localX = (trX * math.sin(R_COEF) +
                  trY * math.cos(R_COEF))
        localZ = trZ

        point = XYZ(localX, localY, localZ)
        color = "green"
        if float(coords[6]) > 0.015:
            color = "red"
        points.append([point, color])
        # print(point)

    for point in points:
        if point[1] == "red":
            fs = red
        else:
            fs = green

        revit.doc.Create.NewFamilyInstance(
            point[0], fs, StructuralType.NonStructural)

print("all done!")
