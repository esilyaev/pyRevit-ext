# -*- coding: utf-8 -*-
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import *
from Autodesk.Revit.DB.Analysis import *

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.UI import TaskDialogCommonButtons
from Autodesk.Revit.UI import TaskDialogResult
from Autodesk.Revit.UI import UIApplication

import clr
import System
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
from System.Windows.Forms import *
from System.Drawing import *

LINK = "\\\\fs-uni\\BIM\\Library\\Revit\\00_Проигрыватель Dynamo\\UD_Описание дверей_v1\\Эскизы дверей"

class MainForm(System.Windows.Forms.Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._tabControl1 = System.Windows.Forms.TabControl()
		self._tabPage1 = System.Windows.Forms.TabPage()
		self._tabPage2 = System.Windows.Forms.TabPage()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._checkedListBox1 = System.Windows.Forms.CheckedListBox()
		self._label3 = System.Windows.Forms.Label()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._button1 = System.Windows.Forms.Button()
		self._tabControl1.SuspendLayout()
		self._tabPage1.SuspendLayout()
		self._tabPage2.SuspendLayout()
		self.SuspendLayout()
		# 
		# tabControl1
		# 
		self._tabControl1.Controls.Add(self._tabPage1)
		self._tabControl1.Controls.Add(self._tabPage2)
		self._tabControl1.Font = System.Drawing.Font("ISOCPEUR", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 204)
		self._tabControl1.Location = System.Drawing.Point(12, 12)
		self._tabControl1.Name = "tabControl1"
		self._tabControl1.SelectedIndex = 0
		self._tabControl1.Size = System.Drawing.Size(409, 427)
		self._tabControl1.TabIndex = 0
		# 
		# tabPage1
		# 
		self._tabPage1.Controls.Add(self._button1)
		self._tabPage1.Controls.Add(self._comboBox1)
		self._tabPage1.Controls.Add(self._label3)
		self._tabPage1.Controls.Add(self._checkedListBox1)
		self._tabPage1.Controls.Add(self._radioButton3)
		self._tabPage1.Controls.Add(self._radioButton2)
		self._tabPage1.Controls.Add(self._radioButton1)
		self._tabPage1.Controls.Add(self._label1)
		self._tabPage1.Font = System.Drawing.Font("ISOCPEUR", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 204)
		self._tabPage1.Location = System.Drawing.Point(4, 30)
		self._tabPage1.Name = "tabPage1"
		self._tabPage1.Padding = System.Windows.Forms.Padding(3)
		self._tabPage1.Size = System.Drawing.Size(401, 403)
		self._tabPage1.TabIndex = 0
		self._tabPage1.Text = "Скрипт"
		self._tabPage1.UseVisualStyleBackColor = True
		# 
		# tabPage2
		# 
		self._tabPage2.Controls.Add(self._label2)
		self._tabPage2.Location = System.Drawing.Point(4, 30)
		self._tabPage2.Name = "tabPage2"
		self._tabPage2.Padding = System.Windows.Forms.Padding(3)
		self._tabPage2.Size = System.Drawing.Size(401, 403)
		self._tabPage2.TabIndex = 1
		self._tabPage2.Text = "Инструкция"
		self._tabPage2.UseVisualStyleBackColor = True
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("ISOCPEUR", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 204)
		self._label1.Location = System.Drawing.Point(22, 26)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(171, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Вариант выборки:"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(18, 20)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(374, 383)
		self._label2.TabIndex = 0
		self._label2.Text = """1. Совместимые семейства дверей:
	- UD_Дверь
	- UD_Дверь стеклянная
2. Соответствие значений параметров "UD_DR_ГОСТ", "UD_DR_Материал" материалам дверей:
	- стальная - "UD_DR_ГОСТ" = ГОСТ 31173-2016
	- стальная - "UD_DR_ГОСТ" = Серия 5.904-4, "UD_DR_Гермодверь" = Да
	- ПВХ - "UD_DR_ГОСТ" = ГОСТ 30970-2014
	- алюминиевая - "UD_DR_ГОСТ" = ГОСТ 23747-2015
	- деревянная - "UD_DR_ГОСТ" = ГОСТ 475-2016
	- стеклянная - "UD_DR_ГОСТ" = индивидуальное изготовление, "UD_DR_Материал" = Стекло
	- индивидуальное изготовление - "UD_DR_ГОСТ" = индивидуальное изготовление"""
		# 
		# radioButton1
		# 
		self._radioButton1.Font = System.Drawing.Font("ISOCPEUR", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 204)
		self._radioButton1.Location = System.Drawing.Point(22, 70)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(213, 24)
		self._radioButton1.TabIndex = 1
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Предварительно выбранные"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Font = System.Drawing.Font("ISOCPEUR", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 204)
		self._radioButton2.Location = System.Drawing.Point(22, 100)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(199, 24)
		self._radioButton2.TabIndex = 2
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "По выбранным уровням"
		self._radioButton2.UseVisualStyleBackColor = True
		self._radioButton2.Checked=False
		self._radioButton2.CheckedChanged+=self.rB2_CC
		# 
		# radioButton3
		# 
		self._radioButton3.Font = System.Drawing.Font("ISOCPEUR", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 204)
		self._radioButton3.Location = System.Drawing.Point(22, 296)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(171, 24)
		self._radioButton3.TabIndex = 3
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Во всем проекте"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# checkedListBox1
		# 
		self._checkedListBox1.Font = System.Drawing.Font("ISOCPEUR", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 204)
		self._checkedListBox1.FormattingEnabled = True
		self._checkedListBox1.Location = System.Drawing.Point(22, 130)
		self._checkedListBox1.Name = "checkedListBox1"
		self._checkedListBox1.Size = System.Drawing.Size(360, 158)
		self._checkedListBox1.TabIndex = 4
		[self._checkedListBox1.Items.Add(i.Name) for i in levelMas]
		self._checkedListBox1.SelectionMode=SelectionMode.None
		self._checkedListBox1.CheckOnClick=True
		self._checkedListBox1.MultiColumn=True
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("ISOCPEUR", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 204)
		self._label3.Location = System.Drawing.Point(22, 343)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(128, 23)
		self._label3.TabIndex = 5
		self._label3.Text = "Стадия:"
		# 
		# comboBox1
		# 
		self._comboBox1.Font = System.Drawing.Font("ISOCPEUR", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 204)
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Location = System.Drawing.Point(83, 341)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(149, 29)
		self._comboBox1.TabIndex = 6
		[self._comboBox1.Items.Add(i.Name) for i in phaseCol]
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("ISOCPEUR", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 204)
		self._button1.Location = System.Drawing.Point(289, 338)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 30)
		self._button1.TabIndex = 7
		self._button1.Text = "Ок"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1_Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(445, 485)
		self.MaximumSize = System.Drawing.Size(445, 485)
		self.MinimumSize = System.Drawing.Size(445, 485)
		self.Controls.Add(self._tabControl1)
		self.Name = "MainForm"
		self.Text = "DR"
		self._tabControl1.ResumeLayout(False)
		self._tabPage1.ResumeLayout(False)
		self._tabPage2.ResumeLayout(False)
		self.ResumeLayout(False)


	def rB2_CC(self,sender,e):
		if self._radioButton2.Checked==True:
			self._checkedListBox1.SelectionMode=SelectionMode.One
		else:
			self._checkedListBox1.SelectionMode=SelectionMode.None
			[self._checkedListBox1.SetItemCheckState(i,CheckState.Unchecked) for i,level in enumerate(levelCol)]
		
	def Button1_Click(self, sender, e):
		doorCol=FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Doors).WhereElementIsNotElementType().ToElements()
		if self._radioButton1.TabStop==True:
			doorMas=[doc.GetElement(i) for i in uidoc.Selection.GetElementIds() if doc.GetElement(i).Category.Name=='Двери']
		elif self._radioButton2.TabStop==True:
			doorMas=[]
			for i, lev in enumerate(levelMas):
				if self._checkedListBox1.GetItemChecked(i)==True:
					for door in doorCol:
						if door.LevelId.IntegerValue==lev.Id.IntegerValue:
							doorMas.append(door)
							
		else:
			doorMas=[i for i in doorCol]
		doorMas=[i for i in doorMas if self._comboBox1.SelectedItem.ToString()==doc.GetElement(i.CreatedPhaseId).Name if i.Symbol.LookupParameter('Ключевая пометка').AsString()=='Скрипт']
		if len(doorMas)==0:
			self.Close()
		if self._radioButton3.TabStop==True:
			imageReLoad()
		if len(doorMas)>0 and doorMas[0].LookupParameter('UD_DR_Изображение') is None:
			paramLoad('UD_DR_Изображение')

		[imageSet(i) for i in doorMas]
		[gabSet(i) for i in doorMas]
		[naimSet(i) for i in doorMas]
		[prSet(i) for i in doorMas]
		
		
		msgBox = TaskDialog
		msgBox.Show("Результат:", "Дверей обработано : " + str(len(doorMas)))
		
		self.Close()

