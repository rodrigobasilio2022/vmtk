#!/usr/bin/env python

## Program:   VMTK
## Module:    $RCSfile: vmtkimagesmoothing.py,v $
## Language:  Python
## Date:      $Date: 2006/07/17 09:53:14 $
## Version:   $Revision: 1.8 $

##   Copyright (c) Luca Antiga, David Steinman. All rights reserved.
##   See LICENCE file for details.

##      This software is distributed WITHOUT ANY WARRANTY; without even 
##      the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
##      PURPOSE.  See the above copyright notices for more information.


import vtk
import sys

import pypes

vmtkpythonscript = 'vmtkPythonScript'

class vmtkPythonScript(pypes.pypeScript):

    def __init__(self):

        pypes.pypeScript.__init__(self)
        
        self.Image = None
        self.Image2 = None
        self.Surface = None
        self.Surface2 = None
        self.Mesh = None
        self.Mesh2 = None
        self.PythonScriptFileName = ''

        self.SetScriptName('vmtkpythonscript')
        self.SetScriptDoc('execute a python script contained in a file')
        self.SetInputMembers([
            ['Image','image','vtkImageData',1,'','the input image','vmtkimagereader'],
            ['Image2','image2','vtkImageData',1,'','the second input image','vmtkimagereader'],
            ['Surface','surface','vtkPolyData',1,'','the input surface','vmtksurfacereader'],
            ['Surface2','surface2','vtkPolyData',1,'','the second input surface','vmtksurfacereader'],
            ['Mesh','mesh','vtkUnstructuredGrid',1,'','the input mesh','vmtkmeshreader'],
            ['Mesh2','mesh2','vtkUnstructuredGrid',1,'','the second input mesh','vmtkmeshreader'],
            ['PythonScriptFileName','scriptfile','str',1,'','the name of the file were the Python script resides']
            ])
        self.SetOutputMembers([
            ['Image','oimage','vtkImageData',1,'','the output image','vmtkimagewriter'],
            ['Surface','osurface','vtkPolyData',1,'','the output surface','vmtksurfacewriter'],
            ['Mesh','omesh','vtkUnstructuredGrid',1,'','the output mesh','vmtkmeshwriter']
            ])

    def Execute(self):

        if self.PythonScriptFileName == '':
            self.PrintError('Error: no PythonScriptFileName')

        try:
            execfile(self.PythonScriptFileName)
        except Exception as error:
            self.PrintError("Python script error: %s" % error)


if __name__=='__main__':

    main = pypes.pypeMain()
    main.Arguments = sys.argv
    main.Execute()
