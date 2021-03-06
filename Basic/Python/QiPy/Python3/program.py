﻿from qipy import *
import configparser
import datetime
import time
import math
import inspect
import collections

#returns a type that represents the WaveData data
def getWaveDataType(sampleTypeId):
    if sampleTypeId is None or not isinstance(sampleTypeId, str):
        raise TypeError("sampleTypeId is not an instantiated string")

    intType = QiType()
    intType.Id = "intType"
    intType.QiTypeCode = QiTypeCode.Int32

    doubleType = QiType()
    doubleType.Id = "doubleType"
    doubleType.QiTypeCode = QiTypeCode.Double

    # note that the Order is the key (primary index)
    orderProperty = QiTypeProperty()
    orderProperty.Id = "Order"
    orderProperty.QiType = intType
    orderProperty.IsKey = True

    tauProperty = QiTypeProperty()
    tauProperty.Id = "Tau"
    tauProperty.QiType = doubleType

    radiansProperty = QiTypeProperty()
    radiansProperty.Id = "Radians"
    radiansProperty.QiType = doubleType

    sinProperty = QiTypeProperty()
    sinProperty.Id = "Sin"
    sinProperty.QiType = doubleType

    cosProperty = QiTypeProperty()
    cosProperty.Id = "Cos"
    cosProperty.QiType = doubleType

    tanProperty = QiTypeProperty()
    tanProperty.Id = "Tan"
    tanProperty.QiType = doubleType

    sinhProperty = QiTypeProperty()
    sinhProperty.Id = "Sinh"
    sinhProperty.QiType = doubleType

    coshProperty = QiTypeProperty()
    coshProperty.Id = "Cosh"
    coshProperty.QiType = doubleType

    tanhProperty = QiTypeProperty()
    tanhProperty.Id = "Tanh"
    tanhProperty.QiType = doubleType

    #create a QiType for WaveData Class
    wave = QiType()
    wave.Id = sampleTypeId
    wave.Name = "WaveDataSample"
    wave.Description = "This is a sample Qi type for storing WaveData type events"
    wave.QiTypeCode = QiTypeCode.Object
    wave.Properties = [orderProperty, tauProperty, radiansProperty, sinProperty, 
                       cosProperty, tanProperty, sinhProperty, coshProperty, tanhProperty]

    return wave
#returns a type that represents the WaveDataTarget data
def getWaveDataTargetType(sampleTypeId):
    if sampleTypeId is None or not isinstance(sampleTypeId, str):
        raise TypeError("sampleTypeId is not an instantiated string")

    intType = QiType()
    intType.Id = "intType"
    intType.QiTypeCode = QiTypeCode.Int32

    doubleType = QiType()
    doubleType.Id = "doubleType"
    doubleType.QiTypeCode = QiTypeCode.Double

    # note that the Order is the key (primary index)
    orderTargetProperty = QiTypeProperty()
    orderTargetProperty.Id = "OrderTarget"
    orderTargetProperty.QiType = intType
    orderTargetProperty.IsKey = True

    tauTargetProperty = QiTypeProperty()
    tauTargetProperty.Id = "TauTarget"
    tauTargetProperty.QiType = doubleType

    radiansTargetProperty = QiTypeProperty()
    radiansTargetProperty.Id = "RadiansTarget"
    radiansTargetProperty.QiType = doubleType

    sinTargetProperty = QiTypeProperty()
    sinTargetProperty.Id = "SinTarget"
    sinTargetProperty.QiType = doubleType

    cosTargetProperty = QiTypeProperty()
    cosTargetProperty.Id = "CosTarget"
    cosTargetProperty.QiType = doubleType

    tanTargetProperty = QiTypeProperty()
    tanTargetProperty.Id = "TanTarget"
    tanTargetProperty.QiType = doubleType

    sinhTargetProperty = QiTypeProperty()
    sinhTargetProperty.Id = "SinhTarget"
    sinhTargetProperty.QiType = doubleType

    coshTargetProperty = QiTypeProperty()
    coshTargetProperty.Id = "CoshTarget"
    coshTargetProperty.QiType = doubleType

    tanhTargetProperty = QiTypeProperty()
    tanhTargetProperty.Id = "TanhTarget"
    tanhTargetProperty.QiType = doubleType

    #create a QiType for WaveData Class
    wave = QiType()
    wave.Id = sampleTargetTypeId
    wave.Name = "WaveDataTargetSample"
    wave.Description = "This is a sample Qi type for storing WaveDataTarget type events"
    wave.QiTypeCode = QiTypeCode.Object
    wave.Properties = [orderTargetProperty, tauTargetProperty, radiansTargetProperty, sinTargetProperty, 
                       cosTargetProperty, tanTargetProperty, sinhTargetProperty, coshTargetProperty, tanhTargetProperty]

    return wave