def imageReLoad():
	imTypeCol=FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_RasterImages).WhereElementIsElementType().ToElements()
	imNameMas=['error.jpg','ГД.jpg','Д.jpg','ДГ.jpg','ДГ_ФГ.jpg','ДГ_ФО.jpg','ДО.jpg','ДО_ФГ.jpg','ДО_ФО.jpg','ДОх4.jpg','ДОх4_ФГ.jpg','ДОх4_ФО.jpg','ДОГ.jpg','ДОГ_ФГ.jpg','ДОГ_ФО.jpg','ДОх2Г.jpg','ДОх2Г_ФГ.jpg','ДОх2Г_ФО.jpg','ОГ.jpg','ОГ_ФГ.jpg','ОГ_ФО.jpg','ОГР.jpg','ОО.jpg','ОО_ФГ.jpg','ОО_ФО.jpg','ООР.jpg','ООх2.jpg','ООх2_ФГ.jpg','ООх2_ФО.jpg','РГ.jpg','РГ_ФГ.jpg','РГ_ФО.jpg','РО.jpg','РО_ФГ.jpg','РО_ФО.jpg','РОх2Г.jpg','РОх2Г_ФГ.jpg','РОх2Г_ФО.jpg','РОГ.jpg','РОГ_ФГ.jpg','РОГ_ФО.jpg','РООт.jpg','РОх4.jpg','РОх4_ФГ.jpg','РОх4_ФО.jpg','ЛК.jpg','Вр.jpg','ООу.jpg','ООу_ФГ.jpg','ООу_ФО.jpg','РОу.jpg','РОу_ФГ.jpg','РОу_ФО.jpg','ДОу.jpg','ДОу_ФГ.jpg','ДОу_ФО.jpg','ДОГу.jpg','ДОГу_ФГ.jpg','ДОГу_ФО.jpg']
	for imType in imTypeCol:
		for imName in imNameMas:
			if imType.get_Parameter(BuiltInParameter.ALL_MODEL_TYPE_NAME).AsString()==imName:
				doc.Delete(imType.Id)
				break
	[ImageType.Create(doc,LINK+'/'+imName) for imName in imNameMas]

