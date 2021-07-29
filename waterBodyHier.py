import qgis
import qgis.core

# abstract class Waterbody is the root class of our hierarchy 
class Waterbody():
    
    # constructor (can be derived by subclasses)
    def __init__(self, name, geometry):
        self.name = name            # instance variable for storing the name of the watebrbody
        self.geometry = geometry    # instance variable for storing the a QgsGeometry object with the geometry for this waterbody

    # abstract static class function for creating a waterbody object if the given way satisfies
    # the required conditions; needs to be overridden by instantiable subclasses 
    def fromOSMWay(way, allNodes):     
        pass
    
    # abstract method for creating QgsFeature object for this waterbody;
    # needs to be overridden by instantiable subclasses 
    def toQgsFeature(self):
        pass
    

# abstract class LinearWaterBody is derived from class Waterbody
class LinearWaterbody(Waterbody):
    
    # constructor (can be invoked by derived classes and takes care of the length computation)
    def __init__(self, name, geometry):
        super(LinearWaterbody, self).__init__(name, geometry)
        
        # calculate length of this linear waterbody
        qda = qgis.core.QgsDistanceArea() 
        qda.setEllipsoid('WGS84')
        length = qda.measureLength(geometry)

        # instance variable for storing the length of this linear waterbody
        self.length = qda.convertLengthMeasurement(length, qgis.core.QgsUnitTypes.DistanceMeters) 


# abstract class ArealWaterbody is derived from class Waterbody
class ArealWaterbody(Waterbody):

    # constructor (can be invoked by derived classes and takes care of the area computation)
    def __init__(self, name, geometry):
        super(ArealWaterbody, self).__init__(name, geometry)

        # calculate area of this areal waterbody
        qda = qgis.core.QgsDistanceArea() 
        qda.setEllipsoid('WGS84')
        area = qda.measureArea(geometry)

        # instance variable for storing the length of this areal waterbody
        self.area = qda.convertAreaMeasurement(area, qgis.core.QgsUnitTypes.AreaSquareMeters)


# class Stream is derived from class LinearWaterBody and can be instantiated
class Stream(LinearWaterbody):
    
    # constructor (calls LinearWaterbody constructor to initialize name, geometry, and length instance variables)
    def __init__(self, name, geometry):
        super(Stream,self).__init__(name, geometry)

    # override the fromOSMWay(...) static class function
    def fromOSMWay(way, allNodes):  
      #try checking for the tag waterway and if that tag's value is equal to stream
      try:
       key, value = "waterway", "stream"
       if key in way["tags"] and value == way["tags"][key]:  
         #save way's nodes as list
         wayNodes = way["nodes"]
         #try grabbing the name from the tags
         try:
           name = way["tags"]["name"]
         #if it doesn't exsit set name to unknown
         except KeyError:
           name = "unknown"
         #Loop through way's node list 
         points = []
         for nodeId in wayNodes:
          #for each node make a QgsObject from the lat lon points   
           point = qgis.core.QgsPointXY(allNodes[nodeId]["lon"],allNodes[nodeId]["lat"])
           points.append(point)
         #create line geometry for based on all points and construct a new stream object    
         lineGeometry = qgis.core.QgsGeometry.fromPolylineXY(points)
         newstream = Stream(name, lineGeometry)
         return newstream
      #if it fails move on    
      except KeyError:
         pass
    pass

    # override the toQgsFeature(...) method
    def toQgsFeature(self):
      stream = qgis.core.QgsFeature()
      stream.setGeometry(self.geometry)
      stream.setAttributes([self.name, "Stream",self.length])
      return stream
      
      pass 
    
    def __str__(self):
      return ("Stream", self.name, round(self.length, 2))      