#returns a type that represents WaveDataInteger data
def getWaveDataIntegerType(sampleTypeId):
    if sampleTypeId is None or not isinstance(sampleTypeId, str):
        raise TypeError("sampleTypeId is not an instantiated string")

    intType = QiType()
    intType.Id = "intType"
    intType.QiTypeCode = QiTypeCode.Int32

    # note that the Order is the key (primary index)
    orderTargetProperty = QiTypeProperty()
    orderTargetProperty.Id = "OrderTarget"
    orderTargetProperty.QiType = intType
    orderTargetProperty.IsKey = True

    sinIntProperty = QiTypeProperty()
    sinIntProperty.Id = "SinInt"
    sinIntProperty.QiType = intType

    cosIntProperty = QiTypeProperty()
    cosIntProperty.Id = "CosInt"
    cosIntProperty.QiType = intType

    tanIntProperty = QiTypeProperty()
    tanIntProperty.Id = "TanInt"
    tanIntProperty.QiType = intType

    #create a QiType for the WaveDataInteger Class
    wave = QiType()
    wave.Id = sampleIntegerTypeId
    wave.Name = "WaveDataIntegerSample"
    wave.Description = "This is a sample Qi type for storing WaveDataInteger type events"
    wave.QiTypeCode = QiTypeCode.Object
    wave.Properties = [orderTargetProperty, sinIntProperty, 
                       cosIntProperty, tanIntProperty]

    return wave

# Generate a new WaveData event
def nextWave(now, interval, multiplier, order):
    totalSecondsDay = (now - now.replace(hour=0, minute=0, second = 0, microsecond = 0)).total_seconds() * 1000
    intervalSeconds = (interval - interval.replace(hour=0, minute=0, second = 0, microsecond = 0)).total_seconds() * 1000
    radians = ((totalSecondsDay % intervalSeconds ) / intervalSeconds) * 2 * math.pi
        
    newWave = WaveData()
    newWave.Order = order
    newWave.Radians = radians
    newWave.Tau = radians / (2 * math.pi)
    newWave.Sin = multiplier * math.sin(radians)
    newWave.Cos = multiplier * math.cos(radians)
    newWave.Tan = multiplier * math.tan(radians)
    newWave.Sinh = multiplier * math.sinh(radians)
    newWave.Cosh = multiplier * math.cosh(radians)
    newWave.Tanh = multiplier * math.tanh(radians)
        
    return newWave

# we'll use the following for cleanup, supressing errors
def supressError(qiCall):
    try:
        qiCall()
    except Exception as e:
        print(("Encountered Error: {error}".format(error = e)))

def isprop(v):
  return isinstance(v, property)

def toString(event):
    string = ""
    props = inspect.getmembers(type(event), isprop)
    printOrder = [2,3,4,0,6,5,1,7,8]
    orderedProps = [props[i] for i in printOrder]
    for prop in orderedProps:
        value = prop[1].fget(event)
        if value is None:
            string += "{name}: , ".format(name = prop[0])
        else:
            string += "{name}: {value}, ".format(name = prop[0], value = value)
    return string[:-2]