def paramLoad(paramName):
	file=app.OpenSharedParameterFile()
	cats=app.Create.NewCategorySet()
	[cats.Insert(item) for item in doc.Settings.Categories if item.Name.ToString()=='Двери']
	bind=app.Create.NewInstanceBinding(cats)
	paramType=[type for type in System.Enum.GetValues(ParameterType) if type.ToString()=='Image']
	paramGroup=[item for item in System.Enum.GetValues(BuiltInParameterGroup) if item.ToString()=='PG_DATA']
	opt=ExternalDefinitionCreationOptions(paramName,paramType[0])
	opt.Visible=True
	group=file.Groups.get_Item('GKS_Arch_DR')
	_def=group.Definitions.Item[paramName]
	doc.ParameterBindings.Insert(_def,bind,paramGroup[0])

def imageSet(el):
	picCol=FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_RasterImages).WhereElementIsElementType().ToElements()
	picName=''
	if el.get_Parameter(BuiltInParameter.ELEM_FAMILY_PARAM).AsValueString()=='UD_Дверь стеклянная':
		picName='Д.jpg'
	elif el.get_Parameter(BuiltInParameter.ELEM_FAMILY_PARAM).AsValueString()=='UD_Дверь откатная_2Ст':
		picName='РООт.jpg'
	elif el.Symbol.LookupParameter('UD_DR_Двустворчатая').AsInteger()==0:
		if el.LookupParameter('UD_DR_Гермодверь').AsInteger()==1:
			picName='ГД.jpg'
		elif el.LookupParameter('Стекло_слева').AsInteger()==0:
			if el.LookupParameter('Фрамуга').AsInteger()==1:
				if el.LookupParameter('Открывание фрамуги').AsInteger()==1:
					picName='ОГ_ФО.jpg'
				else:
					picName='ОГ_ФГ.jpg'
			else:
				if el.LookupParameter('Решетка').AsInteger()==0:
					picName='ОГ.jpg'
				else:
					picName='ОГР.jpg'
		elif el.LookupParameter('Стекло_слева').AsInteger()==1:
			if el.LookupParameter('Стекло_слева2').AsInteger()==1:
				if el.LookupParameter('Фрамуга').AsInteger()==1:
					if el.LookupParameter('Открывание фрамуги').AsInteger()==1:
						picName='ООх2_ФО.jpg'
					else:
						picName='ООх2_ФГ.jpg'
				else:
					picName='ООх2.jpg'
			else:
				if el.LookupParameter('Фрамуга').AsInteger()==1:
					if el.LookupParameter('Открывание фрамуги').AsInteger()==1:
						if el.LookupParameter('Отметка_остекления').AsDouble()*304.8>500:
							picName='ОО_ФО.jpg'
						else:
							picName='ООу_ФО.jpg'
					else:
						if el.LookupParameter('Отметка_остекления').AsDouble()*304.8>500:
							picName='ОО_ФГ.jpg'
						else:
							picName='ООу_ФГ.jpg'
				else:
					if el.LookupParameter('Решетка').AsInteger()==0:
						if el.LookupParameter('Отметка_остекления').AsDouble()*304.8>500:
							picName='ОО.jpg'
						else:
							picName='ООу.jpg'
					else:
						picName='ООР.jpg'
	elif el.Symbol.LookupParameter('UD_DR_Равнопольная').AsInteger()==1:
		if el.LookupParameter('Фрамуга').AsInteger()==0:
			if el.LookupParameter('Стекло_слева').AsInteger()==1 and el.LookupParameter('Стекло_справа').AsInteger()==1 and el.LookupParameter('Стекло_слева2').AsInteger()==1 and el.LookupParameter('Стекло_справа2').AsInteger()==1:
				picName='РОх4.jpg'
			elif el.LookupParameter('Стекло_слева').AsInteger()==1 and el.LookupParameter('Стекло_справа').AsInteger()==1:
				if el.LookupParameter('Отметка_остекления').AsDouble()*304.8>500:
					picName='РО.jpg'
				else:
					picName='РОу.jpg'
			elif (el.LookupParameter('Стекло_слева').AsInteger()==1 and el.LookupParameter('Стекло_слева2').AsInteger()==1) or (el.LookupParameter('Стекло_справа').AsInteger()==1 and el.LookupParameter('Стекло_справа2').AsInteger()==1):
				picName='РОх2Г.jpg'
			elif el.LookupParameter('Стекло_слева').AsInteger()==1 or el.LookupParameter('Стекло_справа').AsInteger()==1:
				picName='РОГ.jpg'
			else:
				picName='РГ.jpg'
		elif el.LookupParameter('Открывание фрамуги').AsInteger()==0:
			if el.LookupParameter('Стекло_слева').AsInteger()==1 and el.LookupParameter('Стекло_справа').AsInteger()==1 and el.LookupParameter('Стекло_слева2').AsInteger()==1 and el.LookupParameter('Стекло_справа2').AsInteger()==1:
				picName='РОх4_ФГ.jpg'
			elif el.LookupParameter('Стекло_слева').AsInteger()==1 and el.LookupParameter('Стекло_справа').AsInteger()==1:
				if el.LookupParameter('Отметка_остекления').AsDouble()*304.8>500:
					picName='РО_ФГ.jpg'
				else:
					picName='РОу_ФГ.jpg'
			elif (el.LookupParameter('Стекло_слева').AsInteger()==1 and el.LookupParameter('Стекло_слева2').AsInteger()==1) or (el.LookupParameter('Стекло_справа').AsInteger()==1 and el.LookupParameter('Стекло_справа2').AsInteger()==1):
				picName='РОх2Г_ФГ.jpg'
			elif el.LookupParameter('Стекло_слева').AsInteger()==1 or el.LookupParameter('Стекло_справа').AsInteger()==1:
				picName='РОГ_ФГ.jpg'
			else:
				picName='РГ_ФГ.jpg'
		else:
			if el.LookupParameter('Стекло_слева').AsInteger()==1 and el.LookupParameter('Стекло_справа').AsInteger()==1 and el.LookupParameter('Стекло_слева2').AsInteger()==1 and el.LookupParameter('Стекло_справа2').AsInteger()==1:
				picName='РОх4_ФО.jpg'
			elif el.LookupParameter('Стекло_слева').AsInteger()==1 and el.LookupParameter('Стекло_справа').AsInteger()==1:
				if el.LookupParameter('Отметка_остекления').AsDouble()*304.8>500:
					picName='РО_ФО.jpg'
				else:
					picName='РОу_ФО.jpg'
			elif (el.LookupParameter('Стекло_слева').AsInteger()==1 and el.LookupParameter('Стекло_слева2').AsInteger()==1) or (el.LookupParameter('Стекло_справа').AsInteger()==1 and el.LookupParameter('Стекло_справа2').AsInteger()==1):
				picName='РОх2Г_ФО.jpg'
			elif el.LookupParameter('Стекло_слева').AsInteger()==1 or el.LookupParameter('Стекло_справа').AsInteger()==1:
				picName='РОГ_ФО.jpg'
			else:
				picName='РГ_ФО.jpg'
	else:
		if el.LookupParameter('Фрамуга').AsInteger()==0:
			if el.LookupParameter('Стекло_слева').AsInteger()==1 and el.LookupParameter('Стекло_справа').AsInteger()==1 and el.LookupParameter('Стекло_слева2').AsInteger()==1 and el.LookupParameter('Стекло_справа2').AsInteger()==1:
				picName='ДОх4.jpg'
			elif el.LookupParameter('Стекло_слева').AsInteger()==1 and el.LookupParameter('Стекло_справа').AsInteger()==1:
				if el.LookupParameter('Отметка_остекления').AsDouble()*304.8>500:
					picName='ДО.jpg'
				else:
					picName='ДОу.jpg'
			elif (el.LookupParameter('Стекло_слева').AsInteger()==1 and el.LookupParameter('Стекло_слева2').AsInteger()==1) or (el.LookupParameter('Стекло_справа').AsInteger()==1 and el.LookupParameter('Стекло_справа2').AsInteger()==1):
				picName='ДОх2Г.jpg'
			elif el.LookupParameter('Стекло_слева').AsInteger()==1 or el.LookupParameter('Стекло_справа').AsInteger()==1:
				if el.LookupParameter('Отметка_остекления').AsDouble()*304.8>500:
					picName='ДОГ.jpg'
				else:
					picName='ДОГу.jpg'
			else:
				picName='ДГ.jpg'
		elif el.LookupParameter('Открывание фрамуги').AsInteger()==0:
			if el.LookupParameter('Стекло_слева').AsInteger()==1 and el.LookupParameter('Стекло_справа').AsInteger()==1 and el.LookupParameter('Стекло_слева2').AsInteger()==1 and el.LookupParameter('Стекло_справа2').AsInteger()==1:
				picName='ДОх4_ФГ.jpg'
			elif el.LookupParameter('Стекло_слева').AsInteger()==1 and el.LookupParameter('Стекло_справа').AsInteger()==1:
				if el.LookupParameter('Отметка_остекления').AsDouble()*304.8>500:
					picName='ДО_ФГ.jpg'
				else:
					picName='ДОу_ФГ.jpg'
			elif (el.LookupParameter('Стекло_слева').AsInteger()==1 and el.LookupParameter('Стекло_слева2').AsInteger()==1) or (el.LookupParameter('Стекло_справа').AsInteger()==1 and el.LookupParameter('Стекло_справа2').AsInteger()==1):
				picName='ДОх2Г_ФГ.jpg'
			elif el.LookupParameter('Стекло_слева').AsInteger()==1 or el.LookupParameter('Стекло_справа').AsInteger()==1:
				if el.LookupParameter('Отметка_остекления').AsDouble()*304.8>500:
					picName='ДОГ_ФГ.jpg'
				else:
					picName='ДОГу_ФГ.jpg'
			else:
				picName='ДГ_ФГ.jpg'
		else:
			if el.LookupParameter('Стекло_слева').AsInteger()==1 and el.LookupParameter('Стекло_справа').AsInteger()==1 and el.LookupParameter('Стекло_слева2').AsInteger()==1 and el.LookupParameter('Стекло_справа2').AsInteger()==1:
				picName='ДОх4_ФО.jpg'
			elif el.LookupParameter('Стекло_слева').AsInteger()==1 and el.LookupParameter('Стекло_справа').AsInteger()==1:
				if el.LookupParameter('Отметка_остекления').AsDouble()*304.8>500:
					picName='ДО_ФО.jpg'
				else:
					picName='ДОу_ФО.jpg'
			elif (el.LookupParameter('Стекло_слева').AsInteger()==1 and el.LookupParameter('Стекло_слева2').AsInteger()==1) or (el.LookupParameter('Стекло_справа').AsInteger()==1 and el.LookupParameter('Стекло_справа2').AsInteger()==1):
				picName='ДОх2Г_ФО.jpg'
			elif el.LookupParameter('Стекло_слева').AsInteger()==1 or el.LookupParameter('Стекло_справа').AsInteger()==1:
				if el.LookupParameter('Отметка_остекления').AsDouble()*304.8>500:
					picName='ДОГ_ФО.jpg'
				else:
					picName='ДОГу_ФО.jpg'
			else:
				picName='ДГ_ФО.jpg'
	if picName=='':
		picName='error.jpg'
	pic=[i for i in picCol if i.LookupParameter('Имя типа').AsString()==picName][0]
	el.LookupParameter('UD_DR_Изображение').Set(pic.Id)