class River(LinearWaterbody):
    
    # constructor (calls LinearWaterbody constructor to initialize name, geometry, and length instance variables)
    def __init__(self, name, geometry):
        super(River,self).__init__(name, geometry)

    # override the fromOSMWay(...) static class function
    def fromOSMWay(way, allNodes):  
      #try checking for the tag waterway and if that tag's value is equal to stream
      try:
       key, value = "waterway", "river"
       if key in way["tags"] and value == way["tags"][key]:  
         #save way's nodes as list
         wayNodes = way["nodes"]
         #try grabbing the name from the tags
         try:
           name = way["tags"]["name"]
         #if it doesn't exsit set name to unknown
         except KeyError:
           name = "unknown"
         #Loop through way's node list 
         points = []
         for nodeId in wayNodes:
          #for each node make a QgsObject from the lat lon points   
           point = qgis.core.QgsPointXY(allNodes[nodeId]["lon"],allNodes[nodeId]["lat"])
           points.append(point)
         #create line geometry for based on all points and construct a new stream object    
         lineGeometry = qgis.core.QgsGeometry.fromPolylineXY(points)
         newRiver = River(name, lineGeometry)
         return newRiver
      #if it fails move on    
      except KeyError:
         pass
    pass

    # override the toQgsFeature(...) method
    def toQgsFeature(self):
      river = qgis.core.QgsFeature()
      river.setGeometry(self.geometry)
      river.setAttributes([self.name, "River",self.length])
      return river
      
      pass 
    
    def __str__(self):
      return ("River", self.name, round(self.length, 2)) 
  
class Canal(LinearWaterbody):
    
    # constructor (calls LinearWaterbody constructor to initialize name, geometry, and length instance variables)
    def __init__(self, name, geometry):
        super(Canal,self).__init__(name, geometry)

    # override the fromOSMWay(...) static class function
    def fromOSMWay(way, allNodes):  
      #try checking for the tag waterway and if that tag's value is equal to stream
      try:
       key, value = "waterway", "canal"
       if key in way["tags"] and value == way["tags"][key]:  
         #save way's nodes as list
         wayNodes = way["nodes"]
         #try grabbing the name from the tags
         try:
           name = way["tags"]["name"]
         #if it doesn't exsit set name to unknown
         except KeyError:
           name = "unknown"
         #Loop through way's node list 
         points = []
         for nodeId in wayNodes:
          #for each node make a QgsObject from the lat lon points   
           point = qgis.core.QgsPointXY(allNodes[nodeId]["lon"],allNodes[nodeId]["lat"])
           points.append(point)
         #create line geometry for based on all points and construct a new stream object    
         lineGeometry = qgis.core.QgsGeometry.fromPolylineXY(points)
         newCanal = Canal(name, lineGeometry)
         return newCanal
      #if it fails move on    
      except KeyError:
         pass
    pass

    # override the toQgsFeature(...) method
    def toQgsFeature(self):
      canal = qgis.core.QgsFeature()
      canal.setGeometry(self.geometry)
      canal.setAttributes([self.name, "Canal",self.length])
      return canal
      
      pass 
    
    def __str__(self):
      return ("Canal", self.name, round(self.length, 2)) 

class Lake(ArealWaterbody):
    
    # constructor (calls LinearWaterbody constructor to initialize name, geometry, and length instance variables)
    def __init__(self, name, geometry):
        super(Lake,self).__init__(name, geometry)

    # override the fromOSMWay(...) static class function
    def fromOSMWay(way, allNodes):  
      #try checking for the tag waterway and if that tag's value is equal to stream
      try:
       key, value = "water", "lake"
       if key in way["tags"] and value == way["tags"][key]:  
         #save way's nodes as list
         wayNodes = way["nodes"]
         #try grabbing the name from the tags
         try:
           name = way["tags"]["name"]
         #if it doesn't exsit set name to unknown
         except KeyError:
           name = "unknown"
         #Loop through way's node list 
         points = []
         for nodeId in wayNodes:
          #for each node make a QgsObject from the lat lon points   
           point = qgis.core.QgsPointXY(allNodes[nodeId]["lon"],allNodes[nodeId]["lat"])
           points.append(point)
         #create geometry for based on all points and construct a new stream object    
         areaGeometry = qgis.core.QgsGeometry.fromPolygonXY([points])
         newLake = Lake(name, areaGeometry)
         return newLake
      #if it fails move on    
      except KeyError:
         pass
    pass

    # override the toQgsFeature(...) method
    def toQgsFeature(self):
      lake = qgis.core.QgsFeature()
      lake.setGeometry(self.geometry)
      lake.setAttributes([self.name, "Lake",self.area])
      return lake
      
      pass 
    
    def __str__(self):
      return ("Lake", self.name, round(self.area, 2)) 

