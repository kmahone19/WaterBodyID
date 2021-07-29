#import useful libraries
import sys, os, json
import qgis 
import qgis.core
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

#set up qgis 
qgis_prefix = os.getenv("QGIS_PREFIX_PATH")      
qgis.core.QgsApplication.setPrefixPath(qgis_prefix, True) 
qgs = qgis.core.QgsApplication([], False)
qgs.initQgis()

#import gui and class
import l4gui
from waterBodyHier import Stream, River, Canal, Lake, Pond, Reservoir

#Set classes to list vaiable to use later
waterTypes = [Stream, River, Canal, Lake, Pond, Reservoir]

#main function for creating Geopackages
def runAnalysis ():
    
  #Get file names and paths from input fields and assign variables  
  filename = ui.inputJson.text()
  linearOut = ui.output1.text()
  arealOut = ui.output2.text()
  
  #create layers and their data providers 
  fileFormat = "GPKG"
  linearLayer = qgis.core.QgsVectorLayer('LineString?crs=EPSG:4326&field=NAME:string(255)&field=TYPE:String(255)&field=LENGTH:integer', 'linear Features' , 'memory')
  linearProv = linearLayer.dataProvider()
  areaLayer = qgis.core.QgsVectorLayer('Polygon?crs=EPSG:4326&field=NAME:string(255)&field=TYPE:String(255)&field=AREA:integer', 'Areal Features' , 'memory')
  areaProv = areaLayer.dataProvider()
  
  #attempt creating file
  try:
      #read incoming JSON file
      with open(filename, encoding = "utf8") as file: 
        data = json.load(file)  
    
     #Create dicts for storing data
      nodeDict = {}
      waysDict = {}

      #seperate incoming data by way and node
      for element in data["elements"]:
          if element["type"] == "node":
              nodeDict[element["id"]] = element
          elif element["type"] == "way":
              waysDict[element["id"]] = element

      #Create list variables to store newly create features
      linearFeatures = []
      arealFeatures = []
      
      #create list variable of waterbody type attributes
      linearTypes = ["River", "Stream", "Canal"]
      arealTypes = ["Lake", "Pond","Reservoir"]
      
      #loop through dict and create a variable for individual way 
      for wayID in waysDict:             
       way = waysDict[wayID]
       
       #loop through list and create a variable storing new class object
       for waterType in waterTypes:
         results = waterType.fromOSMWay(way, nodeDict)
         
         #check results are linear or areal objects and add them to respective list
         if results.__str__()[0] in linearTypes:
          linearFeature = results.toQgsFeature()
          linearFeatures.append(linearFeature)
                
         elif results.__str__()[0] in arealTypes:
            arealFeature = results.toQgsFeature()
            arealFeatures.append(arealFeature)

      #use list of features to populate layer then write to geopackage file
      linearProv.addFeatures(linearFeatures) 
      qgis.core.QgsVectorFileWriter.writeAsVectorFormat( linearLayer, linearOut, "utf-8", linearLayer.crs(), fileFormat)

      areaProv.addFeatures(arealFeatures) 
      qgis.core.QgsVectorFileWriter.writeAsVectorFormat( areaLayer, arealOut, "utf-8", areaLayer.crs(), fileFormat)          
                
  #Catch errors during extraction
  except Exception as e:
    QMessageBox.information(mainWindow, 'Operation failed', "The process has failed: " + str(e.__class__) + ': ' + str(e), QMessageBox.Ok ) 
    ui.statusbar.clearMessage() 

#Functions for selecting JSON file and saving the GeoPackages
def selectJsonFile():
      
  fileName, _ = QFileDialog.getOpenFileName(mainWindow,"Select JSON", "","JSON (*.JSON)") 
  if fileName: 
    ui.inputJson.setText(fileName) 

def selectOutput1file():
      
  fileName, _ = QFileDialog.getSaveFileName(mainWindow,"Select Geopackage", "","OGC Geopackage (*.gpkg)") 
  if fileName: 
    ui.output1.setText(fileName) 

def selectOutput2file():
      
  fileName, _ = QFileDialog.getSaveFileName(mainWindow,"Select Geopackage", "","OGC Geopackage (*.gpkg)") 
  if fileName: 
    ui.output2.setText(fileName) 


#set up main window
app = QApplication(sys.argv) 

mainWindow = QMainWindow() 
ui = l4gui.Ui_MainWindow() 
ui.setupUi(mainWindow)

# connect signals  

#file Buttons  
ui.openFile.clicked.connect(selectJsonFile)
ui.save1.clicked.connect(selectOutput1file)
ui.save2.clicked.connect(selectOutput2file)

#Start button
ui.runBtn.clicked.connect(runAnalysis)

# run app 
mainWindow.show() 
sys.exit(app.exec_()) 