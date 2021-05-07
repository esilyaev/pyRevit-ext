# -*- coding: utf-8 -*-

__doc__ = """Создать 3D виды по системам"""
__author__ = '@unidraft'
__version__ = '0.0.0'
__title__ = "Аксонометрии"

from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import *
from Autodesk.Revit.DB.Analysis import *

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

#dependencies

import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('IronPython.Wpf')

from pyrevit import script
xamlfile = script.get_bundle_file('Viewer.xaml')

import wpf
from System import Windows
from config import Configurator
from create_aks import AksCreator

class MyWindow(Windows.Window):
	"""UI manager"""
	def __init__(self, arg):
		wpf.LoadComponent(self, xamlfile)
		

	def Close_Click(self, sender, args):
		self.Close()

	def Run(self, sender, args):
		t = Transaction(doc, 'filters and views creation...')
		t.Start()
		self.Output.Text = AksCreator(config).Run()
		 
		t.Commit()

	def devMode_Unchecked(self, sender, args):
		config.devMode = False
	def devMode_Checked(self, sender, args):
		config.devMode = True

	def systemCommon_Unchecked(self, sender, args):
		config.systemCommon = False
	def systemCommon_Checked(self, sender, args):
		config.systemCommon = True

	def systemPDV_Unchecked(self, sender, args):
		config.systemPDV = False
	def systemPDV_Checked(self, sender, args):
		config.systemPDV = True

	def FilterByName_Unchecked(self, sender, args):
		config.FilterByName = False
	def FilterByName_Checked(self, sender, args):
		config.FilterByName = True

	def SystemNameFilter_Changed(self, sender, args):
		config.SystemNameFilter = self.SystemNameFilter.Text

	def FilterByNameNotContains_Unchecked(self, sender, args):
		config.FilterByNameNotContains = False
	def FilterByNameNotContains_Checked(self, sender, args):
		config.FilterByNameNotContains = True

	def SystemNameFilterNotContains_Changed(self, sender, args):
		config.SystemNameFilterNotContains = self.SystemNameFilterNotContains.Text

	def Clear(self, sender, args):
		config.Reset()
		self.systemCommon.IsChecked = False
		self.systemPDV.IsChecked = False
		self.FilterByName.IsChecked = False
		self.FilterByNameNotContains.IsChecked = False
		self.SystemNameFilterNotContains.Text = ""
		self.SystemNameFilter.Text = ""



config = Configurator()
MyWindow(xamlfile).ShowDialog()