def gabSet(el):
	gabValue=''
	h=round(el.LookupParameter('UD_DR_Высота').AsDouble()*304.8-el.Symbol.LookupParameter('Монтажный зазор').AsDouble()*304.8)
	w=round(el.LookupParameter('UD_DR_Ширина').AsDouble()*304.8-2*el.Symbol.LookupParameter('Монтажный зазор').AsDouble()*304.8)
	if el.LookupParameter('UD_DR_Изображение').AsValueString()=='Д.jpg':
		gabValue='h3 = '+dNull(h)+'\nw3 = '+dNull(w)
	elif el.LookupParameter('UD_DR_Изображение').AsValueString()=='ГД.jpg':
		h1=h-2*round(el.Symbol.LookupParameter('Ширина коробки сверху').AsDouble()*304.8)
		w1=w-2*round(el.Symbol.LookupParameter('Ширина коробки').AsDouble()*304.8)
		gabValue='h = '+dNull(h)+'\nw = '+dNull(w)+'\nh1 = '+dNull(h1)+'\nw1 = '+dNull(w1)
	elif el.LookupParameter('UD_DR_Изображение').AsValueString()=='error.jpg':
		gabValue='o0oo'
	else:
		gabValue='h = '+dNull(h)+'\nw = '+dNull(w)
		if el.LookupParameter('Фрамуга').AsInteger()==1:
			h2=round(el.LookupParameter('Высота фрамуги').AsDouble()*304.8)
			hI=h-h2-round(el.Symbol.LookupParameter('Ширина коробки сверху').AsDouble()*304.8)
			h1=hI+round(el.Symbol.LookupParameter('UD_DR_Заглубление полотна').AsDouble()*304.8)
			gabValue=gabValue+'\nh1 = '+dNull(h1)+'\nh2 = '+dNull(h2)+"\nh' = "+dNull(hI)
		else:
			hI=h-round(el.Symbol.LookupParameter('Ширина коробки сверху').AsDouble()*304.8)
			h1=hI+round(el.Symbol.LookupParameter('UD_DR_Заглубление полотна').AsDouble()*304.8)
			gabValue=gabValue+'\nh1 = '+dNull(h1)+"\nh' = "+dNull(hI)
		if el.Symbol.LookupParameter('UD_DR_Заглубление полотна') is not None:
			zP=el.Symbol.LookupParameter('UD_DR_Заглубление полотна').AsDouble()*304.8
		else:
			zP=0
		if el.Symbol.LookupParameter('UD_DR_Двустворчатая').AsInteger()==0:
			w1=w-2*round(el.Symbol.LookupParameter('Ширина коробки').AsDouble()*304.8)+2*zP
			gabValue=gabValue+'\nw1 = '+dNull(w1)
		elif el.Symbol.LookupParameter('UD_DR_Равнопольная').AsInteger()==1:
			w1=w/2-round(el.Symbol.LookupParameter('Ширина коробки').AsDouble()*304.8)+zP
			gabValue=gabValue+'\nw1 = '+dNull(w1)+'\nw2 = '+dNull(w1)
		else:
			w1=round(el.LookupParameter('UD_DR_Ширина большей створки').AsDouble()*304.8)
			w2=w-w1-2*round(el.Symbol.LookupParameter('Ширина коробки').AsDouble()*304.8)+2*zP
			gabValue=gabValue+'\nw1 = '+dNull(w1)+'\nw2 = '+dNull(w2)
		if el.Symbol.LookupParameter('UD_DR_Заужение проема') is not None:
			if el.Symbol.LookupParameter('UD_DR_Двустворчатая').AsInteger()==0 and el.Symbol.LookupParameter('UD_DR_Равнопольная').AsInteger()==0:
				wI=w-2*round(el.Symbol.LookupParameter('Ширина коробки').AsDouble()*304.8)-el.Symbol.LookupParameter('UD_DR_Заужение проема').AsDouble()*304.8
			else:
				wI=w-2*round(el.Symbol.LookupParameter('Ширина коробки').AsDouble()*304.8)-el.Symbol.LookupParameter('UD_DR_Заужение проема').AsDouble()*304.8*2
			gabValue+="\nw'="+dNull(wI)
		if el.LookupParameter('UD_DR_Изображение').AsValueString()=='РООт.jpg':
			a=round(el.LookupParameter('Отметка остекления').AsDouble()*304.8)
			c=round(el.LookupParameter('Диаметр остекления').AsDouble()*304.8)
			gabValue=gabValue+'\na = '+dNull(a)+'\nc = '+dNull(c)
		else:
			if el.LookupParameter('UD_DR_Остекленная').AsInteger()==1:
				if el.Symbol.LookupParameter('UD_DR_Двустворчатая').AsInteger()==0:
					if el.LookupParameter('Стекло_слева2').AsInteger()==1:
						a1=round(el.LookupParameter('Отметка_остекления2').AsDouble()*304.8)
						b1=round(el.LookupParameter('Высота_остекления2').AsDouble()*304.8)
						a2=round(el.LookupParameter('Отметка_остекления').AsDouble()*304.8)
						b2=round(el.LookupParameter('Высота_остекления').AsDouble()*304.8)
						c1=round(el.LookupParameter('Ширина_остекления_слева').AsDouble()*304.8)
						gabValue=gabValue+'\na1 = '+dNull(a1)+'\nb1 = '+dNull(b1)+'\na2 = '+dNull(a2)+'\nb2 = '+dNull(b2)+'\nc1 = '+dNull(c1)
					else:
						a=round(el.LookupParameter('Отметка_остекления').AsDouble()*304.8)
						b=round(el.LookupParameter('Высота_остекления').AsDouble()*304.8)
						c1=round(el.LookupParameter('Ширина_остекления_слева').AsDouble()*304.8)
						gabValue=gabValue+'\na = '+dNull(a)+'\nb = '+dNull(b)+'\nc1 = '+dNull(c1)
				else:
					if el.LookupParameter('Стекло_слева').AsInteger()==1 and el.LookupParameter('Стекло_справа').AsInteger()==1 and el.LookupParameter('Стекло_слева2').AsInteger()==1 and el.LookupParameter('Стекло_справа2').AsInteger()==1:
						a1=round(el.LookupParameter('Отметка_остекления2').AsDouble()*304.8)
						b1=round(el.LookupParameter('Высота_остекления2').AsDouble()*304.8)
						a2=round(el.LookupParameter('Отметка_остекления').AsDouble()*304.8)
						b2=round(el.LookupParameter('Высота_остекления').AsDouble()*304.8)
						if round(el.LookupParameter('Ширина_остекления_слева').AsDouble()*304.8)>round(el.LookupParameter('Ширина_остекления_справа').AsDouble()*304.8):
							c1=round(el.LookupParameter('Ширина_остекления_слева').AsDouble()*304.8)
							c2=round(el.LookupParameter('Ширина_остекления_справа').AsDouble()*304.8)
						else:
							c1=round(el.LookupParameter('Ширина_остекления_справа').AsDouble()*304.8)
							c2=round(el.LookupParameter('Ширина_остекления_слева').AsDouble()*304.8)
						gabValue=gabValue+'\na1 = '+dNull(a1)+'\nb1 = '+dNull(b1)+'\na2 = '+dNull(a2)+'\nb2 = '+dNull(b2)+'\nc1 = '+dNull(c1)+'\nc2 = '+dNull(c2)
					elif el.LookupParameter('Стекло_слева').AsInteger()==1 and el.LookupParameter('Стекло_справа').AsInteger()==1 and el.LookupParameter('Стекло_слева2').AsInteger()==0 and el.LookupParameter('Стекло_справа2').AsInteger()==0:
						a=round(el.LookupParameter('Отметка_остекления').AsDouble()*304.8)
						b=round(el.LookupParameter('Высота_остекления').AsDouble()*304.8)
						if round(el.LookupParameter('Ширина_остекления_слева').AsDouble()*304.8)>round(el.LookupParameter('Ширина_остекления_справа').AsDouble()*304.8):
							c1=round(el.LookupParameter('Ширина_остекления_слева').AsDouble()*304.8)
							c2=round(el.LookupParameter('Ширина_остекления_справа').AsDouble()*304.8)
						else:
							c1=round(el.LookupParameter('Ширина_остекления_справа').AsDouble()*304.8)
							c2=round(el.LookupParameter('Ширина_остекления_слева').AsDouble()*304.8)
						gabValue=gabValue+'\na = '+dNull(a)+'\nb = '+dNull(b)+'\nc1 = '+dNull(c1)+'\nc2 = '+dNull(c2)
					elif el.LookupParameter('Стекло_слева').AsInteger()==1 and el.LookupParameter('Стекло_слева2').AsInteger()==1 and el.LookupParameter('Стекло_справа').AsInteger()==0 and el.LookupParameter('Стекло_справа2').AsInteger()==0:
						a1=round(el.LookupParameter('Отметка_остекления2').AsDouble()*304.8)
						b1=round(el.LookupParameter('Высота_остекления2').AsDouble()*304.8)
						a2=round(el.LookupParameter('Отметка_остекления').AsDouble()*304.8)
						b2=round(el.LookupParameter('Высота_остекления').AsDouble()*304.8)
						c1=round(el.LookupParameter('Ширина_остекления_слева').AsDouble()*304.8)
						gabValue=gabValue+'\na1 = '+dNull(a1)+'\nb1 = '+dNull(b1)+'\na2 = '+dNull(a2)+'\nb2 = '+dNull(b2)+'\nc1 = '+dNull(c1)
					elif el.LookupParameter('Стекло_справа').AsInteger()==1 and el.LookupParameter('Стекло_справа2').AsInteger()==1 and el.LookupParameter('Стекло_слева').AsInteger()==0 and el.LookupParameter('Стекло_слева2').AsInteger()==0:
						a1=round(el.LookupParameter('Отметка_остекления2').AsDouble()*304.8)
						b1=round(el.LookupParameter('Высота_остекления2').AsDouble()*304.8)
						a2=round(el.LookupParameter('Отметка_остекления').AsDouble()*304.8)
						b2=round(el.LookupParameter('Высота_остекления').AsDouble()*304.8)
						c1=round(el.LookupParameter('Ширина_остекления_справа').AsDouble()*304.8)
						gabValue=gabValue+'\na1 = '+dNull(a1)+'\nb1 = '+dNull(b1)+'\na2 = '+dNull(a2)+'\nb2 = '+dNull(b2)+'\nc1 = '+dNull(c1)
					elif el.LookupParameter('Стекло_слева').AsInteger()==1 and el.LookupParameter('Стекло_справа').AsInteger()==0 and el.LookupParameter('Стекло_слева2').AsInteger()==0 and el.LookupParameter('Стекло_справа2').AsInteger()==0:
						a=round(el.LookupParameter('Отметка_остекления').AsDouble()*304.8)
						b=round(el.LookupParameter('Высота_остекления').AsDouble()*304.8)
						c1=round(el.LookupParameter('Ширина_остекления_слева').AsDouble()*304.8)
						gabValue=gabValue+'\na = '+dNull(a)+'\nb = '+dNull(b)+'\nc1 = '+dNull(c1)
					elif el.LookupParameter('Стекло_слева').AsInteger()==0 and el.LookupParameter('Стекло_справа').AsInteger()==1 and el.LookupParameter('Стекло_слева2').AsInteger()==0 and el.LookupParameter('Стекло_справа2').AsInteger()==0:
						a=round(el.LookupParameter('Отметка_остекления').AsDouble()*304.8)
						b=round(el.LookupParameter('Высота_остекления').AsDouble()*304.8)
						c1=round(el.LookupParameter('Ширина_остекления_справа').AsDouble()*304.8)
						gabValue=gabValue+'\na = '+dNull(a)+'\nb = '+dNull(b)+'\nc1 = '+dNull(c1)
					else:
						gabValue='думдум'
	el.LookupParameter('UD_DR_Габариты').Set(gabValue)

