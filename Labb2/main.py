import vtk

reader = vtk.vtkImageReader()
reader.SetFileName("BostonTeapot.raw")
reader.SetDataByteOrderToBigEndian()
reader.SetNumberOfScalarComponents(1)
reader.SetFileDimensionality(3)
reader.SetDataExtent(0, 255, 0, 255, 0, 177)
reader.SetDataScalarTypeToUnsignedChar()
reader.Update()

output = reader.GetOutput()

contour = vtk.vtkContourFilter()
contour.SetInputConnection(reader.GetOutputPort())
contour.GenerateValues(10, 0, 255)

modelToContour = vtk.vtkPolyDataMapper()
modelToContour.SetInputConnection(contour.GetOutputPort())
contourActor = vtk.vtkActor()
contourActor.SetMapper(modelToContour)

#LOBSTER

contour2 = vtk.vtkContourFilter()
contour2.SetInputConnection(reader.GetOutputPort())
contour2.GenerateValues(40, 0, 255)

plane = vtk.vtkPlane()
plane.SetOrigin(79.51763853353643, 142.3562725373262, 113.45252769160768)
plane.SetNormal(0.8645083127426199, 0.2248326171531122, -0.44952827660002725)

clip = vtk.vtkClipPolyData()
clip.SetInputConnection(contour.GetOutputPort())
clip.SetClipFunction(plane)
clip.SetValue(0)
clip.Update()

contourToSlice = vtk.vtkPolyDataMapper()
contourToSlice.SetInputConnection(clip.GetOutputPort())
lobster = vtk.vtkActor()
lobster.SetMapper(contourToSlice)
lobster.RotateY(135)
lobster.RotateX(-35)


reWin = vtk.vtkRenderWindow()
reWin.SetWindowName("Labb 2")
reWin.SetSize(800, 600)
iren = vtk.vtkRenderWindowInteractor()

renderer = vtk.vtkRenderer()
renderer.AddActor(lobster)
renderer.AddActor(contourActor)

reWin.AddRenderer(renderer)
iren.SetRenderWindow(reWin)
reWin.Render()
iren.Start()