class Pond(ArealWaterbody):
    
    # constructor (calls LinearWaterbody constructor to initialize name, geometry, and length instance variables)
    def __init__(self, name, geometry):
        super(Pond,self).__init__(name, geometry)

    # override the fromOSMWay(...) static class function
    def fromOSMWay(way, allNodes):  
      #try checking for the tag waterway and if that tag's value is equal to stream
      try:
       key, value = "water", "pond"
       if key in way["tags"] and value == way["tags"][key]:  
         #save way's nodes as list
         wayNodes = way["nodes"]
         #try grabbing the name from the tags
         try:
           name = way["tags"]["name"]
         #if it doesn't exsit set name to unknown
         except KeyError:
           name = "unknown"
         #Loop through way's node list 
         points = []
         for nodeId in wayNodes:
          #for each node make a QgsObject from the lat lon points   
           point = qgis.core.QgsPointXY(allNodes[nodeId]["lon"],allNodes[nodeId]["lat"])
           points.append(point)
         #create geometry for based on all points and construct a new stream object    
         areaGeometry = qgis.core.QgsGeometry.fromPolygonXY([points])
         newPond = Pond(name, areaGeometry)
         return newPond
      #if it fails move on    
      except KeyError:
         pass
    pass

    # override the toQgsFeature(...) method
    def toQgsFeature(self):
      pond = qgis.core.QgsFeature()
      pond.setGeometry(self.geometry)
      pond.setAttributes([self.name, "Pond",self.area])
      return pond
      
      pass 
    
    def __str__(self):
      return ("Pond", self.name, round(self.area, 2)) 

class Reservoir(ArealWaterbody):
    
    # constructor (calls LinearWaterbody constructor to initialize name, geometry, and length instance variables)
    def __init__(self, name, geometry):
        super(Reservoir,self).__init__(name, geometry)

    # override the fromOSMWay(...) static class function
    def fromOSMWay(way, allNodes):  
      #try checking for the tags and if that tag's value is equal to desired key
      try:
       key, value = "water", "reservoir"
       if key in way["tags"] and value == way["tags"][key]:  
         #save way's nodes as list
         wayNodes = way["nodes"]
         #try grabbing the name from the tags
         try:
           name = way["tags"]["name"]
         #if it doesn't exsit set name to unknown
         except KeyError:
           name = "unknown"
         #Loop through way's node list 
         points = []
         for nodeId in wayNodes:
          #for each node make a QgsObject from the lat lon points   
           point = qgis.core.QgsPointXY(allNodes[nodeId]["lon"],allNodes[nodeId]["lat"])
           points.append(point)
         #create geometry for based on all points and construct a new stream object    
         areaGeometry = qgis.core.QgsGeometry.fromPolygonXY([points])
         newReservior = Reservoir(name, areaGeometry)
         return newReservior
      #if it fails move on    
      except KeyError:
         pass
    pass

    # override the toQgsFeature(...) method
    def toQgsFeature(self):
      reservoir = qgis.core.QgsFeature()
      reservoir.setGeometry(self.geometry)
      reservoir.setAttributes([self.name, "Reservoir",self.area])
      return reservoir
      
      pass 
    
    def __str__(self):
      return ("Reservoir", self.name, round(self.area, 2)) 