def naimSet(el):
	naim='Д'
	ghost=el.Symbol.LookupParameter('UD_DR_ГОСТ').AsString()
	
	if ghost=='ГОСТ 31173-2016':
		naim+='C'
	elif ghost=='ГОСТ 30970-2014' or ghost=='ТУ 2249-003-60059117-2010, ГОСТ 30674-99':
		naim+='П'
	elif ghost=='ГОСТ 23747-2015':
		naim+='А'
	elif ghost=='ГОСТ 475-2016':
		naim+=''
	elif ghost=='Серия 5.904-4' and el.LookupParameter('UD_DR_Гермодверь').AsInteger()==1:
		naim+='С'
	elif ghost=='ГОСТ 57327-2016':
		mat='C'
	elif ghost=='ГОСТ Р 53780-2010':
		mat='C'
	elif ghost=='ЛДСП':
		naim+=''
	else:
		naim+='<<Уточни ГОСТ>>'
	if el.LookupParameter('UD_DR_Внутренняя').AsInteger()==1:
		naim+='В '
	else:
		naim+='Н '
	if el.LookupParameter('UD_DR_Остекленная').AsInteger()==1:
		naim+='О'
	else:
		naim+='Г'
	if el.Symbol.LookupParameter('UD_DR_Двустворчатая').AsInteger()==1:
		naim+='Дв'
	if el.LookupParameter('UD_DR_Порог').AsString()!='':
		naim+='П'
	naim+=' '+dNull(round(el.LookupParameter('UD_DR_Высота').AsDouble()*304.8))+'-'+dNull(round(el.LookupParameter('UD_DR_Ширина').AsDouble()*304.8))+' '+ghost
	if ghost=='индивидуальное изготовление' or (el.LookupParameter('UD_DR_Двойное полотно') and el.LookupParameter('UD_DR_Двойное полотно').AsInteger()==1):
		naim='Индивидуальное изготовление'
	el.LookupParameter('UD_DR_Наименование').Set(naim)

