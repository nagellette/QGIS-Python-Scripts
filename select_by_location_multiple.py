## select the features and save into seperate shape files in a polygon layer

import processing

## change input output options
outputPath = "/home/nagellette-ws/Desktop/Output/"
outputAddName = "_selected.shp" ## string to add at the and of layer name
selectionBoundaryPath = "/home/nagellette-ws/Desktop/asd.shp" ## boundry path for selection polygon

mapcanvas = iface.mapCanvas()
layers = mapcanvas.layers()
#print len(layers)
boundary = iface.addVectorLayer(selectionBoundaryPath, "boundary", "ogr")

for layer in layers:
    processing.runalg("qgis:selectbylocation", layer, boundary, u'within', False, 0)
    QgsVectorFileWriter.writeAsVectorFormat( layer, outputPath + layer.name() + outputAddName, "utf-8", None, "ESRI Shapefile", onlySelected=True)