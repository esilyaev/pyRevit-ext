# -*- coding: utf-8 -*-
__doc__ = 'Sanbox для rwp'
__author__ = '@evgeny.silyaev'
__version__ = '0.0.0'
__title__ = 'sandbox'

# import libraries and reference the RevitAPI and RevitAPIUI
import clr
import math
from rpw.db import Collector
from rpw.ui.forms import SelectFromList


col = Collector(of_class='View', is_not_type=True)

namesOfView = [i.Name for i in col]

value = SelectFromList('Select view', namesOfView)

print(value)