def prSet(el):
	pr=''
	if el.Symbol.FamilyName=='UD_Дверь стеклянная':
		pass
	if el.LookupParameter('UD_DR_Внутренняя').AsInteger()==1:
		pr+=' внутренняя,'
	else:
		pr+=' наружная,'
	if el.LookupParameter('UD_DR_Остекленная') and el.LookupParameter('UD_DR_Остекленная').AsInteger()==1:
		pr+=' остекленная,'
	elif el.LookupParameter('UD_DR_Остекленная') and el.LookupParameter('UD_DR_Остекленная').AsInteger()==0:
		pr+=' глухая,'
	if el.LookupParameter('UD_DR_Отделка') and el.LookupParameter('UD_DR_Отделка').AsString()!='':
		pr+=' '+el.LookupParameter('UD_DR_Отделка').AsString()+','
	if el.LookupParameter('UD_DR_Класс') and el.LookupParameter('UD_DR_Класс').AsString()!='':
		pr+=' '+el.LookupParameter('UD_DR_Класс').AsString()+','
	if el.LookupParameter('UD_DR_Гермодверь') and el.LookupParameter('UD_DR_Гермодверь').AsInteger()==1:
		pr+=' герметичная,'
	if el.LookupParameter('UD_DR_Утепление').AsInteger()==1:
		pr+=' утепленная,'
	if el.LookupParameter('UD_DR_Автоматика').AsInteger()==1:
		pr+=' автоматическая,'
	if el.LookupParameter('UD_DR_Рентгенозащита').AsString()!='':
		pr+=' '+el.LookupParameter('UD_DR_Рентгенозащита').AsString()+','
	if el.LookupParameter('UD_DR_Усиление').AsString()!='':
		pr+=' '+el.LookupParameter('UD_DR_Усиление').AsString()+','
	if el.LookupParameter('UD_DR_RAL').AsString()!='':
		pr+=' цвет RAL '+el.LookupParameter('UD_DR_RAL').AsString()+','
	if el.LookupParameter('UD_DR_Звукоизоляция') and el.LookupParameter('UD_DR_Звукоизоляция').AsString()!='':
		pr+=' звукоизоляция '+el.LookupParameter('UD_DR_Звукоизоляция').AsString()+','
	if len(pr)>0:
		pr=pr[:len(pr)-1]
	if el.LookupParameter('UD_DR_Ручка').AsString()!='' or el.LookupParameter('UD_DR_Замок').AsString()!='' or el.LookupParameter('UD_DR_Порог').AsString()!='' or el.LookupParameter('UD_DR_Доводчик').AsInteger()==1 or el.LookupParameter('UD_DR_СКУД').AsInteger()==1 or (el.LookupParameter('Решетка') and el.LookupParameter('Решетка').AsInteger()==1) or (el.LookupParameter('UD_DR_Уплотнение в притворах') and el.LookupParameter('UD_DR_Уплотнение в притворах').AsInteger()==1) or (el.LookupParameter('UD_DR_Цилиндр') and el.LookupParameter('UD_DR_Цилиндр').AsString()!='') or (el.LookupParameter('UD_DR_Накладка на цилиндр') and el.LookupParameter('UD_DR_Накладка на цилиндр').AsString()!='') or (el.LookupParameter('UD_DR_Завертка') and el.LookupParameter('UD_DR_Завертка').AsString!='') or (el.LookupParameter('UD_DR_Петли') and el.LookupParameter('UD_DR_Петли').AsString()!='') or (el.LookupParameter('UD_DR_Дверной упор') and el.LookupParameter('UD_DR_Дверной упор').AsString()!=''):
		pr+=' в комплекте:'
		if el.LookupParameter('UD_DR_Наличники') and el.LookupParameter('UD_DR_Наличники').AsString()!='':
			pr+=' наличники '+el.LookupParameter('UD_DR_Наличники').AsString()+','
		if el.LookupParameter('UD_DR_Уплотнение в притворах') and el.LookupParameter('UD_DR_Уплотнение в притворах').AsInteger()==1:
			pr+=' с уплотнением в притворах,'
		if el.LookupParameter('UD_DR_СКУД').AsInteger()==1:
			pr+=' СКУД,'
		if el.LookupParameter('UD_DR_str_Доводчик') and el.LookupParameter('UD_DR_str_Доводчик').AsString()!='':
			pr+=' доводчик '+el.LookupParameter('UD_DR_str_Доводчик').AsString()+','
		elif el.LookupParameter('UD_DR_Доводчик').AsInteger()==1:
			pr+=' с доводчиком,'
		if el.LookupParameter('UD_DR_Замок').AsString()!='':
			pr+=' замок '+el.LookupParameter('UD_DR_Замок').AsString()+','
		if el.LookupParameter('UD_DR_Ручка').AsString()!='':
			pr+=' ручка '+el.LookupParameter('UD_DR_Ручка').AsString()+','
		if el.LookupParameter('UD_DR_Цилиндр') and el.LookupParameter('UD_DR_Цилиндр').AsString()!='':
			pr+=' цилиндр '+el.LookupParameter('UD_DR_Цилиндр').AsString()+','
		if el.LookupParameter('UD_DR_Накладка на цилиндр') and el.LookupParameter('UD_DR_Накладка на цилиндр').AsString()!='':
			pr+=' накладка на цилиндр '+el.LookupParameter('UD_DR_Накладка на цилиндр').AsString()+','
		if el.LookupParameter('UD_DR_Завертка') and el.LookupParameter('UD_DR_Завертка').AsString()!='':
			pr+=' завертка '+el.LookupParameter('UD_DR_Завертка').AsString()+','
		if el.LookupParameter('UD_DR_Петли') and el.LookupParameter('UD_DR_Петли').AsString()!='':
			pr+=' петли '+el.LookupParameter('UD_DR_Петли').AsString()+','
		if el.LookupParameter('UD_DR_Дверной упор') and el.LookupParameter('UD_DR_Дверной упор').AsString()!='':
			pr+=' '+el.LookupParameter('UD_DR_Дверной упор').AsString()+','
		if el.LookupParameter('UD_DR_Порог').AsString()!='':
			pr+=' порог '+el.LookupParameter('UD_DR_Порог').AsString()+','
		if el.LookupParameter('Решетка') and el.LookupParameter('Решетка').AsInteger()==1:
			pr+=' вентиляционная решетка,'
		pr=pr[:len(pr)-1]
	mat=''
	ghost=el.Symbol.LookupParameter('UD_DR_ГОСТ').AsString()
	if ghost=='ГОСТ 31173-2016':
		mat=' стальная'
	elif ghost=='ГОСТ 30970-2014':
		mat=' ПВХ'
	elif ghost=='ТУ 2249-003-60059117-2010, ГОСТ 30674-99':
		mat=' влагостойкая композитная'
	elif ghost=='ГОСТ 23747-2015':
		mat=' алюминиевая'
	elif ghost=='ГОСТ 475-2016':
		mat=' деревянная'
	elif ghost=='ГОСТ 57327-2016':
		mat=' стальная противопожарная'
	elif ghost=='ГОСТ Р 53780-2010':
		mat=' стальная аварийная лифтовой шахты'
	elif ghost=='Серия 5.904-4' and el.LookupParameter('UD_DR_Гермодверь').AsInteger()==1:
		mat=' стальная'
	elif ghost=='индивидуальное изготовление':
		mat=' '+el.Symbol.LookupParameter('UD_DR_Материал').AsString()
	elif ghost=='ЛДСП':
		mat=' ЛДСП'
	else:
		mat=' <<Уточни ГОСТ>>'
	otkr=''

	if el.LookupParameter('UD_DR_Маятниковая') and el.LookupParameter('UD_DR_Маятниковая').AsInteger()==1:
		otkr=' маятниковая'
	elif el.LookupParameter('UD_DR_Двойное полотно') and el.LookupParameter('UD_DR_Двойное полотно').AsInteger()==1:
		otkr=' двойная'
	if pr!='' or otkr!='':
		pr='Дверь'+mat+otkr+pr
	if mat=='ЛДСП':
		pr='Дверь в комплекте перегородок ЛДСП'
	if el.LookupParameter('Фрамуга') and el.LookupParameter('Фрамуга').AsInteger()==1:
		pr+=', с фрамугой'
	el.LookupParameter('UD_DR_Примечание').Set(pr)

def dNull(val):
	strVal=str(val)
	strVal=strVal[:strVal.find('.')]
	return strVal

###
levelCol=FilteredElementCollector(doc).OfClass(Level).ToElements()
levelMas=[i for i in levelCol]
levelMas.sort(key=lambda i: i.Elevation)
phaseCol=FilteredElementCollector(doc).OfClass(Phase).ToElements()
###

t = Transaction(doc, "doors handle...")
t.Start()
dialog=MainForm()
dialog.ShowDialog()
t.Commit()
