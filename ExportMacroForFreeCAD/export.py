import Mesh
import MeshPart
import os
import tempfile
doc = App.ActiveDocument
name = os.path.splitext(doc.FileName)[0]
outputFile=open(name+'.stl','w')
for obj in doc.Objects:
	if obj.ViewObject.Visibility:
		tmpFile = tempfile.mkstemp()
		file = tmpFile[1]
		obj.Shape.exportStl(file)
		importFile=open(file,'r')
		temp=importFile.readlines()
		for line in temp:
			if 'endsolid' in line:
				outputFile.write('endsolid '+obj.Label+'\n')
			elif 'solid' in line:
				outputFile.write('solid '+obj.Label+'\n')
			else:
				outputFile.write(line)
		importFile.close
		os.remove(file)