def toWaveData(jsonObj):
    # Many JSON implementations leave default values out.  We compensate for WaveData, knowing
    # that all values should be filled in
    wave = WaveData()
    properties = inspect.getmembers(type(wave), isprop)
    for prop in properties:
        # Pre-Assign the default
        prop[1].fset(wave, 0)

        # 
        if prop[0] in jsonObj:
            value = jsonObj[prop[0]]
            if value is not None:
                prop[1].fset(wave, value)
    return wave


######################################################################################################
# The following define the identifiers we'll use throughout
######################################################################################################

sampleTypeId = "WaveData_SampleType"
sampleTargetTypeId = "WaveDataTarget_SampleType"
sampleIntegerTypeId = "WaveData_IntegerType"
sampleStreamId = "WaveData_SampleStream"
sampleBehaviorId = "WaveData_SampleBehavior"
sampleViewId = "WaveData_SampleView"
sampleViewIntId = "WaveData_SampleIntView"

try:
    config = configparser.ConfigParser()
    config.read('config.ini')

    client = QiClient(config.get('Access', 'Tenant'), config.get('Access', 'Address'), config.get('Credentials', 'Resource'), 
                      config.get('Credentials', 'Authority'), config.get('Credentials', 'ClientId'), config.get('Credentials', 'ClientSecret'))

    namespaceId = config.get('Configurations', 'Namespace')

    print("----------------------------------")
    print("  ___  _ ____")        
    print(" / _ \(_)  _ \ _   _ ")
    print("| | | | | |_) | | | |")
    print("| |_| | |  __/| |_| |")
    print(" \__\_\_|_|    \__, |")
    print("               |___/ ")	
    print("----------------------------------")
    print("Qi endpoint at {url}".format(url = client.Uri))
    print()

    ######################################################################################################
    # QiType get or creation
    ######################################################################################################
    print("Creating a QiType")
    waveType = getWaveDataType(sampleTypeId)
    waveType = client.getOrCreateType(namespaceId, waveType)

    ######################################################################################################
    # Qi Stream creation
    ######################################################################################################
    print("Creating a QiStream")
    stream = QiStream()
    stream.Id = sampleStreamId
    stream.Name = "WaveStreamPySample"
    stream.Description = "A Stream to store the WaveData events"
    stream.TypeId = waveType.Id
    stream.BehaviorId = None
    client.createOrUpdateStream(namespaceId, stream)

    ######################################################################################################
    # CRUD operations for events
    ######################################################################################################

    start = datetime.datetime.now()
    span = datetime.datetime.strptime("0:1:0", "%H:%M:%S")
    print("Inserting data")
    # Insert a single event
    event = nextWave(start, span, 2.0, 0)
    client.insertValue(namespaceId, stream.Id, event)

    # Insert a list of events
    waves = []
    for i in range(2, 20, 2):
        waves.append(nextWave(start + datetime.timedelta(seconds = i * 0.2), span, 2.0, i))
    client.insertValues(namespaceId, stream.Id, waves)

    # Get the last inserted event in a stream
    print("Getting latest event")
    wave = client.getLastValue(namespaceId, stream.Id, WaveData)
    print(toString(wave))
    print()

    # Get all the events
    waves = client.getWindowValues(namespaceId, stream.Id, WaveData, 0, 40)
    print("Getting all events")
    print("Total events found: " + str(len(waves)))
    for wave in waves:
        print(toString(wave))
    print()
    
    print("Updating events")
    # Update the first event
    event = nextWave(start, span, 4.0, 0)
    client.updateValue(namespaceId, stream.Id, event)

    # Update the rest of the events, adding events that have no prior index entry
    updatedEvents = []
    for i in range(2, 40, 2):
        event = nextWave(start + datetime.timedelta(seconds = i * 0.2), span, 4.0, i)
        updatedEvents.append(event)
    client.updateValues(namespaceId, stream.Id, updatedEvents)

    # Get all the events
    waves = client.getWindowValues(namespaceId, stream.Id, WaveData, 0, 40)
    print("Getting updated events")
    print("Total events found: " + str(len(waves)))
    for wave in waves:
        print(toString(wave))
    print()

    print("Replacing events")
    # replace one value
    event = nextWave(start, span, 10.0, 0)
    client.replaceValue(namespaceId, stream.Id, event)
    
    # replace multiple values
    replacedEvents = []
    for i in range(2, 40, 2):
        event = nextWave(start + datetime.timedelta(seconds=i * 0.2), span, 10.0, i)
        replacedEvents.append(event)
    client.replaceValues(namespaceId, stream.Id, replacedEvents)

    # Get all the events
    waves = client.getWindowValues(namespaceId, stream.Id, WaveData, 0, 40)
    print("Getting replaced events")
    print("Total events found: " + str(len(waves)))
    for wave in waves:
        print(toString(wave))
    print()
    ######################################################################################################
    # Stream behavior
    ######################################################################################################

    print("QiStreamBehaviors determine whether Qi interpolates or extrapolates data at the requested index location")
    print()
    # Stream behaviors modify retrieval.  We will retrieve three events using the default behavior, Continuous
    waves = client.getRangeValues(namespaceId, stream.Id, WaveData, "1", 0, 3, False, QiBoundaryType.ExactOrCalculated)

    print("Default (Continuous) stream behavior, requesting data starting at index location '1', Qi will interpolate this value:")
    for wave in waves:
        print(("Order: {order}: Radians: {radians}".format(order = wave.Order, radians = wave.Radians)))

    # Create a Discrete stream behavior 
    discreteBehavior = QiStreamBehavior()
    discreteBehavior.Id = sampleBehaviorId
    discreteBehavior.Mode = QiStreamMode.Discrete
    discreteBehavior = client.getOrCreateBehavior(namespaceId, discreteBehavior)

    stream.BehaviorId = discreteBehavior.Id
    client.createOrUpdateStream(namespaceId, stream)

    waves = client.getRangeValues(namespaceId, stream.Id, WaveData, "1", 0, 3, False, QiBoundaryType.ExactOrCalculated)
    print()
    print("Discrete stream behavior, Qi does not interpolate and returns the data starting at the next index location containing data:")
    for wave in waves:
        print(("Order: {order}: Radians: {radians}".format(order = wave.Order, radians = wave.Radians)))

    ######################################################################################################
    # Stream Views
    ######################################################################################################

    #Create additional types to define our targets
    waveTargetType = getWaveDataTargetType(sampleTargetTypeId)
    waveTargetType = client.getOrCreateType(namespaceId, waveTargetType)

    waveIntegerType = getWaveDataIntegerType(sampleIntegerTypeId)
    waveIntegerType = client.getOrCreateType(namespaceId, waveIntegerType)

    #Create a QiViewProperty objects when we want to explicitly map one property to another
    vp1 = QiViewProperty()
    vp1.SourceId = "Order"
    vp1.TargetId = "OrderTarget"

    vp2 = QiViewProperty()
    vp2.SourceId = "Sin"
    vp2.TargetId = "SinInt"
    
    vp3 = QiViewProperty()
    vp3.SourceId = "Cos"
    vp3.TargetId = "CosInt"
    
    vp4 = QiViewProperty()
    vp4.SourceId = "Tan"
    vp4.TargetId = "TanInt"
    
    #Create a view mapping our original type to our target type, data shape is the same so let Qi handle the mapping
    view = QiView()
    view.Id = sampleViewId
    view.Name = "SampleView"
    view.TargetTypeId = waveTargetType.Id
    view.SourceTypeId = waveType.Id

    #Data shape and data types are different so include explicit mappings between properties
    manualView = QiView()
    manualView.Id = sampleViewIntId
    manualView.Name = "SampleIntView"
    manualView.TargetTypeId = waveIntegerType.Id
    manualView.SourceTypeId = waveType.Id
    manualView.Properties = [vp1, vp2, vp3, vp4]
    
    automaticView = client.getOrCreateView(namespaceId, view)
    manualView = client.getOrCreateView(namespaceId, manualView)
    
    viewMap1 = QiViewMap()
    viewMap1 = client.getViewMap(namespaceId, automaticView.Id)

    viewMap2 = QiViewMap()
    viewMap2 = client.getViewMap(namespaceId, manualView.Id)

    rangeWaves = client.getRangeValues(namespaceId, stream.Id, WaveData, "1", 0, 3, False, QiBoundaryType.ExactOrCalculated)
    print()
    print("QiViews")
    print("Here is some of our data as it is stored on the server:")
    for way in rangeWaves:
        print(("Sin: {sin}, Cos: {cos}, Tan: {tan}".format(sin = way.Sin, cos = way.Cos, tan = way.Tan)))

    #view data when retrieved with a view
    rangeWaves = client.getRangeValues(namespaceId, stream.Id, WaveDataTarget, "1", 0, 3, False, QiBoundaryType.ExactOrCalculated, automaticView.Id)
    print()
    print("Specifying a view with a QiType of the same shape returns values that are automatically mapped to the target QiType's properties:")
    for way in rangeWaves:
        print(("SinTarget: {sinTarget}, CosTarget: {cosTarget}, TanTarget: {tanTarget}".format(sinTarget = way.SinTarget, cosTarget = way.CosTarget, tanTarget = way.TanTarget)))

    rangeWaves = client.getRangeValues(namespaceId, stream.Id, WaveDataInteger, "1", 0, 3, False, QiBoundaryType.ExactOrCalculated, manualView.Id)
    print()
    print("QiViews can also convert certain types of data, here we return integers where the original values were doubles:")
    for way in rangeWaves:
        print(("SinInt: {sinInt}, CosInt: {cosInt}, TanInt: {tanInt}".format(sinInt = way.SinInt, cosInt = way.CosInt, tanInt = way.TanInt)))

    print ()
    print ("We can query Qi to return the QiViewMap for our QiView, here is the one generated automatically:")
    for prop in viewMap1.Properties:
        print(("{source} => {dest}".format(source = prop.SourceId, dest = prop.TargetId)))
		
    print ()
    print ("Here is our explicit mapping, note QiViewMap will return all properties of the Source Type, even those without a corresponding Target property:")
    for prop in viewMap2.Properties:
        if hasattr(prop,'TargetId'):
            print(("{source} => {dest}".format(source = prop.SourceId, dest = prop.TargetId)))
        else:
            print(("{source} => {dest}".format(source = prop.SourceId, dest = 'Not mapped')))

    ######################################################################################################
    # Delete events
    ######################################################################################################
    print()
    print('Deleting values from the QiStream')
    # remove a single value from the stream
    client.removeValue(namespaceId, stream.Id, 0)

    # remove multiple values from the stream
    client.removeWindowValues(namespaceId, stream.Id, 0, 40)
    try:
        event = client.getLastValue(namespaceId, stream.Id, WaveData)
        if event != None:
            raise ValueError
    except TypeError:
        pass
    print("All values deleted successfully!")

except Exception as i:
    print(("Encountered Error: {error}".format(error = i)))
    print()

finally:
    ######################################################################################################
    # QiType, QiStream, QiView and QiBehavior deletion
    ######################################################################################################

    # Clean up the remaining artifacts
    print("Cleaning up")
    print("Deleting the stream")
    supressError(lambda: client.deleteStream(namespaceId, sampleStreamId))

    print("Deleting the types")
    supressError(lambda: client.deleteType(namespaceId, sampleTypeId))
    supressError(lambda: client.deleteType(namespaceId, sampleTargetTypeId))
    supressError(lambda: client.deleteType(namespaceId, sampleIntegerTypeId))

    print("Deleting the behavior")
    supressError(lambda: client.deleteBehavior(namespaceId, sampleBehaviorId))

    print("Deleting the views")
    supressError(lambda: client.deleteView(namespaceId, sampleViewId))
    supressError(lambda: client.deleteView(namespaceId, sampleViewIntId))

print("done")
