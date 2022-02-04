#!/usr/bin/python3
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import io
import json


def main():

  filepath = r'U:\__tmp\source\pyRevit.extension\pyRevit.tab\2021.09.02_VR4_KR.xml'
  txt = ''
  with io.open(filepath, 'r', encoding='utf-8') as o:
    txt = o.read()
  root = ET.fromstring(txt)
  print(len(root))
  list = []
  for element in root:
    print("Element: %s, has work %s" % (element[-2].text, element[1].text))

    list.append({
        1: element[-2].text,
        2: element[1].text,
    })
  filename = "elements.json"
  with open(filename, 'w') as json_file:
    Jsonstr = json.dumps(list)
    json.dump(Jsonstr, json_file)


if __name__ == "__main__":
  main()
